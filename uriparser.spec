%define	major 1
%define libname	%mklibname uriparser %{major}
%define develname %mklibname -d uriparser

Summary:	URI parsing library - RFC 3986
Name:		uriparser
Version:	0.7.5
Release:	%mkrel 1
Group:		System/Libraries
License:	BSD
URL:		http://%{name}.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		uriparser-0.7.5-doc_Makefile_in.patch
BuildRequires:	cpptest-devel
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	pkgconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Uriparser is a strictly RFC 3986 compliant URI parsing library written in C.
uriparser is cross-platform, fast, supports Unicode and is licensed under the
New BSD license.

%package -n	%{libname}
Summary:	URI parsing library - RFC 3986
Group:          System/Libraries

%description -n	%{libname}
Uriparser is a strictly RFC 3986 compliant URI parsing library written in C.
uriparser is cross-platform, fast, supports Unicode and is licensed under the
New BSD license.

%package -n	%{develname}
Summary:	Development files for the uriparser library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:	%{libname} >= %{version}

%description -n	%{develname}
This package contains libraries and header files for developing applications
that use uriparser.

%prep

%setup -q
%patch0 -p1 -b .doc_Makefile_in
sed -i 's/\r//' THANKS
sed -i 's/\r//' COPYING
iconv -f iso-8859-1 -t utf-8 -o THANKS{.utf8,}
mv THANKS{.utf8,}

%build
autoreconf -fi
%configure2_5x \
 --disable-static
pushd doc
    autoreconf -fi
    # Remove qhelpgenerator dependency, by commenting these lines in
    # Doxygen.in
    ## .qch output
    ## QCH_FILE = "../uriparser-doc-0.7.5.qch"
    ## QHG_LOCATION = "qhelpgenerator"
    sed -i 's/^# .qch output.*//' Doxyfile.in
    sed -i 's/^QCH.*//' Doxyfile.in
    sed -i 's/^QHG.*//' Doxyfile.in
    %configure2_5x
    %make
popd

%make

%check
make check

%install
rm -rf %{buildroot}

%makeinstall_std INSTALL="install -p"

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}%{_docdir}/uriparser-doc

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%doc THANKS AUTHORS COPYING ChangeLog
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root,-)
%doc doc/html
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

