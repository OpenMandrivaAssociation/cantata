Summary:	Client for the Music Player Daemon (MPD)
Name:		cantata
Version:	1.1.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://code.google.com/p/cantata/
Source0:	https://%{name}.googlecode.com/files/%{name}-%{version}.tar.bz2
Patch0:		cantata-1.1.1-fix-po.patch
BuildRequires:	cdparanoia
BuildRequires:	cdda-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libmtp)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(libmusicbrainz5)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(speexdsp)
BuildRequires:	pkgconfig(taglib) >= 1.6
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	ffmpeg-devel
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
%{_kde_bindir}/%{name}
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_appsdir}/solid/actions/cantata-play-audiocd.desktop
%{_kde_datadir}/%{name}
%{_kde_libdir}/%{name}
%{_kde_iconsdir}/hicolor/*/apps/%{name}.*

#------------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

# Hack to fix install path for x86_64 build
sed -i s,lib/cantata,%{_lib}/cantata,g replaygain/CMakeLists.txt
sed -i s,lib/cantata,%{_lib}/cantata,g replaygain/albumscanner.cpp

%build
%cmake_kde4 \
	-DENABLE_CDPARANOIA=ON \
	-DENABLE_FFMPEG=ON \
	-DENABLE_KDE=ON \
	-DENABLE_MPG123=ON \
	-DENABLE_MTP=ON \
	-DENABLE_MUSICBRAINZ=ON \
	-DENABLE_OVERLAYSCROLLBARS=OFF \
	-DENABLE_PHONON=ON \
	-DENABLE_QT5=OFF \
	-DENABLE_SPEEXDSP=ON \
	-DENABLE_TAGLIB=ON \
	-DENABLE_TAGLIB_EXTRAS=ON \
	-DENABLE_UDISK2=OFF

%make

%install
%makeinstall_std -C build

%find_lang %{name}

%changelog
* Thu Aug 22 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1.1.1-1
- New version 1.1.1
- Add patch to fix build with broken po files in 1.1.1
- Update files list
- Update build options
- Update RuildRequires

* Fri Aug 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1.0.3-3
- Add patch to fix build with ffmpeg 2.0

* Fri May 31 2013 Giovanni Mariani <mc2374@mclink.it> 1.0.3-1
- New release 1.0.3

* Fri May 10 2013 Giovanni Mariani <mc2374@mclink.it> 1.0.2-1
- New release 1.0.2

* Fri May 03 2013 Giovanni Mariani <mc2374@mclink.it> 1.0.1-1
- New release 1.0.1
- Added P0 to fix a rpmlint error with the desktop file
- Adjusted BReqs according to the CMakeLists.txt file
- Updated URL tag
- Enabled support for optional programs
- Fixed file list

* Fri Jul 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.8.2-1mdv2012.0
+ Revision: 811280
- imported package cantata

