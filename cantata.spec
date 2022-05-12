Summary:	Client for the Music Player Daemon (MPD)
Name:		cantata
Version:	2.5.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://github.com/CDrummond/cantata
Source0:	https://github.com/CDrummond/cantata/releases/download/v%{version}/%{name}-%{version}.tar.bz2

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
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(libvlc)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(speexdsp)
BuildRequires:	pkgconfig(taglib) >= 1.6
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	ffmpeg-devel
BuildRequires:	pkgconfig(libcddb)

Requires:	mpd
Recommends:	lame

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
%dir %{_datadir}/cantata/icons
%dir %{_datadir}/cantata/scripts
%dir %{_datadir}/cantata/translations
%{_bindir}/cantata
%{_libdir}/cantata/cantata-*
%{_datadir}/applications/cantata.desktop
%{_datadir}/cantata/icons/*.*g
%{_datadir}/cantata/scripts/cantata-*
%{_iconsdir}/hicolor/*/apps/%{name}*.*g
%{_datadir}/cantata/translations/cantata_*.qm

#------------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

# Hack to fix install path for x86_64 build
# TODO report upstream for a fix -done.
sed -i -e "s,LINUX_LIB_DIR lib,LINUX_LIB_DIR %{_lib},g" CMakeLists.txt

%build
%cmake_qt5 \
    -DENABLE_HTTP_STREAM_PLAYBACK=ON \
    -DENABLE_REMOTE_DEVICES=ON

%make_build

%install
%make_install -C build

