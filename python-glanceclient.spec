#
# Conditional build:
%bcond_with	doc	# do build doc (missing deps)
%bcond_with	tests	# do perform "make test" (missing deps)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	OpenStack Image API Client Library
Name:		python-glanceclient
Version:	2.8.0
Release:	2
License:	Apache
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/python-glanceclient/%{name}-%{version}.tar.gz
# Source0-md5:	9504fa42fb8327f2d5a616bab8066006
URL:		https://pypi.python.org/pypi/python-glanceclient
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-pbr >= 2.0.0
BuildRequires:	python3-setuptools
%endif
Requires:	python-babel >= 2.3.4
Requires:	python-keystoneauth1 >= 3.0.1
Requires:	python-oslo.i18n >= 2.1.0
Requires:	python-oslo.utils >= 3.20.0
Requires:	python-pbr >= 2.0.0
Requires:	python-prettytable >= 0.7.1
Requires:	python-pyOpenSSL >= 0.14
Requires:	python-requests >= 2.14.2
Requires:	python-six >= 1.9.0
Requires:	python-warlock >= 1.0.1
Requires:	python-wrapt >= 1.7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a client library for Glance built on the OpenStack Images API.

%package -n python3-glanceclient
Summary:	OpenStack Image API Client Library
Group:		Libraries/Python
Requires:	python3-babel >= 2.3.4
Requires:	python3-keystoneauth1 >= 3.0.1
Requires:	python3-oslo.i18n >= 2.1.0
Requires:	python3-oslo.utils >= 3.20.0
Requires:	python3-pbr >= 2.0.0
Requires:	python3-prettytable >= 0.7.1
Requires:	python3-pyOpenSSL >= 0.14
Requires:	python3-requests >= 2.14.2
Requires:	python3-six >= 1.9.0
Requires:	python3-warlock >= 1.0.1
Requires:	python3-wrapt >= 1.7.0

%description -n python3-glanceclient
This is a client library for Glance built on the OpenStack Images API.

%package -n glanceclient
Summary:	OpenStack Image API Client
Group:		Libraries/Python
%if %{with python3}
Requires:	python3-glanceclient = %{version}-%{release}
%else
Requires:	%{name} = %{version}-%{release}
%endif

%description -n glanceclient
This is a client for Glance built on the OpenStack Images API.

%package apidocs
Summary:	API documentation for Python glanceclient module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona glanceclient
Group:		Documentation

%description apidocs
API documentation for Pythona glanceclient module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona glanceclient.

%prep
%setup -q

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd doc
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/glanceclient
%{py_sitescriptdir}/python_glanceclient-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-glanceclient
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/glanceclient
%{py3_sitescriptdir}/python_glanceclient-%{version}-py*.egg-info
%endif

%files -n glanceclient
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%attr(755,root,root) %{_bindir}/glance

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/*
%endif
