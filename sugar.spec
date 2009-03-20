# NOTE: Do not edit, file was generated by jhconvert

Name: sugar
Version: 0.84.1
Release: %mkrel 1
Summary: Sugar window manager
License: GPL/LGPL
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/glucose/sugar/sugar-0.84.1.tar.bz2

Patch: sugar-0.84.1-sugar-licence.patch
Patch1: sugar-0.84.1-sugar-start-script.patch
Patch2: sugar-0.84.1-sugar-logout-forever.patch

Requires: sugar-artwork >= 0.84.1
Requires: dbus  
Requires: dbus-x11  
Requires: GConf2  
Requires: gstreamer0.10-plugins-base  
Requires: gstreamer0.10-python  
Requires: gtk+2  
Requires: hal  
Requires: gnome-python-desktop  
Requires: matchbox-window-manager  
Requires: python-numpy  
Requires: openssh  
Requires: pygtk2.0  
Requires: python-gtksourceview  
Requires: python  
Requires: python-cjson  
Requires: sugar-toolkit >= 0.84.1
Requires: xdpyinfo  

BuildRequires: perl-XML-Parser  
BuildRequires: libGConf2-devel  
BuildRequires: gettext  
BuildRequires: libgtk+2-devel  
BuildRequires: intltool >= 0.33
BuildRequires: pygtk2.0-devel  
BuildRequires: libpython-devel  

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This package contains the base modules for Sugar.
Sugar is a graphical user interface aimed at children which promotes sharing
and collaborative learning. It was introduced on the One Laptop Per Child
(OLPC) XO laptop but is useful on other devices as well.

%package emulator
Summary: The emulator for the Sugar Desktop Environment
Group: Graphical desktop/Other
Requires: %{name} = %{version}-%{release}
Requires: x11-server-xephyr
%description emulator
This package contains the Sugar emulator. It is using Xephyr
to run a Sugar environment similar to what is on the XO laptop. 

%prep
%setup -q -n sugar-0.84.1
%patch -p1
%patch1 -p1
%patch2 -p1

%build
%configure 
make 

%install
rm -rf %{buildroot}
make  \
	DESTDIR=%{buildroot} \
	install
%find_lang sugar

install -d -m 0755 %{buildroot}/%{_sysconfdir}/X11/wmsession.d/
cat <<__EOF__ > %{buildroot}/%{_sysconfdir}/X11/wmsession.d/08sugar
NAME=Sugar
ICON=%{_datadir}/sugar/data/icons/module-about_me.svg
DESC=Sugar window manager
EXEC=%{_bindir}/sugar
SCRIPT:
exec %{_bindir}/sugar
__EOF__

%clean
rm -rf %{buildroot}

%files -f sugar.lang
%defattr(-,root,root,-)
%dir %{_datadir}/sugar
%config(noreplace) %{_sysconfdir}/X11/wmsession.d/*
%config(noreplace) %{_sysconfdir}/dbus*/system.d/*
%config(noreplace) %{_sysconfdir}/gconf/schemas/*
%{_bindir}/*
%exclude %{_bindir}/sugar-emulator
%{python_sitelib}/*
%{_datadir}/sugar/*
%{_datadir}/mime/packages/*
%{_datadir}/xsessions/sugar.desktop
%doc AUTHORS COPYING README

%files emulator
%defattr(-,root,root,-)
%{_bindir}/sugar-emulator

