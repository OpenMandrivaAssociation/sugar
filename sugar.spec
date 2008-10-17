%define commitid 454def195d
%define alphatag 20080822git%{commitid}

Summary: OLPC desktop environment
Name: sugar
Version: 0.82.9
Release: 1%{?dist}
#Release: 2.%{alphatag}%{?dist}
URL: http://dev.laptop.org
# git clone git://dev.laptop.org/sugar
# cd sugar
# git-checkout %{commitid}
#Source0: %{name}-%{version}-git%{commitid}.tar.bz2
Source0: http://dev.laptop.org/pub/sugar/sources/%{name}/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: System Environment/Libraries
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: pkgconfig
BuildRequires: perl-XML-Parser
BuildRequires: gettext
BuildRequires: python
BuildRequires: pygtk2.0-devel
BuildRequires: gtk2-devel

Requires: sugar-artwork
Requires: sugar-toolkit
Requires: gnome-python-desktop
Requires: matchbox-window-manager
Requires: python-telepathy
Requires: gstreamer0.10-python

%description

Desktop Environment for the One Laptop Per Child project; see the
sites http://fedoraproject.org/wiki/OLPC and http://www.laptop.org for
goals of this project.

%package emulator
Summary: The emulator for the Desktop Environment sugar
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: x11-server-xephyr

%description emulator
The emulator let's you test and debug sugar. For example it allows you to run 
multiple instances of sugar. 

%prep
%setup -q

%build
%configure
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%find_lang %name

%post
if (update-mime-database -v &> /dev/null); then
  update-mime-database "%{_datadir}/mime" > /dev/null
fi

%postun
if (update-mime-database -v &> /dev/null); then
  update-mime-database "%{_datadir}/mime" > /dev/null
fi

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING README

%config %{_sysconfdir}/dbus-1/system.d/NetworkManagerInfo.conf

%dir %{_datadir}/sugar
%{_datadir}/sugar/*

%{_datadir}/xsessions/sugar.desktop
%{_datadir}/dbus-1/services/*.service

%{_bindir}/*
%exclude %{_bindir}/sugar-emulator

%{_datadir}/mime/packages/sugar.xml

%files emulator
%defattr(-,root,root,-)
%{_bindir}/sugar-emulator

