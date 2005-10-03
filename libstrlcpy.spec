Summary:	A library implementing OpenBSD strlcpy/strlcat functions.
Name:		libstrlcpy
%define		_snap 20050808
Version:	0.%{_snap}
Release:	0.2
License:	BSD
Group:		Libraries
Source0:	ftp://ftp.openbsd.org/pub/OpenBSD/src/lib/libc/string/strlcpy.c
# Source0-md5:	f25a1f8bdaa4b37ca89d571d84814c19
Source1:	ftp://ftp.openbsd.org/pub/OpenBSD/src/lib/libc/string/strlcat.c
# Source1-md5:	bf53a0fffc0d877812dbcc3aadb51b88
Source2:	ftp://ftp.openbsd.org/pub/OpenBSD/src/lib/libc/string/strlcpy.3
# Source2-md5:	b520c837f35bd97a1ff89456ecae7561
URL:		http://mail.gnome.org/archives/gtk-list/2000-April/msg00249.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		soname %{name}.0

%description
strlcpy and strlcat - consistent, safe, string copy and concatenation.

%package devel
Summary:	Development libraries for libstrlcpy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the development library for libstrlcpy.

%prep
%setup -q -c -T
cp %{SOURCE0} .
cp %{SOURCE1} .

%build
gcc %{rpmcflags} -c strlcpy.c
gcc %{rpmcflags} -c strlcat.c
gcc %{rpmldflags} -Wl,-soname,%{soname} -shared strlcpy.o strlcat.o -o %{soname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man3}
ln -s %{soname} $RPM_BUILD_ROOT%{_libdir}/%{name}.so
install %{soname} $RPM_BUILD_ROOT%{_libdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{soname}

%files devel
%attr(755,root,root) %{_libdir}/%{name}.so
%{_mandir}/man3/*
