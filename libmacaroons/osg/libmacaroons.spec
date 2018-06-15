Name:		libmacaroons
Version:	0.3.0
Release:	1%{?dist}
Summary:	C library supporting generation and use of macaroons

License:	BSD
URL:		https://github.com/rescrv/libmacaroons
Source0:	%url/archive/releases/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Fix for the inspect() method triggering an assert on newer versions of libsodium.
# See the upstream PR: https://github.com/rescrv/libmacaroons/pull/52
Patch0:		libmacaroons-hex-encoding.patch

BuildRequires:	libsodium-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	python2-devel
BuildRequires:	Cython

%description
%{summary}

%package -n python2-macaroons
Summary:	Python 2 bindings for libmacaroons
Requires:	%{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python2-macaroons}

%description -n python2-macaroons
%{summary}

%package devel
Summary:	Development libraries linking against libmacaroons
Requires:	%{name} = %{version}-%{release} 

%description devel
%{summary}

%prep
%setup -q
%patch0 -p 1

%build
autoreconf -i
%configure --enable-python-bindings
%make_build

%ldconfig_scriptlets

%install
%make_install
rm -f %{buildroot}%{_libdir}/%{name}.la
rm -f %{buildroot}%{_libdir}/%{name}.a
rm -f %{buildroot}%{python2_sitearch}/macaroons.a
rm -f %{buildroot}%{python2_sitearch}/macaroons.la

%files
%license LICENSE
%doc README
%{_libdir}/%{name}.so.*

%files -n python2-macaroons
%{python2_sitearch}/macaroons.so

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/macaroons.h

%changelog
* Thu Jun 14 2018 Brian Bockelman <bbockelm@cse.unl.edu> - 0.3.0-1
- Initial packaging of libmacaroons.


