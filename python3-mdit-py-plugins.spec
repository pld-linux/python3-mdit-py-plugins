#
# Conditional build:
%bcond_with	doc	# Sphinx documentation (not included in sdist)
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	Collection of core plugins for markdown-it-py
Summary(pl.UTF-8):	Zbiór podstawowych wtyczek dla modułu markdown-it-py
Name:		python3-mdit-py-plugins
Version:	0.3.0
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/mdit-py-plugins/
Source0:	https://files.pythonhosted.org/packages/source/m/mdit-py-plugins/mdit-py-plugins-%{version}.tar.gz
# Source0-md5:	285b8d911d1c3b175e45b1fe5324da5b
URL:		https://pypi.org/project/mdit-py-plugins/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools >= 1:46.4.0
%if %{with tests}
BuildRequires:	python3-markdown-it-py >= 1.0.0
BuildRequires:	python3-pytest >= 3.6
BuildRequires:	python3-pytest-cov
BuildRequires:	python3-pytest-regressions
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
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
%setup -q -n mdit-py-plugins-%{version}

%build
%py3_build

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

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%{py3_sitescriptdir}/mdit_py_plugins
%{py3_sitescriptdir}/mdit_py_plugins-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/*
%endif
