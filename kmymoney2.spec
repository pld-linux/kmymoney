Summary:	Personal finance application similar to Microsoft Money
Summary(pl):	Program do finansów osobistych, podobny do Microsoft Money
Name:		kmymoney2
Version:	0.6
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	9cf0e358adb7756c0bf546155808e7ce
URL:		http://kmymoney2.sourceforge.net/
BuildRequires:	arts-qt-devel
BuildRequires:	artsc-devel
BuildRequires:	kdelibs-devel >= 9:3.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	xrender-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMyMoney is striving to be a full-featured replacement for your
Windows-based finance software. We are a full double-entry accounting
software package, for personal or small-business use.

%description -l pl
kmymoney2 to programowanie KDE do prowadzenia osobistych finansów.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/kmymoney2.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

echo "Categories=Qt;KDE;Utility;" >> \
	$RPM_BUILD_ROOT%{_desktopdir}/kde/kmymoney2.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/*
%{_desktopdir}/*
%{_desktopdir}/kde/*
%{_iconsdir}/*/*/*/*
%{_datadir}/mimelnk/application/x-kmymoney2.desktop
%{_mandir}/man1/*
