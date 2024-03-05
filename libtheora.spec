#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : libtheora
Version  : 1.1.1
Release  : 43
URL      : http://downloads.xiph.org/releases/theora/libtheora-1.1.1.tar.bz2
Source0  : http://downloads.xiph.org/releases/theora/libtheora-1.1.1.tar.bz2
Summary  : Development tools for Theora applications.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libtheora-lib = %{version}-%{release}
Requires: libtheora-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32libpng)
BuildRequires : pkgconfig(32ogg)
BuildRequires : pkgconfig(32vorbis)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(ogg)
BuildRequires : pkgconfig(vorbis)
BuildRequires : zlib-dev32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Change-png_sizeof-by-sizeof-function.patch

%description
Theora is Xiph.Org's first publicly released video codec, intended
for use within the Ogg's project's Ogg multimedia streaming system.
Theora is derived directly from On2's VP3 codec; Currently the two are
nearly identical, varying only in encapsulating decoder tables in the
bitstream headers, but Theora will make use of this extra freedom
in the future to improve over what is possible with VP3.

%package dev
Summary: dev components for the libtheora package.
Group: Development
Requires: libtheora-lib = %{version}-%{release}
Provides: libtheora-devel = %{version}-%{release}
Requires: libtheora = %{version}-%{release}

%description dev
dev components for the libtheora package.


%package dev32
Summary: dev32 components for the libtheora package.
Group: Default
Requires: libtheora-lib32 = %{version}-%{release}
Requires: libtheora-dev = %{version}-%{release}

%description dev32
dev32 components for the libtheora package.


%package doc
Summary: doc components for the libtheora package.
Group: Documentation

%description doc
doc components for the libtheora package.


%package lib
Summary: lib components for the libtheora package.
Group: Libraries
Requires: libtheora-license = %{version}-%{release}

%description lib
lib components for the libtheora package.


%package lib32
Summary: lib32 components for the libtheora package.
Group: Default
Requires: libtheora-license = %{version}-%{release}

%description lib32
lib32 components for the libtheora package.


%package license
Summary: license components for the libtheora package.
Group: Default

%description license
license components for the libtheora package.


%prep
%setup -q -n libtheora-1.1.1
cd %{_builddir}/libtheora-1.1.1
%patch1 -p1
pushd ..
cp -a libtheora-1.1.1 build32
popd
pushd ..
cp -a libtheora-1.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685645212
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1685645212
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libtheora
cp %{_builddir}/libtheora-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libtheora/5c1d4d8f603100ce87f5dab2182b9641c505bcd1 || :
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/theora/codec.h
/usr/include/theora/theora.h
/usr/include/theora/theoradec.h
/usr/include/theora/theoraenc.h
/usr/lib64/libtheora.so
/usr/lib64/libtheoradec.so
/usr/lib64/libtheoraenc.so
/usr/lib64/pkgconfig/theora.pc
/usr/lib64/pkgconfig/theoradec.pc
/usr/lib64/pkgconfig/theoraenc.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libtheora.so
/usr/lib32/libtheoradec.so
/usr/lib32/libtheoraenc.so
/usr/lib32/pkgconfig/32theora.pc
/usr/lib32/pkgconfig/32theoradec.pc
/usr/lib32/pkgconfig/32theoraenc.pc
/usr/lib32/pkgconfig/theora.pc
/usr/lib32/pkgconfig/theoradec.pc
/usr/lib32/pkgconfig/theoraenc.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/libtheora/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libtheora.so.0.3.10
/V3/usr/lib64/libtheoradec.so.1.1.4
/V3/usr/lib64/libtheoraenc.so.1.1.2
/usr/lib64/libtheora.so.0
/usr/lib64/libtheora.so.0.3.10
/usr/lib64/libtheoradec.so.1
/usr/lib64/libtheoradec.so.1.1.4
/usr/lib64/libtheoraenc.so.1
/usr/lib64/libtheoraenc.so.1.1.2

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libtheora.so.0
/usr/lib32/libtheora.so.0.3.10
/usr/lib32/libtheoradec.so.1
/usr/lib32/libtheoradec.so.1.1.4
/usr/lib32/libtheoraenc.so.1
/usr/lib32/libtheoraenc.so.1.1.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libtheora/5c1d4d8f603100ce87f5dab2182b9641c505bcd1
