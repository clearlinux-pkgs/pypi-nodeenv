#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-nodeenv
Version  : 1.6.0
Release  : 35
URL      : https://files.pythonhosted.org/packages/75/8d/14c4ac588711f8de0dd02a11460ed72f48cab65a998994ca20f40c6e1a8f/nodeenv-1.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/75/8d/14c4ac588711f8de0dd02a11460ed72f48cab65a998994ca20f40c6e1a8f/nodeenv-1.6.0.tar.gz
Summary  : Node.js virtual environment builder
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-nodeenv-bin = %{version}-%{release}
Requires: pypi-nodeenv-license = %{version}-%{release}
Requires: pypi-nodeenv-python = %{version}-%{release}
Requires: pypi-nodeenv-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: nodeenv
Provides: nodeenv-python
Provides: nodeenv-python3

%description
===========================
        
        ``nodeenv`` (node.js virtual environment) is a tool to create 
        isolated node.js environments.
        
        It creates an environment that has its own installation directories, 
        that doesn't share libraries with other node.js virtual environments.
        
        Also the new environment can be integrated with the environment which was built
        by virtualenv_ (python).

%package bin
Summary: bin components for the pypi-nodeenv package.
Group: Binaries
Requires: pypi-nodeenv-license = %{version}-%{release}

%description bin
bin components for the pypi-nodeenv package.


%package license
Summary: license components for the pypi-nodeenv package.
Group: Default

%description license
license components for the pypi-nodeenv package.


%package python
Summary: python components for the pypi-nodeenv package.
Group: Default
Requires: pypi-nodeenv-python3 = %{version}-%{release}

%description python
python components for the pypi-nodeenv package.


%package python3
Summary: python3 components for the pypi-nodeenv package.
Group: Default
Requires: python3-core
Provides: pypi(nodeenv)

%description python3
python3 components for the pypi-nodeenv package.


%prep
%setup -q -n nodeenv-1.6.0
cd %{_builddir}/nodeenv-1.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641459509
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-nodeenv
cp %{_builddir}/nodeenv-1.6.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-nodeenv/65f1b0655756044b7fd3f2d81d27cb0b39c1d348
cp %{_builddir}/nodeenv-1.6.0/debian-upstream/copyright %{buildroot}/usr/share/package-licenses/pypi-nodeenv/65f1b0655756044b7fd3f2d81d27cb0b39c1d348
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nodeenv

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-nodeenv/65f1b0655756044b7fd3f2d81d27cb0b39c1d348

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
