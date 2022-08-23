#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pysubnettree
Version  : 0.35
Release  : 29
URL      : https://files.pythonhosted.org/packages/3d/32/ffa0e8150c2a455bb202e1a1ca384ff3e6ea746968d92f5a53bfd6e4b368/pysubnettree-0.35.tar.gz
Source0  : https://files.pythonhosted.org/packages/3d/32/ffa0e8150c2a455bb202e1a1ca384ff3e6ea746968d92f5a53bfd6e4b368/pysubnettree-0.35.tar.gz
Summary  : The PySubnetTree package provides a Python data structure SubnetTree
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pysubnettree-filemap = %{version}-%{release}
Requires: pypi-pysubnettree-lib = %{version}-%{release}
Requires: pypi-pysubnettree-license = %{version}-%{release}
Requires: pypi-pysubnettree-python = %{version}-%{release}
Requires: pypi-pysubnettree-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : python3-dev

%description
..
.. Version number is filled in automatically.
.. |version| replace:: 0.35
===============================================
PySubnetTree - A Python Module for CIDR Lookups
===============================================

%package filemap
Summary: filemap components for the pypi-pysubnettree package.
Group: Default

%description filemap
filemap components for the pypi-pysubnettree package.


%package lib
Summary: lib components for the pypi-pysubnettree package.
Group: Libraries
Requires: pypi-pysubnettree-license = %{version}-%{release}
Requires: pypi-pysubnettree-filemap = %{version}-%{release}

%description lib
lib components for the pypi-pysubnettree package.


%package license
Summary: license components for the pypi-pysubnettree package.
Group: Default

%description license
license components for the pypi-pysubnettree package.


%package python
Summary: python components for the pypi-pysubnettree package.
Group: Default
Requires: pypi-pysubnettree-python3 = %{version}-%{release}

%description python
python components for the pypi-pysubnettree package.


%package python3
Summary: python3 components for the pypi-pysubnettree package.
Group: Default
Requires: pypi-pysubnettree-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(pysubnettree)

%description python3
python3 components for the pypi-pysubnettree package.


%prep
%setup -q -n pysubnettree-0.35
cd %{_builddir}/pysubnettree-0.35
pushd ..
cp -a pysubnettree-0.35 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656400415
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pysubnettree
cp %{_builddir}/pysubnettree-0.35/COPYING %{buildroot}/usr/share/package-licenses/pypi-pysubnettree/5e33d4674a821a666e7bb1fb7717d193ac234713
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-pysubnettree

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pysubnettree/5e33d4674a821a666e7bb1fb7717d193ac234713

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
