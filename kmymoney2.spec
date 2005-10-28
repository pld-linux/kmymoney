Summary:	Personal finance application similar to Microsoft Money
Summary(pl):	Program do finansów osobistych, podobny do Microsoft Money
Name:		kmymoney2
Version:	0.6.4
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kmymoney2/%{name}-%{version}.tar.bz2
# Source0-md5:	01257a16ef26487f8891106b33ad2c64
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
KMyMoney stara siê byæ w pe³ni funkcjonalnym zamiennikiem dla
windowsowych programów finansowych. Jest to oprogramowanie o podwójnej
roli, do u¿ytku osobistego i dla ma³ych firm.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/kmymoney2.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

echo "Categories=Qt;KDE;Utility;" >> \
	$RPM_BUILD_ROOT%{_desktopdir}/kmymoney2.desktop

mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/apps/kmymoney2
%{_datadir}/apps/kmymoney2/default_accounts_en*
%lang(de) %{_datadir}/apps/kmymoney2/default_accounts_de.dat
%lang(fr) %{_datadir}/apps/kmymoney2/comptes_par_defaut_fr.dat
%lang(pt) %{_datadir}/apps/kmymoney2/default_accounts_ptPT.dat
%lang(ru) %{_datadir}/apps/kmymoney2/default_accounts_ruSU.dat
%dir %{_datadir}/apps/kmymoney2/html
%{_datadir}/apps/kmymoney2/html/home.html
%lang(de) %{_datadir}/apps/kmymoney2/html/home_de.de.html
%lang(fr) %{_datadir}/apps/kmymoney2/html/home_fr.fr.html
%lang(ru) %{_datadir}/apps/kmymoney2/html/home_ru.ru.html
%{_datadir}/apps/kmymoney2/icons
%{_datadir}/apps/kmymoney2/pics
%{_datadir}/apps/kmymoney2/tips
%{_datadir}/apps/kmymoney2/kmymoney2ui.rc
%{_desktopdir}/*
%{_iconsdir}/*/*/*/*
%{_datadir}/mimelnk/application/x-kmymoney2.desktop
%{_mandir}/man1/*
