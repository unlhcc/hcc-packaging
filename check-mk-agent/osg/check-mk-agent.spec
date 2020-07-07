# Based on Fedora packaging: https://src.fedoraproject.org/rpms/check-mk

# Producing (minimal) source tarfile:
# git clone https://github.com/tribe29/checkmk.git
# VER=1.6.0p8
# git archive --prefix=check-mk-agent-${VER}/ -o check-mk-agent-${VER}.tar v${VER} agents defines.make
# tar --delete --file check-mk-agent-${VER}.tar check-mk-agent-${VER}/agents/windows check-mk-agent-${VER}/agents/wnx
# gzip check-mk-agent-${VER}.tar

Name:       check-mk-agent
Version:    1.6.0p8
Release:    1%{?dist}
Summary:    The check-mk's Agent
License:    GPLv2 and GPLv3
URL:        https://checkmk.com/
Source:     check-mk-agent-%{version}.tar.gz
AutoReq:    0

# Minimal perl
%if 0%{?el6} || 0%{?el7}
BuildRequires: perl
%else
BuildRequires: perl-interpreter
%endif

%description
This package contains the check-mk's agent. Install the following
agent on all the machines you plan to monitor with check-mk.

%prep
%setup -q

%build

pushd agents
rm -f waitmax
# Enable debug info
perl -pi -e 's/gcc -s/gcc -g/g' Makefile
make waitmax

%install

# Agent's installation

pushd agents
mkdir -p %{buildroot}%{_sysconfdir}/xinetd.d
install -m 644 cfg_examples/xinetd.conf %{buildroot}%{_sysconfdir}/xinetd.d/check-mk-agent
install -m 644 cfg_examples/xinetd_caching.conf %{buildroot}%{_sysconfdir}/xinetd.d/check-mk-caching-agent

# Make sure check-mk-caching-agent is installed but not enabled by default
sed -i 's/\tdisable        = no/\tdisable        = yes/g' cfg_examples/xinetd_caching.conf \
  %{buildroot}%{_sysconfdir}/xinetd.d/check-mk-caching-agent

mkdir -p %{buildroot}%{_bindir}
install -m 755 check_mk_agent.linux %{buildroot}%{_bindir}/check_mk_agent
install -m 755 check_mk_caching_agent.linux %{buildroot}%{_bindir}/check_mk_caching_agent

# mk-job installation
install -m 755 mk-job %{buildroot}%{_bindir}/mk-job

# Waitmax's binary
install -m 755 waitmax %{buildroot}%{_bindir}/waitmax

mkdir -p %{buildroot}%{_datadir}/check-mk-agent/plugins
mkdir -p %{buildroot}%{_datadir}/check-mk-agent/local

# Create an /etc/check-mk-agent directory for agent's configuration files. Examples
# will be then available under the /usr/share/check_mk/agents/cfg_examples directory.
mkdir -p %{buildroot}%{_sysconfdir}/check-mk-agent

perl -pi \
    -e 's|MK_LIBDIR:-/usr/lib/check_mk_agent|MK_LIBDIR:-%{_datadir}/check-mk-agent|;' \
    -e 's|MK_CONFDIR:-/etc/check_mk|MK_CONFDIR:-%{_sysconfdir}/check-mk-agent|;' \
    %{buildroot}%{_bindir}/check_mk_agent

# Rename Linux plugins
rename '.linux' '' plugins/*

# Do not install all the plugins by default but make them available on a different
# directory. Users will then be able to symlink each of the plugins under the
# %%{_datadir}/check-mk-agent/plugins directory and finally mark them as active. (BZ: #1218516)
rm plugins/*.aix \
   plugins/*.freebsd \
   plugins/*.solaris
install -d -m 755 %{buildroot}%{_datadir}/check-mk-agent/available-plugins
install -m 755 plugins/* %{buildroot}%{_datadir}/check-mk-agent/available-plugins/
chmod 644 %{buildroot}%{_datadir}/check-mk-agent/available-plugins/README

# Convert unversioned python shebang to python2 for EL8 build compatibility
perl -p -i -e 's/^(#!.*python)$/${1}2/m' %{buildroot}%{_datadir}/check-mk-agent/available-plugins/*

# Upstream now ships systemd service and socket files
%if 0%{?fedora} || 0%{?rhel} >= 7
mkdir -p %{buildroot}%{_unitdir}
install -m 644 cfg_examples/systemd/check_mk@.service %{buildroot}%{_unitdir}/check_mk@.service
install -m 644 cfg_examples/systemd/check_mk.socket   %{buildroot}%{_unitdir}/check_mk.socket
%endif

%files
%{_bindir}/check_mk_agent
%{_bindir}/check_mk_caching_agent
%{_bindir}/mk-job
%{_bindir}/waitmax
%{_datadir}/check-mk-agent
%if 0%{?fedora} || 0%{?rhel} >= 7
%{_unitdir}/check_mk@.service
%{_unitdir}/check_mk.socket
%endif
%config(noreplace) %{_sysconfdir}/xinetd.d/check-mk-agent
%config(noreplace) %{_sysconfdir}/xinetd.d/check-mk-caching-agent
%config(noreplace) %{_sysconfdir}/check-mk-agent

%changelog
* Fri Jan 31 2020 John Thiltges <jthiltges@unl.edu> - 1.6.0p8-1
- New upstream release

* Fri Sep 06 2019 John Thiltges <jthiltges@unl.edu> - 1.5.0p21-1
- New upstream release

* Fri Jun 07 2019 John Thiltges <jthiltges@unl.edu> - 1.5.0p16-1
- Initial build of agent-only package
