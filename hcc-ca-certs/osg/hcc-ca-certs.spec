Name:           hcc-ca-certs
Version:        1.3
Release:        1%{?dist}
Summary:        HCC-CA Certs

Group:          System Environment/Base
License:        Unknown
URL:            http://hcc.unl.edu/
Source0:        hcc-ca-certs-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       authconfig, openssl, ca-certificates
BuildRequires:  authconfig

%description
%{summary}


%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/pki/tls/certs/
install -d $RPM_BUILD_ROOT/etc/openldap/cacerts/
install -d $RPM_BUILD_ROOT/etc/grid-security/certificates

install -m0644 etc/pki/tls/certs/hcc-ca.crt $RPM_BUILD_ROOT/etc/pki/tls/certs/hcc-ca.crt
/bin/ln -s /etc/pki/tls/certs/hcc-ca.crt $RPM_BUILD_ROOT/etc/openldap/cacerts/hcc-ca.crt
/bin/ln -s /etc/openldap/cacerts/hcc-ca.crt $RPM_BUILD_ROOT/etc/openldap/cacerts/bc130621.0

# red-man.unl.edu puppet CA
install -m0644 etc/grid-security/certificates/hcc_puppet_ca.pem $RPM_BUILD_ROOT/etc/grid-security/certificates/hcc_puppet_ca.pem
install -m0644 etc/grid-security/certificates/hcc_puppet_crl.pem $RPM_BUILD_ROOT/etc/grid-security/certificates/hcc_puppet_crl.pem
install -m0644 etc/grid-security/certificates/1592d59f.signing_policy $RPM_BUILD_ROOT/etc/grid-security/certificates/1592d59f.signing_policy
install -m0644 etc/grid-security/certificates/c15bdab5.signing_policy $RPM_BUILD_ROOT/etc/grid-security/certificates/c15bdab5.signing_policy
/bin/ln -s /etc/grid-security/certificates/hcc_puppet_ca.pem $RPM_BUILD_ROOT/etc/grid-security/certificates/1592d59f.0
/bin/ln -s /etc/grid-security/certificates/hcc_puppet_ca.pem $RPM_BUILD_ROOT/etc/grid-security/certificates/c15bdab5.0
/bin/ln -s /etc/grid-security/certificates/hcc_puppet_crl.pem $RPM_BUILD_ROOT/etc/grid-security/certificates/1592d59f.r0
/bin/ln -s /etc/grid-security/certificates/hcc_puppet_crl.pem $RPM_BUILD_ROOT/etc/grid-security/certificates/c15bdab5.r0

# red-puppet.unl.edu puppet CA
install -m0644 etc/grid-security/certificates/HCC-RedPuppet-CA.pem $RPM_BUILD_ROOT/etc/grid-security/certificates/HCC-RedPuppet-CA.pem
/bin/ln -s /etc/grid-security/certificates/HCC-RedPuppet-CA.pem $RPM_BUILD_ROOT/etc/grid-security/certificates/d0b20b1f.0
install -m0644 etc/grid-security/certificates/HCC-RedPuppet-CA.signing_policy $RPM_BUILD_ROOT/etc/grid-security/certificates/HCC-RedPuppet-CA.signing_policy
/bin/ln -s /etc/grid-security/certificates/HCC-RedPuppet-CA.signing_policy $RPM_BUILD_ROOT/etc/grid-security/certificates/d0b20b1f.signing_policy
install -m0644 etc/grid-security/certificates/HCC-RedPuppet-CA.crl_url $RPM_BUILD_ROOT/etc/grid-security/certificates/HCC-RedPuppet-CA.crl_url


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%attr(0644,root,root) /etc/pki/tls/certs/hcc-ca.crt
%attr(-,root,root) /etc/openldap/cacerts/*
/etc/grid-security/certificates/*
%doc


%changelog
* Thu Oct 15 2015 Garhan Attebury <garhan.attebury@unl.edu> - 1.3-1
- Added Puppet CA from red-puppet.unl.edu

* Wed Aug 13 2014 Garhan Attebury <garhan.attebury@unl.edu> - 1.2-1
- Added hcc_puppet_ca certs from red-man.unl.edu

* Thu Sep 06 2012 Garhan Attebury <garhan.attebury@unl.edu> - 1.0-1
- HCC-CA Initial Package
