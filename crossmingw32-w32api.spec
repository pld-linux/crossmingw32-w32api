Summary:	Mingw32 Binary Utility Development Utilities - Win32 API libraries
Summary(pl):	Zestaw narz�dzi mingw32 - biblioteki API Win32
Name:		crossmingw32-w32api
Version:	3.1
%define	apiver	%{version}
%define	apisrc	w32api-%{apiver}
%define runver	3.5
%define	runsrc	mingw-runtime-%{runver}
Release:	2
Epoch:		1
License:	Free
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/mingw/%{apisrc}-src.tar.gz
# Source0-md5:	3a23cb1f26f22e1307f0605b72983ae5
# only for headers
Source1:	http://dl.sourceforge.net/mingw/%{runsrc}-src.tar.gz
# Source1-md5:	cfa1e37c0e6e3243f82044687c859caa
Source2:	http://oss.sgi.com/projects/ogl-sample/ABI/glext.h
# NoSource2-md5:	a5738dcfa20119fa3e06ce479ca94acf
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

%description -l pl
crossmingw32 jest kompletnym systemem do kompilacji skro�nej,
pozwalaj�cym budowa� aplikacje MS Windows pod Linuksem u�ywaj�c
bibliotek mingw32. System sk�ada si� z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generuj�ce kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera pliki nag��wkowe i biblioteki Win32 API.

%package dx
Summary:	DirectX from MinGW Win32 API
Summary(pl):	DirectX z API Win32 dla MinGW
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description dx
DirectX from MinGW Win32 API.

%description dx -l pl
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
