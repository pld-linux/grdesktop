Summary:	GTK rdesktop frontend
Name:		grdesktop
Version:	0.22
Release:	0.9
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	6fa64e007e2b26bfe96e2516c0d6ddf4
URL:		http://www.nongnu.org/grdesktop/
BuildRequires:	gtk+2-devel
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	GConf2-devel
Requires:	rdesktop
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a graphical frontend for the remote
desktop client (rdesktop).

%prep
%setup -q

%build
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--with-keymap-path="%{_datadir}/rdesktop/keymaps"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

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
