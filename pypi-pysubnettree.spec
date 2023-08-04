#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-pysubnettree
Version  : 0.37
Release  : 35
URL      : https://files.pythonhosted.org/packages/6c/8f/51033e6d98418de21ce4e829b198cca62f28d9f6f9969e16e4f5d0e3b360/pysubnettree-0.37.tar.gz
Source0  : https://files.pythonhosted.org/packages/6c/8f/51033e6d98418de21ce4e829b198cca62f28d9f6f9969e16e4f5d0e3b360/pysubnettree-0.37.tar.gz
Summary  : The PySubnetTree package provides a Python data structure SubnetTree
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pysubnettree-license = %{version}-%{release}
Requires: pypi-pysubnettree-python = %{version}-%{release}
Requires: pypi-pysubnettree-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
..
.. Version number is filled in automatically.
.. |version| replace:: 0.37
===============================================
PySubnetTree - A Python Module for CIDR Lookups
===============================================

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
Requires: python3-core
Provides: pypi(pysubnettree)

%description python3
python3 components for the pypi-pysubnettree package.


%prep
%setup -q -n pysubnettree-0.37
cd %{_builddir}/pysubnettree-0.37
pushd ..
cp -a pysubnettree-0.37 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1691176546
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
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
cp %{_builddir}/pysubnettree-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-pysubnettree/5e33d4674a821a666e7bb1fb7717d193ac234713 || :
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pysubnettree/5e33d4674a821a666e7bb1fb7717d193ac234713

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
