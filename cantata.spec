Name:		cantata
Version:	0.8.2
Release:	%mkrel 1
Summary:	Client for the Music Player Daemon (MPD)
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		http://kde-apps.org/content/show.php/Cantata?content=147733
Source0:	http://cantata.googlecode.com/files/cantata-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(taglib) >= 1.6
BuildRequires:	pkgconfig(libmtp)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	ffmpeg-devel
Requires:	mpd

%description
Cantata is a (yet another!) client for the music player daemon (MPD). 
Originally started as a fork of QtMPC, the code is now *very* different. To be 
true to QtMPCs origins, Cantata can be compiled with KDE support, or as a pure 
Qt4 application (however, note that this is not fully tested). The interface 
is very configurable - most views can be shown as either a list or tree 
structure.

%files -f %name.lang
%{_kde_bindir}/cantata
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_appsdir}/%{name}/%{name}.notifyrc
%{_kde_appsdir}/%{name}/cantataui.rc
%{_kde_iconsdir}/hicolor/scalable/apps/%{name}.svgz
%{_kde_iconsdir}/hicolor/*/actions/*
%{_kde_libdir}/kde4/libexec/cantata-dynamic

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 
%make

%install
%makeinstall_std -C build
%find_lang %name 


