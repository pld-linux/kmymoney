#
# Conditional build:
%bcond_without	kbanking	# kbanking support
#
Summary:	Personal finance application similar to Microsoft Money
Summary(pl):	Program do finansów osobistych, podobny do Microsoft Money
Name:		kmymoney2
Version:	0.8.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://heanet.dl.sourceforge.net/kmymoney2/%{name}-%{version}.tar.bz2
# Source0-md5:	a39bcd548df8b4c6b9b5cf68d574a18e
URL:		http://kmymoney2.sourceforge.net/
%{?with_kbanking:BuildRequires:	aqbanking-frontend-kbanking-devel >= 0.1.0.0}
BuildRequires:	arts-qt-devel
BuildRequires:	artsc-devel
BuildRequires:	kdelibs-devel >= 9:3.0
BuildRequires:	libofx-devel
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	xrender-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMyMoney is striving to be a full-featured replacement for your
Windows-based finance software. We are a full double-entry accounting
software package, for personal or small-business use.

%description -l pl
KMyMoney stara siê byæ w pe³ni funkcjonalnym zamiennikiem dla
windowsowych programów finansowych. Jest to kompletny system podwójnego
ksiêgowania przeznaczony do u¿ytku osobistego i dla ma³ych firm.

%package devel
Summary:	kmymoney2 - header files
Summary(pl):	kmymoney2 - pliki nag³ówkowe
Summary(pt_BR):	Arquivos de inclusão para compilar aplicativos kmymoney2
Summary(ru):	èÅÄÅÒÙ ÄÌÑ ËÏÍÐÉÌÌÑÃÉÉ ÐÒÏÇÒÁÍÍ kmymoney2
Summary(uk):	èÅÄÅÒÉ ÄÌÑ ËÏÍÐ¦ÌÑÃ¦§ ÐÒÏÇÒÁÍ kmymoney2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files for kMyMoney2.

%description devel -l pl
Pakiet ten zawiera pliki nag³ówkowe potrzebne przy pisaniu w³asnych
programów wykorzystuj±cych kMyMoney2.

%description devel -l pt_BR
Este pacote contém os arquivos de inclusão que são necessários para
compilar aplicativos kMyMoney2.

%description devel -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÈÅÄÅÒÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ËÏÍÐÉÌÑÃÉÉ ÐÒÏÇÒÁÍÍ ÄÌÑ
kMyMoney2.

%description devel -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÈÅÄÅÒÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ËÏÍÐ¦ÌÑÃ¦§ ÐÒÏÇÒÁÍ ÄÌÑ
kMyMoney2.

%package kbanking
Summary:	KBanking plugin for KMyMoney2
Summary(pl):	Wtyczka KBanking dla KMyMoney2
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description kbanking
KBanking plugin for KMyMoney2.

%description kbanking -l pl
Wtyczka KBanking dla KMyMoney2.

%prep
%setup -q

%build
CONFIG_SHELL="/bin/bash" \
%configure \
	%{?with_kbanking:--enable-kbanking} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

echo "Categories=Qt;KDE;Utility;" >> \
	$RPM_BUILD_ROOT%{_desktopdir}/kde/kmymoney2.desktop

mv $RPM_BUILD_ROOT%{_iconsdir}/{l,L}ocolor
mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libkmm_mymoney.so.*.*.*
%attr(755,root,root) %{_libdir}/libkmm_plugin.so.*.*.*
%{_libdir}/libkmm_mymoney.la
%{_libdir}/libkmm_plugin.la
%attr(755,root,root) %{_libdir}/kde3/kmm_ofximport.so
%{_libdir}/kde3/kmm_ofximport.la
%dir %{_datadir}/apps/kmymoney2
%dir %{_datadir}/apps/kmymoney2/templates
%{_datadir}/apps/kmymoney2/templates/C
%{_datadir}/apps/kmymoney2/templates/README
%{_datadir}/apps/kmymoney2/templates/en_GB
%{_datadir}/apps/kmymoney2/templates/en_US
%lang(de) %{_datadir}/apps/kmymoney2/templates/de_DE
%lang(fr) %{_datadir}/apps/kmymoney2/templates/fr_FR
%lang(gl) %{_datadir}/apps/kmymoney2/templates/gl_ES
%lang(pt_BR) %{_datadir}/apps/kmymoney2/templates/pt_BR
%lang(ru) %{_datadir}/apps/kmymoney2/templates/ru_SU
%dir %{_datadir}/apps/kmymoney2/html
%{_datadir}/apps/kmymoney2/html/home.html
%{_datadir}/apps/kmymoney2/html/whats_new.html
%{_datadir}/apps/kmymoney2/html/*.css
%{_datadir}/apps/kmymoney2/html/images
%lang(pt_BR) %{_datadir}/apps/kmymoney2/html/home_br.pt_BR.html
%lang(de) %{_datadir}/apps/kmymoney2/html/home_de.de.html
%lang(de) %{_datadir}/apps/kmymoney2/html/whats_new_de.html
%lang(fr) %{_datadir}/apps/kmymoney2/html/home_fr.fr.html
%lang(fr) %{_datadir}/apps/kmymoney2/html/whats_new_fr.html
%lang(gl) %{_datadir}/apps/kmymoney2/html/home_gl.html
%lang(gl) %{_datadir}/apps/kmymoney2/html/whats_new_gl.html
%lang(it) %{_datadir}/apps/kmymoney2/html/home_it.html
%lang(it) %{_datadir}/apps/kmymoney2/html/whats_new_it.html
%lang(ru) %{_datadir}/apps/kmymoney2/html/home_ru.ru.html
%{_datadir}/apps/kmymoney2/icons
%{_datadir}/apps/kmymoney2/pics
%{_datadir}/apps/kmymoney2/tips
%{_datadir}/apps/kmymoney2/kmymoney2ui.rc
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/*/*
%{_datadir}/mimelnk/application/x-kmymoney2.desktop
%{_datadir}/services/kmm_ofximport.desktop
%{_datadir}/servicetypes/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkmm_mymoney.so
%attr(755,root,root) %{_libdir}/libkmm_plugin.so
%{_includedir}/kmymoney

%files kbanking
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kmm_kbanking.so
%{_libdir}/kde3/kmm_kbanking.la
%{_datadir}/apps/kmm_kbanking
%{_datadir}/services/kmm_kbanking.desktop
