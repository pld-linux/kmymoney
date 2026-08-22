#
# Conditional build:
%bcond_without	kbanking	# kbanking support

Summary:	Personal finance application similar to Microsoft Money
Summary(pl.UTF-8):	Program do finansów osobistych, podobny do Microsoft Money
Name:		kmymoney
Version:	5.2.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/kmymoney/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	9db9ace053c7d86ac0b5450130bd4962
URL:		https://kmymoney.org/
Patch1:		install.patch
Patch2:		cxx17.patch
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel >= 5.15.2
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Keychain-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
%{?with_kbanking:BuildRequires:	aqbanking-devel >= 6.8.4}
BuildRequires:	cmake >= 3.16
BuildRequires:	doxygen
BuildRequires:	gpgmepp-devel
%{?with_kbanking:BuildRequires:	gwenhywfar-devel >= 5.14.1}
%{?with_kbanking:BuildRequires:	gwenhywfar-gui-cpp-devel >= 5.14.1}
%{?with_kbanking:BuildRequires:	gwenhywfar-gui-qt5-devel >= 5.14.1}
BuildRequires:	ka5-akonadi-devel
BuildRequires:	ka5-kidentitymanagement-devel
BuildRequires:	ka5-kpimtextedit-devel
BuildRequires:	kdiagram-qt5-devel >= 2.6.0
BuildRequires:	kf5-extra-cmake-modules >= 5.90
BuildRequires:	kf5-kactivities-devel
BuildRequires:	kf5-karchive-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcontacts-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kholidays-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kitemmodels-devel
BuildRequires:	kf5-kitemviews-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	libalkimia-devel >= 8.2.1
BuildRequires:	libical-c++-devel
# These are not needed, but libical cmake file is broken
BuildRequires:	libical-c++-static
BuildRequires:	libical-glib-static
BuildRequires:	libical-static
BuildRequires:	libofx-devel >= 0.10.0
BuildRequires:	pkgconfig
BuildRequires:	python3-devel
BuildRequires:	qgpgme-qt5-devel
BuildRequires:	qt5-build
BuildRequires:	rpmbuild(macros) >= 1.606
BuildRequires:	shared-mime-info
BuildRequires:	sqlcipher-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libalkimia >= 8.2.1
Obsoletes:	kmymoney2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMyMoney is striving to be a full-featured replacement for your
Windows-based finance software. We are a full double-entry accounting
software package, for personal or small-business use.

%description -l pl.UTF-8
KMyMoney stara się być w pełni funkcjonalnym zamiennikiem dla
windowsowych programów finansowych. Jest to kompletny system
podwójnego księgowania przeznaczony do użytku osobistego i dla małych
firm.

%package devel
Summary:	kmymoney - header files
Summary(pl.UTF-8):	kmymoney - pliki nagłówkowe
Summary(pt_BR.UTF-8):	Arquivos de inclusão para compilar aplicativos kmymoney
Summary(ru.UTF-8):	Хедеры для компилляции программ kmymoney
Summary(uk.UTF-8):	Хедери для компіляції програм kmymoney
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kmymoney2-devel

%description devel
This package contains header files for kMyMoney.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe potrzebne przy pisaniu własnych
programów wykorzystujących kMyMoney.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos de inclusão que são necessários para
compilar aplicativos kMyMoney.

%description devel -l ru.UTF-8
Этот пакет содержит хедеры, необходимые для компиляции программ для
kMyMoney.

%description devel -l uk.UTF-8
Цей пакет містить хедери, необхідні для компіляції програм для
kMyMoney.

%package kbanking
Summary:	KBanking plugin for KMyMoney
Summary(pl.UTF-8):	Wtyczka KBanking dla KMyMoney
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	aqbanking >= 6.8.4
Requires:	gwenhywfar >= 5.14.1
Requires:	gwenhywfar-gui-cpp >= 5.14.1
Requires:	gwenhywfar-gui-qt5 >= 5.14.1
Obsoletes:	kmymoney2-kbanking

%description kbanking
KBanking plugin for KMyMoney.

%description kbanking -l pl.UTF-8
Wtyczka KBanking dla KMyMoney.

%prep
%setup -q
%patch -P 1 -p1
%patch -P 2 -p1

%build
install -d build
cd build
%cmake .. \
	-DBUILD_WITH_QT6=OFF \
	-DKDE_INSTALL_PLUGINDIR=%{_libdir}/qt5/plugins \
	-DKDE_INSTALL_DOCBUNDLEDIR:PATH=%{_defaultdocdir}/kde/HTML \
	-DENABLE_ADDRESSBOOK=ON \
	-DENABLE_GPG=ON \
	-DENABLE_KBANKING=%{?with_kbanking:ON}%{!?with_kbanking:OFF} \
	-DENABLE_REPORTSVIEW=ON \
	-DUSE_QT_DESIGNER=OFF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/kmymoney
%attr(755,root,root) %{_libdir}/libkmm_base_dialogs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_base_dialogs.so.5
%attr(755,root,root) %{_libdir}/libkmm_base_widgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_base_widgets.so.5
%attr(755,root,root) %{_libdir}/libkmm_codec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_codec.so.5
%attr(755,root,root) %{_libdir}/libkmm_csvimportercore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_csvimportercore.so.5
%attr(755,root,root) %{_libdir}/libkmm_extended_dialogs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_extended_dialogs.so.5
%attr(755,root,root) %{_libdir}/libkmm_gpgfile.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_gpgfile.so.5
%attr(755,root,root) %{_libdir}/libkmm_icons.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_icons.so.5
%attr(755,root,root) %{_libdir}/libkmm_keychain.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_keychain.so.5
%attr(755,root,root) %{_libdir}/libkmm_menuactionexchanger.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_menuactionexchanger.so.5
%attr(755,root,root) %{_libdir}/libkmm_menus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_menus.so.5
%attr(755,root,root) %{_libdir}/libkmm_models.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_models.so.5
%attr(755,root,root) %{_libdir}/libkmm_mymoney.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_mymoney.so.5
%attr(755,root,root) %{_libdir}/libkmm_payeeidentifier.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_payeeidentifier.so.5
%attr(755,root,root) %{_libdir}/libkmm_plugin.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_plugin.so.5
%attr(755,root,root) %{_libdir}/libkmm_printer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_printer.so.5
%attr(755,root,root) %{_libdir}/libkmm_selections.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_selections.so.5
%attr(755,root,root) %{_libdir}/libkmm_settings.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_settings.so.5
%attr(755,root,root) %{_libdir}/libkmm_templates.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_templates.so.5
%attr(755,root,root) %{_libdir}/libkmm_webconnect.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_webconnect.so.5
%attr(755,root,root) %{_libdir}/libkmm_widgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_widgets.so.5
%attr(755,root,root) %{_libdir}/libkmm_wizard.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_wizard.so.5
%attr(755,root,root) %{_libdir}/libkmm_yesno.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_yesno.so.5
%attr(755,root,root) %{_libdir}/libonlinetask_interfaces.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libonlinetask_interfaces.so.5
%dir %{_libdir}/qt5/plugins/kmymoney_plugins
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/budgetview.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/checkprinting.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/csvexporter.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/csvimporter.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/forecastview.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/gncimporter.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/icalendarexporter.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/konlinetasks_sepa.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/ofximporter.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/onlinejoboutboxview.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/qifexporter.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/qifimporter.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/reconciliationreport.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/reportsview.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/sqlstorage.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/woob.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/xmlstorage.so
%dir %{_libdir}/qt5/plugins/kmymoney_plugins/kcms
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/kcms/kcm_checkprinting.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/kcms/kcm_csvimporter.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/kcms/kcm_forecastview.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/kcms/kcm_icalendarexporter.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/kcms/kcm_qif.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/kcms/kcm_reportsview.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/kcms/kcm_xmlstorage.so
%attr(755,root,root) %{_libdir}/qt5/plugins/sqldrivers/qsqlcipher.so
%{_datadir}/config.kcfg/kmymoney.kcfg
%{_datadir}/kconf_update/kmymoney.upd
%dir %{_datadir}/kmymoney
%{_datadir}/kmymoney/checkprinting
%{_datadir}/metainfo/org.kde.kmymoney.appdata.xml
%{_datadir}/mime/packages/x-kmymoney.xml
%{_iconsdir}/hicolor/*x*/apps/kmymoney.png
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-kmymoney.png
%{_desktopdir}/org.kde.kmymoney.desktop
%{_mandir}/man1/kmymoney.1*
%lang(ca) %{_mandir}/ca/man1/kmymoney.1*
%lang(de) %{_mandir}/de/man1/kmymoney.1*
%lang(it) %{_mandir}/it/man1/kmymoney.1*
%lang(nl) %{_mandir}/nl/man1/kmymoney.1*
%lang(pt) %{_mandir}/pt/man1/kmymoney.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kmymoney.1*
%lang(ru) %{_mandir}/ru/man1/kmymoney.1*
%lang(sv) %{_mandir}/sv/man1/kmymoney.1*
%lang(uk) %{_mandir}/uk/man1/kmymoney.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkmm_base_dialogs.so
%attr(755,root,root) %{_libdir}/libkmm_base_widgets.so
%attr(755,root,root) %{_libdir}/libkmm_codec.so
%attr(755,root,root) %{_libdir}/libkmm_csvimportercore.so
%attr(755,root,root) %{_libdir}/libkmm_extended_dialogs.so
%attr(755,root,root) %{_libdir}/libkmm_gpgfile.so
%attr(755,root,root) %{_libdir}/libkmm_icons.so
%attr(755,root,root) %{_libdir}/libkmm_keychain.so
%attr(755,root,root) %{_libdir}/libkmm_menuactionexchanger.so
%attr(755,root,root) %{_libdir}/libkmm_menus.so
%attr(755,root,root) %{_libdir}/libkmm_models.so
%attr(755,root,root) %{_libdir}/libkmm_mymoney.so
%attr(755,root,root) %{_libdir}/libkmm_payeeidentifier.so
%attr(755,root,root) %{_libdir}/libkmm_plugin.so
%attr(755,root,root) %{_libdir}/libkmm_printer.so
%attr(755,root,root) %{_libdir}/libkmm_selections.so
%attr(755,root,root) %{_libdir}/libkmm_settings.so
%attr(755,root,root) %{_libdir}/libkmm_templates.so
%attr(755,root,root) %{_libdir}/libkmm_webconnect.so
%attr(755,root,root) %{_libdir}/libkmm_widgets.so
%attr(755,root,root) %{_libdir}/libkmm_wizard.so
%attr(755,root,root) %{_libdir}/libkmm_yesno.so
%attr(755,root,root) %{_libdir}/libonlinetask_interfaces.so
%{_includedir}/kmymoney

%if %{with kbanking}
%files kbanking
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/kmymoney_plugins/kbanking.so
%{_datadir}/config.kcfg/kbanking.kcfg
%endif
