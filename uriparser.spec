%define	major 1
%define libname	%mklibname uriparser
%define devname %mklibname uriparser -d
%define oldlibname %mklibname uriparser 1

Summary:	URI parsing library - RFC 3986
Name:		uriparser
Version:	0.9.9
Release:	1
Group:		System/Libraries
License:	BSD
URL:		https://uriparser.sourceforge.net
Source0:	https://github.com/uriparser/uriparser/releases/download/%{name}-%{version}/%{name}-%{version}.tar.lz
BuildRequires:  cmake
BuildRequires:	cpptest-devel
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	lzip
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(gtest)

BuildSystem:	cmake

%description
Uriparser is a strictly RFC 3986 compliant URI parsing library written in C.
uriparser is cross-platform, fast, supports Unicode and is licensed under the
New BSD license.

%files
%{_bindir}/uriparse

#----------------------------------------------------------------------

%package -n %{libname}
Summary:	URI parsing library - RFC 3986
Group:          System/Libraries
%rename	%{oldlibname}

%description -n	%{libname}
Uriparser is a strictly RFC 3986 compliant URI parsing library written in C.
uriparser is cross-platform, fast, supports Unicode and is licensed under the
New BSD license.

%files -n %{libname}
%doc THANKS AUTHORS ChangeLog
%{_libdir}/*.so.%{major}*
%{_libdir}/cmake/%{name}-%{version}/*

#----------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for the uriparser library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:	%{libname} >= %{version}

%description -n	%{devname}
This package contains libraries and header files for developing applications
that use uriparser.

%files -n %{devname}
#doc doc/html
%{_datadir}/doc/%{name}/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#prep
#autosetup -p1 -n %{name}-%{version}

#build
#cmake
#make_build

#pushd doc
#    autoreconf -fi
    # Remove qhelpgenerator dependency, by commenting these lines in
    # Doxygen.in
    ## .qch output
    ## QCH_FILE = "../uriparser-doc-0.7.5.qch"
    ## QHG_LOCATION = "qhelpgenerator"
    #sed -i 's/^# .qch output.*//' Doxyfile.in
    #sed -i 's/^QCH.*//' Doxyfile.in
    #sed -i 's/^QHG.*//' Doxyfile.in
    #make
#popd

	
#install
#make_install -C build

#find %{buildroot} -name '*.la' -exec rm -f {} ';'
#rm -rf %{buildroot}%{_docdir}/uriparser-doc



