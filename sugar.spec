# NOTE: Do not edit, file was generated by jhconvert

Name: sugar
Version: 0.84.2
Release: %mkrel 3
Summary: Sugar window manager
License: GPL/LGPL
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/glucose/sugar/sugar-0.84.2.tar.bz2

Patch: sugar-0.84.2-sugar-start-script.patch
Patch1: sugar-0.84.2-sugar-461.patch
Patch2: sugar-0.84.2-sugar-707.patch
Patch3: sugar-0.84.2-sugar-702.patch
Patch4: sugar-0.84.2-sugar-682.patch
Patch5: sugar-0.84.2-sugar-719.patch
Patch6: sugar-0.84.2-sugar-de.patch
Patch7: sugar-0.84.2-sugar-es.patch

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
Requires: sugar-base >= 0.84.0
Requires: sugar-toolkit >= 0.84.2
Requires: xdpyinfo  

BuildRequires: perl-XML-Parser  
BuildRequires: libGConf2-devel  
BuildRequires: gettext  
BuildRequires: gtk+2-devel  
BuildRequires: intltool >= 0.33
BuildRequires: pygtk2.0-devel  
BuildRequires: libpython-devel  
BuildRequires: sugar-base >= 0.84.0

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
%setup -q -n sugar-0.84.2
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%configure
make

%install
rm -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make DESTDIR=%{buildroot} install
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
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
%config %{_sysconfdir}/dbus*/system.d/*
%config %{_sysconfdir}/gconf/schemas/*
%{_bindir}/*
%exclude %{_bindir}/sugar-emulator
%{python_sitelib}/jarabe
%{_datadir}/sugar
%{_datadir}/mime/packages/*
%{_datadir}/xsessions/sugar.desktop
%doc AUTHORS COPYING README
%config %{_sysconfdir}/X11/wmsession.d/*

%files emulator
%defattr(-,root,root,-)
%{_bindir}/sugar-emulator

