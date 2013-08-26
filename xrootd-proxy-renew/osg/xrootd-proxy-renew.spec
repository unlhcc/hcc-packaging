
Name:      xrootd-proxy-renew
Version:   0.4
Release:   1%{?dist}
Summary:   Scripts for renewing a proxy for Xrootd usage

Group:     System Environment/Daemons
License:   ASL 2.0

Source0:   xrootd-gsi.cfg
Source1:   xrootd-gsi-init
Source2:   xrootd-gsi-renew
Source3:   xrootd-proxy-renew.cron

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

Requires: /usr/bin/myproxy-init /usr/bin/grid-proxy-init /usr/bin/openssl

%description
Scripts for renewing a proxy for Xrootd usage

%prep

%install

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/{cron.d,xrootd}

install -p -m 0644 %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/xrootd/
install -p -m 0755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/
install -p -m 0755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/
install -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/cron.d

%clean

rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/xrootd-gsi-init
%{_bindir}/xrootd-gsi-renew
%{_sysconfdir}/cron.d/xrootd-proxy-renew.cron
%config(noreplace) %{_sysconfdir}/xrootd/xrootd-gsi.cfg

%changelog
* Mon Aug 26 2013 Brian Bockelman <bbockelm@cse.unl.edu> - 0.4-1
- Make sure things are renewed on the correct filesystem.

* Sat Oct 15 2011 Brian Bockelman <bbockelm@cse.unl.edu> - 0.3-2
- Forgot to increase lifetime of myproxy-logon command.

* Sat Oct 15 2011 Brian Bockelman <bbockelm@cse.unl.edu> - 0.3-1
- Increase default lifetime to 168 hrs.

* Fri Oct 14 2011 Brian Bockelman <bbockelm@cse.unl.edu> - 0.2-1
- Support for VOMS extensions.

* Mon Feb 7 2011 Brian Bockelman <bbockelm@cse.unl.edu> 0.1-3
- Use setuid instead of seteuid when changing perms.

* Mon Feb 7 2011 Brian Bockelman <bbockelm@cse.unl.edu> 0.1-2
- Fix for location of the configuration file.

* Sat Feb 5 2011 Brian Bockelman <bbockelm@cse.unl.edu> 0.1-1
- Initial packaging

