%define pythonver 3.4
%define pythondir /usr/lib/python%{pythonver}/site-packages

Name:		python34-redis
Version:	2.10.6
Release:	1%{?dist}
Summary:    redis for python

Group:		Development/Languages
License:	BSD License
URL:		https://pypi.python.org/pypi/libtaxii
Source0:    redis-%{version}.tar.gz

BuildArch:  noarch
BuildRequires:	python34-devel, python34-setuptools
BuildRequires:  python34-pip, unzip
Requires:	python34, python34-pip

%description
Python redis

%prep
%setup -q -n redis-%{version}

%build
# intentianally left empty

%install
python3 setup.py install --root=$RPM_BUILD_ROOT

%files
%{pythondir}/redis
%{pythondir}/redis-%{version}-py%{pythonver}.egg-info

%changelog
* Tue Oct 31 2017 Andreas Muehlemann <andreas.muehlemann@switch.ch> - 2.10.6
- first version
