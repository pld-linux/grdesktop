Summary:	GNOME rdesktop frontend
Summary(pl):	Nak³adka na rdesktop dla GNOME
Name:		grdesktop
Version:	0.23
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	46f8f3e2d4aa2433b8b1537fefa8a4b7
Patch0:		%{name}-gettext.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.nongnu.org/grdesktop/
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-utils
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	pkgconfig
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	rdesktop
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a graphical frontend for the remote
desktop client (rdesktop).

%description -l pl
Ten pakiet zawiera graficzn± nak³adkê na rdesktop.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--with-keymap-path="%{_datadir}/rdesktop/keymaps" \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_sysconfdir}/gconf/schemas/*
%{_pixmapsdir}/%{name}
%{_omf_dest_dir}/%{name}
%{_mandir}/man1/*
%{_desktopdir}/*
%{_datadir}/mime-info/*
%{_datadir}/application-registry/*
