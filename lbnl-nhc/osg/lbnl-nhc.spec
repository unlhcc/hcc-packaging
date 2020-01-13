%{!?_rel:%{expand:%%global _rel 0.1.4.2}}

%{!?sname:%global sname nhc}
%{!?nhc_script_dir:%global nhc_script_dir %{_sysconfdir}/%{sname}/scripts}
%{!?nhc_helper_dir:%global nhc_helper_dir %{_libexecdir}/%{sname}}

Summary: LBNL Node Health Check
Name: lbnl-nhc
Version: 1.4.2
#Release: %{_rel}%{?dist}
#Release: 1%{?dist}
Release: 1.20200113.2%{?dist}
License: US Dept. of Energy (BSD-like)
Group: Applications/System
URL: https://github.com/mej/nhc/
Source: https://github.com/mej/nhc/archive/nhc-%{version}.tar.gz
Patch1: condor.patch
Patch2: test_lbnl_file.nhc-Put-all-process-substitution.patch
Packager: %{?_packager}%{!?_packager:Michael Jennings <mej@lbl.gov>}
Vendor: %{?_vendorinfo}%{!?_vendorinfo:LBNL NHC Project (https://github.com/mej/nhc/)}
Requires: bash
Obsoletes: warewulf-nhc <= 1.4.2-1
BuildArch: noarch
BuildRoot: %{?_tmppath}%{!?_tmppath:/var/tmp}/%{name}-%{version}-%{release}-root
BuildRequires: autoconf automake

%description
This package contains the LBNL Node Health Check system.

TORQUE (and other resource managers) allow for the execution of a
script to determine if a node is "healthy" or "unhealthy" and
potentially mark unhealthy nodes as unavailable.  The scripts
contained in this package provide a flexible, extensible mechanism for
collecting health checks to be run on your cluster and specifying
which checks should be run on which nodes.


%prep
%setup -q -n nhc-%{version}

%patch1 -p1
%patch2 -p1

%build
./autogen.sh
%{configure}
%{__make} %{?mflags}


%install
umask 0077
%{__make} install DESTDIR=$RPM_BUILD_ROOT %{?mflags_install}


%check
%{__make} test


%triggerpostun -p /bin/bash -- warewulf-nhc <= 1.4.2-1
if [ $1 -gt 0 -a $2 -eq 0 ]; then
    cd %{_sysconfdir}/%{sname}/scripts
    for SCRIPT in ww_*.nhc.rpmsave ; do
        if [ -e $SCRIPT ]; then
            NEWSCRIPT=lbnl${SCRIPT##ww}
            NEWSCRIPT=${NEWSCRIPT%%.rpmsave}
            echo warning: Auto-fixing script naming due to modified script ${SCRIPT%%.rpmsave}
            mv -v $NEWSCRIPT $NEWSCRIPT.rpmnew && mv -v $SCRIPT $NEWSCRIPT
        fi
    done 2>/dev/null
fi


%clean
test "$RPM_BUILD_ROOT" != "/" && %{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc COPYING ChangeLog LICENSE nhc.conf contrib/nhc.cron
%dir %{_sysconfdir}/%{sname}/
%dir %{_localstatedir}/lib/%{sname}/
%dir %{_localstatedir}/run/%{sname}/
%dir %{nhc_script_dir}/
%dir %{nhc_helper_dir}/
%config(noreplace) %{_sysconfdir}/%{sname}/%{sname}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{sname}
%config(noreplace) %{nhc_script_dir}/*.nhc
%config(noreplace) %{nhc_helper_dir}/*
%config(noreplace) %{_sbindir}/%{sname}
%config(noreplace) %{_sbindir}/%{sname}-genconf
%config(noreplace) %{_sbindir}/%{sname}-wrapper

%changelog
* Mon Jan 13 2020 John Thiltges <jthiltges@unl.edu> - 1.4.2-1.20200113.2
- Initial support for HTCondor
- Upstream fix for failing tests (212f4f0f)
