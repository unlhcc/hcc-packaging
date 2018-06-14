Name:		libmacaroons
Version:	0.3.0
Release:	0%{?dist}
Summary:	C library supporting generation and use of macaroons.

Group:		System Environment/Libraries
License:	BSD 3-clause
URL:		https://github.com/rescrv/libmacaroons/releases
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	libsodium-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:	python-devel
BuildRequires:	Cython

%description
%{summary}

%package -n python2-macaroons
Summary:	Python 2 bindings for libmacaroons
Requires:	%{name} = %{version}-%{release}

%description -n python2-macaroons
%{summary}

%package devel
Summary:	Development libraries linking against libmacaroons
Requires:	%{name} = %{version}-%{release} 

%description devel
%{summary}

%prep
%setup -q


%build
autoreconf -i
%configure --enable-python-bindings
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/%{name}.la
rm -f %{buildroot}%{_libdir}/%{name}.a
rm -f %{buildroot}%{python2_sitearch}/macaroons.a
rm -f %{buildroot}%{python2_sitearch}/macaroons.la

%files
%{_libdir}/%{name}.so.*

%files -n python2-macaroons
%{python2_sitearch}/macaroons.so

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/macaroons.h

%changelog

