Name:           hcc-ca-certs
Version:        1.5
Release:        2%{?dist}
Summary:        HCC-CA Certs

Group:          System Environment/Base
License:        Unknown
URL:            https://github.com/unlhcc/hcc-ca-certs
Source0:        hcc-ca-certs-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch


%description
%{summary}


%prep
%setup -q


%build


%install
cp -ra etc $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%attr(0644,root,root) /etc/pki/tls/certs/*
%attr(-,root,root) /etc/openldap/cacerts/*
/etc/grid-security/certificates/*
%doc


%changelog
* Wed May 08 2019 John Thiltges <jthiltges2@unl.edu> - 1.5-2
- Remove LetsEncrypt CA in favor of using local system certificate store

* Wed May 08 2019 John Thiltges <jthiltges2@unl.edu> - 1.5-1
- Update red-puppet.unl.edu CA cert with new expiration
- Add new HCC-CA cert
- Add LetsEncrypt as trusted LDAP CA

* Wed Jan 10 2018 John Thiltges <jthiltges2@unl.edu> - 1.4-1
- Removed expired red-man CA

* Thu Oct 15 2015 Garhan Attebury <garhan.attebury@unl.edu> - 1.3-1
- Added Puppet CA from red-puppet.unl.edu

* Wed Aug 13 2014 Garhan Attebury <garhan.attebury@unl.edu> - 1.2-1
- Added hcc_puppet_ca certs from red-man.unl.edu

* Thu Sep 06 2012 Garhan Attebury <garhan.attebury@unl.edu> - 1.0-1
- HCC-CA Initial Package
