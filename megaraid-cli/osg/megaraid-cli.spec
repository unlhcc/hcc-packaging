Summary: MegaCli from LSI repackaged for use at Nebraska
Name: megaraid-cli
Version: 8.07.14
Release: 1%{dist}
License: Public Domain
Group: Administration Tools

Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libsysfs

%description
This package contains the LSI MegaCli utility

%prep
%setup

%install
mkdir -p %{buildroot}%{_bindir}
install --mode=0755 opt/MegaRAID/MegaCli/MegaCli64 %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
install --mode=0755 opt/MegaRAID/MegaCli/libstorelibir-2.so.14.07-0 %{buildroot}%{_libdir}

%ifarch x86_64
pushd %{buildroot}%{_bindir}
ln -s MegaCli64 MegaCli
popd
%else
install --mode=0755 opt/MegaRAID/MegaCli/MegaCli %{buildroot}%{_bindir}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/MegaCli
%{_bindir}/MegaCli64
%{_libdir}/libstorelibir-2.so.14.07-0

%changelog
* Tue Nov 29 2016 John Thiltges <jthiltges@unl.edu> - 8.07.14-1
- Update version
- Do not include MegaCli (32-bit) version in 64-bit package

* Mon Sep 16 2013 Garhan Attebury <garhan.attebury@unl.edu> - 8.07.10-1
- New version, repackaging of MegaCli-8.07.10-1.noarch.rpm

* Wed Feb 08 2012 Brian Bockelman <bbockelm@cse.unl.edu> - 1.0.0-2
- Rebuild for SL6.

* Sun Oct 9 2011 Garhan Attebury <attebury@cse.unl.edu> - 1.0.0-1
- Initial repackaging of LSI MegaCli utility
