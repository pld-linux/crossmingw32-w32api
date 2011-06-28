Summary:	MinGW32 Binary Utility Development Utilities - Win32 API libraries
Summary(pl.UTF-8):	Zestaw narzędzi MinGW32 - biblioteki API Win32
Name:		crossmingw32-w32api
Version:	3.17
%define	apiver	%{version}
%define	apisrc	w32api-%{apiver}-2-mingw32
%define runver	3.18
%define	runsrc	mingwrt-%{runver}-mingw32
Release:	1
Epoch:		1
License:	Free
Group:		Development/Libraries
Source0:	http://downloads.sourceforge.net/mingw/%{apisrc}-src.tar.lzma
# Source0-md5:	7a14e6c9687c010eed35db95604548a4
# only for headers
Source1:	http://downloads.sourceforge.net/mingw/%{runsrc}-src.tar.gz
# Source1-md5:	34b54cb3379f871f0dcd5c20b69b0350
Source2:	http://www.opengl.org/registry/api/glext.h
# NoSource2-md5:	4bae59ed034b7c808081c0b56e42c0cb
Patch0:		%{name}-include_fix.patch
Patch1:		%{name}-mmsystem.patch
URL:		http://www.mingw.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	crossmingw32-gcc
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	crossmingw32-binutils >= 2.15.91.0.2-2
Obsoletes:	crossmingw32-platform
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		i386-mingw32
%define		target_platform i386-pc-mingw32
%define		_prefix		/usr/%{target}
%define		_libdir		%{_prefix}/lib

# strip fails on static COFF files
%define		no_install_post_strip 1

%define		filterout_ld	-Wl,-z,.*
%define		filterout_c	-gdwarf-3

%ifnarch %{ix86}
# arch-specific flags (like alpha's -mieee) are not valid for i386 gcc
%define		optflags	-O2
%endif

%description
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the MinGW32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains Win32 API includes and libraries.

%description -l pl.UTF-8
crossmingw32 jest kompletnym systemem do kompilacji skrośnej,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek MinGW32. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera pliki nagłówkowe i biblioteki Win32 API.

%package dx
Summary:	DirectX from MinGW Win32 API
Summary(pl.UTF-8):	DirectX z API Win32 dla MinGW
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	crossmingw32-dx
Obsoletes:	crossmingw32-dx

%description dx
DirectX from MinGW Win32 API.

%description dx -l pl.UTF-8
DirectX z API Win32 dla MinGW.

%prep
%setup -q -n %{apisrc} -a1
%patch0 -p1
%patch1 -p1

%build
cp /usr/share/automake/config.sub .
%{__autoconf}
./configure \
	--prefix=%{_prefix} \
	--host=%{target} \
	--build=%{_target_platform} \
	CFLAGS="-I`pwd`/%{runsrc}/include %{rpmcflags}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir}


%{!?debug:%{target}-strip -g $RPM_BUILD_ROOT%{_libdir}/*.a}

install %{SOURCE2} $RPM_BUILD_ROOT%{_includedir}/GL

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_includedir}
%{_includedir}/[!d]*.h
%{_includedir}/dbt.h
%{_includedir}/dde.h
%{_includedir}/ddeml.h
%{_includedir}/devguid.h
%{_includedir}/dhcpcsdk.h
%{_includedir}/dlgs.h
%{_includedir}/docobj.h
%{_includedir}/dsadmin.h
%{_includedir}/dsclient.h
%{_includedir}/dsgetdc.h
%{_includedir}/dsquery.h
%{_includedir}/dsrole.h
%{_includedir}/dvdevcod.h
%{_includedir}/dvdmedia.h
%{_includedir}/GL
%{_includedir}/ddk
%{_includedir}/gdiplus
%{_libdir}/lib[!d]*.a
%{_libdir}/libdhcpcsvc.a
%{_libdir}/libdlcapi.a
%{_libdir}/libdnsapi.a
%{_libdir}/libdxapi.a

%files dx
%defattr(644,root,root,755)
%{_libdir}/libd3d8.a
%{_libdir}/libd3d9.a
%{_libdir}/libd3dim.a
%{_libdir}/libd3drm.a
%{_libdir}/libd3dx8d.a
%{_libdir}/libd3dx9d.a
%{_libdir}/libd3dxof.a
%{_libdir}/libddraw.a
%{_libdir}/libdinput.a
%{_libdir}/libdinput8.a
%{_libdir}/libdmoguids.a
%{_libdir}/libdplayx.a
%{_libdir}/libdpnaddr.a
%{_libdir}/libdpnet.a
%{_libdir}/libdpnlobby.a
%{_libdir}/libdpvoice.a
%{_libdir}/libdsetup.a
%{_libdir}/libdsound.a
%{_libdir}/libdxerr8.a
%{_libdir}/libdxerr9.a
%{_libdir}/libdxguid.a
%{_includedir}/d3d9*.h
%{_includedir}/dshow.h
%{_includedir}/dxerr8.h
%{_includedir}/dxerr9.h
