#
Summary:	Cairo/GTK+ Canvas
Name:		goocanvas
Version:	0.9
Release:	1
License:	GPLv2
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/goocanvas/%{name}-%{version}.tar.gz
# Source0-md5:	600f28e51736b9d768108c32172b0726
URL:		http://sourceforge.net/projects/goocanvas/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	cairo-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-doc >= 1.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GooCanvas is a new canvas widget for GTK+ that uses the cairo 2D
library for drawing. It has a model/view split, and uses interfaces
for canvas items and views, so you can easily turn any application
object into canvas items.

%package devel
Summary:	Header files for goocanvas
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for goocanvas.

%package static
Summary:	GooCanvas static libraries
Summary(pl):	Statyczne biblioteki GooCanvas
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GooCanvas static libraries.

%description static -l pl
Statyczne biblioteki GooCanvas.

%package apidocs
Summary:	goocanvas API documentation
Summary(pl):	Dokumentacja API goocanvas
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
goocanvas API documentation.

%description apidocs -l pl
Dokumentacja API goocanvas.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root)    %{_libdir}/libgoocanvas.so.3.0.0

%files devel
%defattr(644,root,root,755)
%dir {_includedir}/goocanvas-1.0
%{_includedir}/goocanvas-1.0/goocanvas.h
%{_includedir}/goocanvas-1.0/goocanvasellipse.h
%{_includedir}/goocanvas-1.0/goocanvasenumtypes.h
%{_includedir}/goocanvas-1.0/goocanvasgroup.h
%{_includedir}/goocanvas-1.0/goocanvasimage.h
%{_includedir}/goocanvas-1.0/goocanvasitem.h
%{_includedir}/goocanvas-1.0/goocanvasitemmodel.h
%{_includedir}/goocanvas-1.0/goocanvasitemsimple.h
%{_includedir}/goocanvas-1.0/goocanvasmarshal.h
%{_includedir}/goocanvas-1.0/goocanvaspath.h
%{_includedir}/goocanvas-1.0/goocanvaspolyline.h
%{_includedir}/goocanvas-1.0/goocanvasrect.h
%{_includedir}/goocanvas-1.0/goocanvasstyle.h
%{_includedir}/goocanvas-1.0/goocanvastable.h
%{_includedir}/goocanvas-1.0/goocanvastext.h
%{_includedir}/goocanvas-1.0/goocanvasutils.h
%{_includedir}/goocanvas-1.0/goocanvaswidget.h
%{_libdir}/libgoocanvas.la
%{_pkgconfigdir}/goocanvas.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgoocanvas.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/goocanvas
