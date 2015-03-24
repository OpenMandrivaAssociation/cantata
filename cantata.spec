Summary:	Client for the Music Player Daemon (MPD)
Name:		cantata
Version:	1.5.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://code.google.com/p/cantata/
# NOTE:
# As of January 14th 2014, google code no longer allows adding new downloads. 
# Therefore, the google code download page has been replaced with this page. 
# New downloads (from 1.3.0 onwards) will be served from google drive.
# No longer direct link to the source.
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	cdparanoia
BuildRequires:	cdda-devel
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	pkgconfig(libmtp)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(libmusicbrainz5)
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
Requires:	oxygen-icon-theme
Suggests:	lame

%description
Cantata is a (yet another!) client for the music player daemon (MPD).
Originally started as a fork of QtMPC, the code is now *very* different. To be
true to QtMPCs origins, Cantata can be compiled with KDE support, or as a pure
Qt4 application (however, note that this is not fully tested). The interface
is very configurable - most views can be shown as either a list or tree
structure.

%files -f %{name}.lang
%doc AUTHORS ChangeLog LICENSE README TODO
%{_kde_bindir}/%{name}
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_appsdir}/solid/actions/cantata-play-audiocd.desktop
%{_kde_datadir}/%{name}
%{_kde_libdir}/%{name}
%{_kde_iconsdir}/hicolor/*/apps/%{name}.*
#------------------------------------------------------------------------------

%prep
%setup -q


# Hack to fix install path for x86_64 build
# TODO report upstream for a fix -done.
sed -i s,lib/cantata,%{_lib}/cantata,g replaygain/CMakeLists.txt
sed -i s,lib/cantata,%{_lib}/cantata,g replaygain/albumscanner.cpp
sed -i s,lib/cantata,%{_lib}/cantata,g tags/CMakeLists.txt


%build
%cmake_qt5 \
    -DENABLE_QT5=ON \
    -DENABLE_HTTP_STREAM_PLAYBACK=ON \
    -DENABLE_REMOTE_DEVICES=ON

%make

%install
%makeinstall_std -C build

%find_lang %{name}

