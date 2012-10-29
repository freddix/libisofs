Summary:	Library to pack up hard disk files and directories into a ISO 9660 disk image
Name:		libisofs
Version:	1.2.4
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://files.libburnia-project.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	0a86f2cda3b86fc95f7c0efbd793f373
URL:		http://libburnia.pykix.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libburn-devel >= 1.2.4
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libisofs is the library to pack up hard disk files and directories
into a ISO 9660 disk image.

%package devel
Summary:	Header files for libisofs library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libisofs library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYRIGHT NEWS README Roadmap TODO
%attr(755,root,root) %ghost %{_libdir}/libisofs.so.?
%attr(755,root,root) %{_libdir}/libisofs.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/Tutorial
%attr(755,root,root) %{_libdir}/libisofs.so
%{_libdir}/libisofs.la
%{_includedir}/libisofs
%{_pkgconfigdir}/libisofs-1.pc

