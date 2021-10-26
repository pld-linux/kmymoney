#
# TODO: - do something with rest of templates
#	- sqlcipher plugin (BR: sqlcipher-devel + qsqlite sources)
#
# Conditional build:
%bcond_without	kbanking	# kbanking support

Summary:	Personal finance application similar to Microsoft Money
Summary(pl.UTF-8):	Program do finansów osobistych, podobny do Microsoft Money
Name:		kmymoney
Version:	5.1.2
Release:	0.1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
# Source0-md5:	386a53cac09052aba2a343badabe4256
URL:		https://kmymoney.org/
Patch0:		qt-deprecated.patch
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	ka5-akonadi-devel
BuildRequires:	kf5-kactivities-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kdewebkit-devel
BuildRequires:	kf5-kholidays-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kitemmodels-devel
BuildRequires:	kf5-kwallet-devel
%{?with_kbanking:BuildRequires:	aqbanking-devel >= 5.5.1}
BuildRequires:	automoc4
BuildRequires:	boost-devel >= 1.33.1
BuildRequires:	cmake >= 2.8.9
BuildRequires:	doxygen
BuildRequires:	gmp-devel
%{?with_kbanking:BuildRequires:	gwenhywfar-devel >= 4.13.0}
%{?with_kbanking:BuildRequires:	gwenhywfar-gui-cpp-devel >= 4.13.0}
%{?with_kbanking:BuildRequires:	gwenhywfar-gui-qt5-devel >= 4.13.0}
BuildRequires:	libalkimia-devel >= 8.0
BuildRequires:	libical-c++-devel
# These two are not needed, but libical cmake file is broken
BuildRequires:	libical-glib-static
BuildRequires:	libical-static
BuildRequires:	libofx-devel >= 0.9.4
BuildRequires:	pkgconfig
BuildRequires:	python3-devel
BuildRequires:	qt5-build
BuildRequires:	rpmbuild(macros) >= 1.606
BuildRequires:	shared-mime-info
BuildRequires:	sqlcipher-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libalkimia >= 4.3.2
Requires:	libofx >= 0.9.4
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
Requires:	aqbanking >= 5.5.1
Requires:	gwenhywfar >= 4.13.0
Requires:	gwenhywfar-gui-cpp >= 4.13.0
Requires:	gwenhywfar-gui-qt5 >= 4.13.0

%description kbanking
KBanking plugin for KMyMoney.

%description kbanking -l pl.UTF-8
Wtyczka KBanking dla KMyMoney.

%package -n Qt5Designer-plugin-kmymoney
Summary:	KMyMoney specific widget library for QtDesigner
Summary(pl.UTF-8):	Biblioteka widgetów KMyMoney dla QtDesignera
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Designer

%description -n Qt5Designer-plugin-kmymoney
KMyMoney specific widget library for QtDesigner.

%description -n Qt5Designer-plugin-kmymoney -l pl.UTF-8
Biblioteka widgetów KMyMoney dla QtDesignera.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake .. \
	%{?with_kbanking:-DENABLE_KBANKING=ON} \
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
%doc AUTHORS BUGS README.Fileformats TODO
%attr(755,root,root) %{_bindir}/kmymoney
%attr(755,root,root) %{_libdir}/libkmm_kdchart.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_kdchart.so.4
%attr(755,root,root) %{_libdir}/libkmm_mymoney.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_mymoney.so.4
%attr(755,root,root) %{_libdir}/libkmm_plugin.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_plugin.so.4
%attr(755,root,root) %{_libdir}/libkmm_widgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_widgets.so.4
%attr(755,root,root) %{_libdir}/libkmm_payeeidentifier.so
%attr(755,root,root) %{_libdir}/libpayeeidentifier_iban_bic.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpayeeidentifier_iban_bic.so.4
%attr(755,root,root) %{_libdir}/libpayeeidentifier_iban_bic_widgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpayeeidentifier_iban_bic_widgets.so.4
%attr(755,root,root) %{_libdir}/libpayeeidentifier_nationalAccount.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpayeeidentifier_nationalAccount.so.4
%dir %{_datadir}/kmymoney
%{_datadir}/kmymoney/icons
%{_datadir}/kmymoney/html
%{_datadir}/kmymoney/ibanbicdata
%{_datadir}/kmymoney/misc
%{_datadir}/kmymoney/pics
%dir %{_datadir}/kmymoney/templates
%{_datadir}/kmymoney/templates/C
%lang(de_AT) %{_datadir}/kmymoney/templates/de_AT
%lang(de_CH) %{_datadir}/kmymoney/templates/de_CH
%lang(de_DE) %{_datadir}/kmymoney/templates/de_DE
%lang(dk) %{_datadir}/kmymoney/templates/dk
%lang(el_GR) %{_datadir}/kmymoney/templates/el_GR
%lang(en_CA) %{_datadir}/kmymoney/templates/en_CA
%lang(en_GB) %{_datadir}/kmymoney/templates/en_GB
%lang(en_US) %{_datadir}/kmymoney/templates/en_US
%lang(es_AR) %{_datadir}/kmymoney/templates/es_AR
%lang(es_ES) %{_datadir}/kmymoney/templates/es_ES
%lang(es_MX) %{_datadir}/kmymoney/templates/es_MX
%lang(fr_CA) %{_datadir}/kmymoney/templates/fr_CA
%lang(fr_CH) %{_datadir}/kmymoney/templates/fr_CH
%lang(fr_FR) %{_datadir}/kmymoney/templates/fr_FR
%lang(gl_ES) %{_datadir}/kmymoney/templates/gl_ES
%lang(hu_HU) %{_datadir}/kmymoney/templates/hu_HU
%lang(it) %{_datadir}/kmymoney/templates/it
%lang(ja) %{_datadir}/kmymoney/templates/jp
%lang(nl_NL) %{_datadir}/kmymoney/templates/nl_NL
%lang(pt_PT) %{_datadir}/kmymoney/templates/pt_PT
%lang(pt_BR) %{_datadir}/kmymoney/templates/pt_BR
%lang(sk) %{_datadir}/kmymoney/templates/sk
%lang(ro_RO) %{_datadir}/kmymoney/templates/ro_RO
%lang(ru_RU) %{_datadir}/kmymoney/templates/ru_RU
%lang(tr_TR) %{_datadir}/kmymoney/templates/tr_TR
%lang(uk_UA) %{_datadir}/kmymoney/templates/uk_UA
%lang(zh_CN) %{_datadir}/kmymoney/templates/zh_CN
%lang(zh_HK) %{_datadir}/kmymoney/templates/zh_HK
%lang(zh_TW) %{_datadir}/kmymoney/templates/zh_TW
%{_datadir}/kmymoney/tips
%{_datadir}/kmymoney/kmymoneyui.rc
%{_datadir}/kconf_update/kmymoney.upd
%{_datadir}/kmm_csvexport
%{_datadir}/kmm_csvimport
%{_datadir}/kmm_icalendarexport
%{_datadir}/kmm_ofximport
%{_datadir}/kmm_printcheck
%{_datadir}/kmm_weboob
%{_datadir}/appdata/kmymoney.appdata.xml
%{_datadir}/config/csvimporterrc
%{_datadir}/config.kcfg/kmymoney.kcfg
%{_datadir}/mime/packages/x-kmymoney.xml
%{_iconsdir}/hicolor/*x*/apps/kmymoney.png
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-kmymoney.png
%{_mandir}/man1/kmymoney.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkmm_kdchart.so
%attr(755,root,root) %{_libdir}/libkmm_mymoney.so
%attr(755,root,root) %{_libdir}/libkmm_plugin.so
%attr(755,root,root) %{_libdir}/libkmm_widgets.so
%attr(755,root,root) %{_libdir}/libpayeeidentifier_iban_bic.so
%attr(755,root,root) %{_libdir}/libpayeeidentifier_iban_bic_widgets.so
%attr(755,root,root) %{_libdir}/libpayeeidentifier_nationalAccount.so
%{_includedir}/kmymoney

%if %{with kbanking}
%files kbanking
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kmm_kbanking.so
%{_datadir}/apps/kmm_kbanking
%{_datadir}/config.kcfg/kbanking.kcfg
%endif

%files -n Qt5Designer-plugin-kmymoney
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt4/plugins/designer/kmymoneywidgets.so
