Summary:	Mingw32 Binary Utility Development Utilities - Win32 API libraries
Summary(pl):	Zestaw narzêdzi mingw32 - biblioteki API Win32
Name:		crossmingw32-w32api
Version:	2.3
#%%define	api_date	20010606
#%%define	apisrc		w32api-%{version}-%{api_date}
%define	apiver	%{version}
%define	apisrc	w32api-%{apiver}
Release:	1
Epoch:		1
License:	Free
Group:		Development/Libraries
# requires cross-gcc installed... loop. Use binaries (doesn't change much, I think).
#Source0:	http://dl.sourceforge.net/mingw/%{apisrc}-src.tar.gz
Source0:	http://dl.sourceforge.net/mingw/%{apisrc}.tar.gz
# Source0-md5:	31d5e495150e392ac0fe6b51011d3fa2
URL:		http://www.mingw.org/
ExclusiveArch:	%{ix86}
Requires:	crossmingw32-runtime
Obsoletes:	crossmingw32-platform
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		i386-mingw32
%define		target_platform i386-pc-mingw32
%define		arch		%{_prefix}/%{target}

# strip fails on static COFF files
%define		no_install_post_strip 1

%description
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains Win32 API includes and libraries.

%description -l pl
crossmingw32 jest kompletnym systemem do kroskompilacji, pozwalaj±cym
budowaæ aplikacje MS Windows pod Linuksem u¿ywaj±c bibliotek mingw32.
System sk³ada siê z binutils, gcc z g++ i objc, libstdc++ - wszystkie
generuj±ce kod dla platformy i386-mingw32, oraz z bibliotek w formacie
COFF.

Ten pakiet zawiera pliki nag³ówkowe i biblioteki Win32 API.

%package dx
Summary:	DirectX from MinGW Win32 API
Summary(pl):	DirectX z API Win32 dla MinGW
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description dx
DirectX from MinGW Win32 API.

%description dx -l pl
DirectX z API Win32 dla MinGW.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{arch}/{include,lib}

cp -fa include/* $RPM_BUILD_ROOT%{arch}/include
cp -fa lib/* $RPM_BUILD_ROOT%{arch}/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{arch}/include/*
%{arch}/lib/lib[!d]*.a
%{arch}/lib/libdlcapi.a
%{arch}/lib/libdxapi.a

%files dx
%defattr(644,root,root,755)
%{arch}/lib/libd[!lx]*.a
%{arch}/lib/libdxguid.a
