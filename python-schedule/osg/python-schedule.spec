# Created by pyp2rpm-2.0.0
%global pypi_name schedule

Name:           python-%{pypi_name}
Version:        0.5.0
Release:        1%{?dist}
Summary:        Job scheduling for humans

License:        MIT
URL:            https://github.com/dbader/schedule
Source0:        https://files.pythonhosted.org/packages/fd/31/599a3387c2e98c270d5ac21a1575f3eb60a3712c192a0ca97a494a207739/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
schedule
========


.. image:: https://api.travis-
ci.org/dbader/schedule.svg?branch=master
        :target: https://travis-
ci.org/dbader/schedule

.. image::
https://coveralls.io/repos/dbader/schedule/badge.svg?branch=master
:target: https://coveralls.io/r/dbader/schedule

.. image::
https://img.shields.io/pypi/v/schedule.svg
        :target:
https://pypi.python.org/pypi/schedule

Python ...

%package -n     python2-%{pypi_name}
Summary:        Job scheduling for humans
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
schedule
========


.. image:: https://api.travis-
ci.org/dbader/schedule.svg?branch=master
        :target: https://travis-
ci.org/dbader/schedule

.. image::
https://coveralls.io/repos/dbader/schedule/badge.svg?branch=master
:target: https://coveralls.io/r/dbader/schedule

.. image::
https://img.shields.io/pypi/v/schedule.svg
        :target:
https://pypi.python.org/pypi/schedule

Python ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build

%install
%py2_install


%files -n python2-%{pypi_name} 
%doc README.rst LICENSE.txt
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Dec 18 2018 Brian Bockelman <bbockelm@cse.unl.edu> - 0.5.0-1
- Initial package, auto-converted from PyPI.
