%global debug_package %{nil}

Name: python-typing-extensions
Epoch: 100
Version: 4.2.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Python Typing Extensions
License: BSD-3-Clause
URL: https://github.com/python/typing/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Typing Extensions - Backported and Experimental Type Hints for Python.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-typing_extensions
Summary: Python Typing Extensions
Requires: python3
Provides: python3-typing-extensions = %{epoch}:%{version}-%{release}
Provides: python3dist(typing-extensions) = %{epoch}:%{version}-%{release}
Provides: python%{python3-version}-typing-extensions = %{epoch}:%{version}-%{release}
Provides: python%{python3-version}dist(typing-extensions) = %{epoch}:%{version}-%{release}
Provides: python%{python3-version-nodots}-typing-extensions = %{epoch}:%{version}-%{release}
Provides: python%{python3-version-nodots}dist(typing-extensions) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-typing_extensions
Typing Extensions - Backported and Experimental Type Hints for Python.

%files -n python%{python3_version_nodots}-typing_extensions
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-typing_extensions
Summary: Python Typing Extensions
Requires: python3
Provides: python3-typing-extensions = %{epoch}:%{version}-%{release}
Provides: python3dist(typing-extensions) = %{epoch}:%{version}-%{release}
Provides: python%{python3-version}-typing-extensions = %{epoch}:%{version}-%{release}
Provides: python%{python3-version}dist(typing-extensions) = %{epoch}:%{version}-%{release}
Provides: python%{python3-version-nodots}-typing-extensions = %{epoch}:%{version}-%{release}
Provides: python%{python3-version-nodots}dist(typing-extensions) = %{epoch}:%{version}-%{release}

%description -n python3-typing_extensions
Typing Extensions - Backported and Experimental Type Hints for Python.

%files -n python3-typing_extensions
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-typing-extensions
Summary: Python Typing Extensions
Requires: python3
Provides: python3-typing-extensions = %{epoch}:%{version}-%{release}
Provides: python3dist(typing-extensions) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-typing-extensions = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(typing-extensions) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-typing-extensions = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(typing-extensions) = %{epoch}:%{version}-%{release}

%description -n python3-typing-extensions
Typing Extensions - Backported and Experimental Type Hints for Python.

%files -n python3-typing-extensions
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
