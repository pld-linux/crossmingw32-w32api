Summary:	Mingw32 Binary Utility Development Utilities - Win32 API libraries
Summary(pl.UTF-8):	Zestaw narzędzi mingw32 - biblioteki API Win32
Name:		crossmingw32-w32api
Version:	3.8
%define	apiver	%{version}
%define	apisrc	w32api-%{apiver}
%define runver	3.11
%define	runsrc	mingw-runtime-%{runver}
Release:	2
Epoch:		1
License:	Free
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/mingw/%{apisrc}-src.tar.gz
# Source0-md5:	f38604492ba27c914d527a07cb5c164a
# only for headers
Source1:	http://dl.sourceforge.net/mingw/%{runsrc}-src.tar.gz
# Source1-md5:	642a9619b32fbf20602a6c8517b578df
Source2:	http://oss.sgi.com/projects/ogl-sample/ABI/glext.h
# NoSource2-md5:	0c40bd4545aa630e139043c2b12f0807
Patch0:		%{name}-include_fix.patch
URL:		http://www.mingw.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	crossmingw32-gcc
Requires:	crossmingw32-binutils >= 2.15.91.0.2-2
Obsoletes:	crossmingw32-platform
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		i386-mingw32
%define		target_platform i386-pc-mingw32
%define		_prefix		/usr/%{target}
%define		_libdir		%{_prefix}/lib

# strip fails on static COFF files
%define		no_install_post_strip 1

%ifarch alpha sparc sparc64 sparcv9
# alpha's -mieee and sparc's -mtune=* are not valid for target's gcc
%define		optflags	-O2
%endif

%description
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains Win32 API includes and libraries.

%description -l pl.UTF-8
crossmingw32 jest kompletnym systemem do kompilacji skrośnej,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek mingw32. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera pliki nagłówkowe i biblioteki Win32 API.

%package dx
Summary:	DirectX from MinGW Win32 API
Summary(pl.UTF-8):	DirectX z API Win32 dla MinGW
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description dx
DirectX from MinGW Win32 API.

%description dx -l pl.UTF-8
DirectX z API Win32 dla MinGW.

%prep
%setup -q -n w32api-%{version} -a1
%patch0 -p1

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
	inst_libdir=$RPM_BUILD_ROOT%{_libdir} \
	inst_includedir=$RPM_BUILD_ROOT%{_includedir}

%{!?debug:%{target}-strip -g $RPM_BUILD_ROOT%{_libdir}/*.a}

install %{SOURCE2} $RPM_BUILD_ROOT%{_includedir}/GL

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_includedir}
%{_includedir}/*
%{_libdir}/lib[!d]*.a
%{_libdir}/libdlcapi.a
%{_libdir}/libdxapi.a
%exclude %{_libdir}/libglut*.a
%exclude %{_includedir}/dxerr*.h
%exclude %{_includedir}/d3d*.h

%files dx
%defattr(644,root,root,755)
%{_libdir}/libd[!lx]*.a
%{_libdir}/libdxguid.a
%{_libdir}/libdxerr8.a
%{_libdir}/libdxerr9.a
%{_includedir}/dxerr*.h
%{_includedir}/d3d*.h
