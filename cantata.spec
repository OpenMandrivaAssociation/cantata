Summary:	Client for the Music Player Daemon (MPD)
Name:		cantata
Version:	2.0.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://github.com/CDrummond/cantata
# NOTE:
# As of January 14th 2014, google code no longer allows adding new downloads. 
# Therefore, the google code download page has been replaced with this page. 
# New downloads (from 1.3.0 onwards) will be served from google drive.
# No longer direct link to the source.
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libcdio_paranoia)
BuildRequires:	cdda-devel
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	qt5-qtmultimedia
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	qt5-linguist-tools
BuildRequires:	pkgconfig(libmtp)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(libmusicbrainz5)
BuildRequires:	pkgconfig(libvlc)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(speexdsp)
BuildRequires:	pkgconfig(taglib) >= 1.6
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	ffmpeg-devel
BuildRequires:  pkgconfig(QJson)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(taglib-extras)

Requires:	mpd
Suggests:	lame

%description
Cantata is a (yet another!) client for the music player daemon (MPD).
Originally started as a fork of QtMPC, the code is now *very* different. To be
true to QtMPCs origins, Cantata can be compiled with KDE support, or as a pure
Qt4 application (however, note that this is not fully tested). The interface
is very configurable - most views can be shown as either a list or tree
structure.

%files
%doc AUTHORS ChangeLog LICENSE README TODO
%dir %{_libdir}/cantata
%dir %{_datadir}/cantata
%dir %{_datadir}/cantata/config
%dir %{_datadir}/cantata/icons
%dir %{_datadir}/cantata/mpd
%dir %{_datadir}/cantata/scripts
%dir %{_datadir}/cantata/themes
%dir %{_datadir}/cantata/translations
%{_sysconfdir}/dbus-1/system.d/mpd.cantata.mounter.conf
%{_bindir}/cantata
%{_libdir}/cantata/cantata-*
%{_datadir}/applications/cantata.desktop
%{_datadir}/cantata/config/*.xml
%{_datadir}/cantata/fonts
%{_datadir}/cantata/icons/cantata
%{_datadir}/cantata/icons/*.*g
%{_datadir}/cantata/mpd/mpd.conf.template
%{_datadir}/cantata/scripts/cantata-*
%{_datadir}/cantata/scripts/mount.cifs.wrapper
%{_datadir}/cantata/themes/*.css
%{_datadir}/dbus-1/system-services/mpd.cantata.mounter.service
%{_iconsdir}/hicolor/*/apps/%{name}.*g
%{_datadir}/cantata/translations/cantata_*.qm

#------------------------------------------------------------------------------

%prep
%setup -q


# Hack to fix install path for x86_64 build
# TODO report upstream for a fix -done.
sed -i -e "s,LINUX_LIB_DIR lib,LINUX_LIB_DIR %{_lib},g" CMakeLists.txt
sed -i s,lib/cantata,%{_lib}/cantata,g devices/mounter/CMakeLists.txt
sed -i s,lib/cantata,%{_lib}/cantata,g devices/mounter/mpd.cantata.mounter.service.cmake

%build
%cmake_qt5 \
    -DENABLE_QT5=ON \
    -DENABLE_HTTP_STREAM_PLAYBACK=ON \
    -DENABLE_REMOTE_DEVICES=ON

%make

%install
%makeinstall_std -C build

