#
# Conditional build:
%bcond_with	doc	# Sphinx documentation (not included in sdist)
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	Collection of core plugins for markdown-it-py
Summary(pl.UTF-8):	Zbiór podstawowych wtyczek dla modułu markdown-it-py
Name:		python3-mdit-py-plugins
Version:	0.4.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/mdit-py-plugins/
Source0:	https://pypi.debian.net/mdit-py-plugins/mdit_py_plugins-%{version}.tar.gz
# Source0-md5:	3c943d03e071121cd41a9684c5ac5eb3
URL:		https://pypi.org/project/mdit-py-plugins/
BuildRequires:	python3-build
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-installer
%if %{with tests}
BuildRequires:	python3-markdown-it-py >= 1.0.0
BuildRequires:	python3-pytest >= 3.6
BuildRequires:	python3-pytest-cov
BuildRequires:	python3-pytest-regressions
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
%if %{with doc}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-myst-parser >= 0.14.0
BuildRequires:	python3-sphinx_book_theme >= 0.1.0
%endif
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of core plugins for markdown-it-py.

%description -l pl.UTF-8
Zbiór podstawowych wtyczek dla modułu markdown-it-py.

%package apidocs
Summary:	API documentation for Python mdit-py-plugins module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona mdit-py-plugins
Group:		Documentation

%description apidocs
API documentation for Python mdit-py-plugins module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona mdit-py-plugins.

%prep
%setup -q -n mdit_py_plugins-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%if %{with doc}
cd docs
%{__python3} -m sphinx -W . build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%{py3_sitescriptdir}/mdit_py_plugins
%{py3_sitescriptdir}/mdit_py_plugins-%{version}.dist-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/*
%endif
