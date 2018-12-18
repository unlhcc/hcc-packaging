# Created by pyp2rpm-2.0.0
%global pypi_name esmond_client

Name:           python-esmond-client
Version:        2.0
Release:        1%{?dist}
Summary:        API client libraries and command line tools for the ESnet Monitoring Daemon (esmond)

License:        BSD
URL:            http://software.es.net/esmond/
Source0:        https://files.pythonhosted.org/packages/4c/fb/49bb2ef971b05690815e0a7e36afa9204f9a06b01610906b6c7f67bda43c/esmond_client-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
*****************************************************************
Client
libraries and programs for esmond: ESnet Monitoring Daemon
*****************************************************************
==================================
Client programs for perfSONAR data
==================================

esmond-ps-get-endpoints
=======================

A discovery tool to quickly see what tests ...

%package -n     python2-esmond-client
Summary:        API client libraries and command line tools for the ESnet Monitoring Daemon (esmond)
%{?python_provide:%python_provide python2-esmond-client}
 
Requires:       python-requests
Requires:       python-dateutil
%description -n python2-esmond-client
*****************************************************************
Client
libraries and programs for esmond: ESnet Monitoring Daemon
*****************************************************************
==================================
Client programs for perfSONAR data
==================================

esmond-ps-get-endpoints
=======================

A discovery tool to quickly see what tests ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build

%install
%py2_install
cp %{buildroot}/%{_bindir}/esmond-ps-get %{buildroot}/%{_bindir}/esmond-ps-get-2
ln -sf %{_bindir}/esmond-ps-get-2 %{buildroot}/%{_bindir}/esmond-ps-get-%{python2_version}
cp %{buildroot}/%{_bindir}/esmond-ps-get-bulk %{buildroot}/%{_bindir}/esmond-ps-get-bulk-2
ln -sf %{_bindir}/esmond-ps-get-bulk-2 %{buildroot}/%{_bindir}/esmond-ps-get-bulk-%{python2_version}
cp %{buildroot}/%{_bindir}/esmond-ps-get-endpoints %{buildroot}/%{_bindir}/esmond-ps-get-endpoints-2
ln -sf %{_bindir}/esmond-ps-get-endpoints-2 %{buildroot}/%{_bindir}/esmond-ps-get-endpoints-%{python2_version}
cp %{buildroot}/%{_bindir}/esmond-ps-get-metadata %{buildroot}/%{_bindir}/esmond-ps-get-metadata-2
ln -sf %{_bindir}/esmond-ps-get-metadata-2 %{buildroot}/%{_bindir}/esmond-ps-get-metadata-%{python2_version}
cp %{buildroot}/%{_bindir}/esmond-ps-load-gridftp %{buildroot}/%{_bindir}/esmond-ps-load-gridftp-2
ln -sf %{_bindir}/esmond-ps-load-gridftp-2 %{buildroot}/%{_bindir}/esmond-ps-load-gridftp-%{python2_version}
cp %{buildroot}/%{_bindir}/esmond-ps-pipe %{buildroot}/%{_bindir}/esmond-ps-pipe-2
ln -sf %{_bindir}/esmond-ps-pipe-2 %{buildroot}/%{_bindir}/esmond-ps-pipe-%{python2_version}


%files -n python2-esmond-client
%doc README.rst
%{_bindir}/esmond-ps-get
%{_bindir}/esmond-ps-get-2
%{_bindir}/esmond-ps-get-%{python2_version}
%{_bindir}/esmond-ps-get-bulk
%{_bindir}/esmond-ps-get-bulk-2
%{_bindir}/esmond-ps-get-bulk-%{python2_version}
%{_bindir}/esmond-ps-get-endpoints
%{_bindir}/esmond-ps-get-endpoints-2
%{_bindir}/esmond-ps-get-endpoints-%{python2_version}
%{_bindir}/esmond-ps-get-metadata
%{_bindir}/esmond-ps-get-metadata-2
%{_bindir}/esmond-ps-get-metadata-%{python2_version}
%{_bindir}/esmond-ps-load-gridftp
%{_bindir}/esmond-ps-load-gridftp-2
%{_bindir}/esmond-ps-load-gridftp-%{python2_version}
%{_bindir}/esmond-ps-pipe
%{_bindir}/esmond-ps-pipe-2
%{_bindir}/esmond-ps-pipe-%{python2_version}
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/esmond_client-%{version}-py?.?.egg-info

%changelog
* Tue Dec 18 2018 Brian Bockelman <bbockelm@cse.unl.edu> - 2.0-1
- Initial package, auto-converted from PyPI.
