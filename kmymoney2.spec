#
# TODO: - do something with rest of templates
#	- consider rename to kmymoney
#	- sqlcipher plugin (BR: sqlcipher-devel + qsqlite sources)
#
# Conditional build:
%bcond_without	kbanking	# kbanking support

%define		real_name kmymoney
Summary:	Personal finance application similar to Microsoft Money
Summary(pl.UTF-8):	Program do finansów osobistych, podobny do Microsoft Money
Name:		kmymoney2
Version:	4.8.0
Release:	4
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/kmymoney2/%{real_name}-%{version}.tar.xz
# Source0-md5:	a1cc5f862493f1abc1f660ffed4f1711
URL:		http://kmymoney2.sourceforge.net/
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-man.patch
Patch2:		%{name}-types.patch
Patch3:		0240-Fix-duplicated-symbol-compile-error-on-Windows.patch
%{?with_kbanking:BuildRequires:	aqbanking-devel >= 5.5.1}
BuildRequires:	automoc4
BuildRequires:	boost-devel >= 1.33.1
BuildRequires:	cmake >= 2.8.9
BuildRequires:	doxygen
BuildRequires:	gmp-devel
# included in kde4-kdelibs-devel
#BuildRequires:	gpgme-c++-devel
#BuildRequires:	gpgme-qt4-devel
%{?with_kbanking:BuildRequires:	gwenhywfar-devel >= 4.13.0}
%{?with_kbanking:BuildRequires:	gwenhywfar-gui-cpp-devel >= 4.13.0}
%{?with_kbanking:BuildRequires:	gwenhywfar-gui-qt4-devel >= 4.13.0}
BuildRequires:	kde4-kdelibs-devel >= 4.6.0
BuildRequires:	kde4-kdepimlibs-devel >= 4.6.0
BuildRequires:	libalkimia-devel >= 4.3.2
BuildRequires:	libical-c++-devel
BuildRequires:	libofx-devel >= 0.9.4
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= 4
BuildRequires:	rpmbuild(macros) >= 1.606
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kde4-kdelibs >= 4.6.0
Requires:	kde4-kdepimlibs >= 4.6.0
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
Summary:	kmymoney2 - header files
Summary(pl.UTF-8):	kmymoney2 - pliki nagłówkowe
Summary(pt_BR.UTF-8):	Arquivos de inclusão para compilar aplicativos kmymoney2
Summary(ru.UTF-8):	Хедеры для компилляции программ kmymoney2
Summary(uk.UTF-8):	Хедери для компіляції програм kmymoney2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= 4.6.0

%description devel
This package contains header files for kMyMoney2.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe potrzebne przy pisaniu własnych
programów wykorzystujących kMyMoney2.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos de inclusão que são necessários para
compilar aplicativos kMyMoney2.

%description devel -l ru.UTF-8
Этот пакет содержит хедеры, необходимые для компиляции программ для
kMyMoney2.

%description devel -l uk.UTF-8
Цей пакет містить хедери, необхідні для компіляції програм для
kMyMoney2.

%package kbanking
Summary:	KBanking plugin for KMyMoney2
Summary(pl.UTF-8):	Wtyczka KBanking dla KMyMoney2
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	aqbanking >= 5.5.1
Requires:	gwenhywfar >= 4.13.0
Requires:	gwenhywfar-gui-cpp >= 4.13.0
Requires:	gwenhywfar-gui-qt4 >= 4.13.0

%description kbanking
KBanking plugin for KMyMoney2.

%description kbanking -l pl.UTF-8
Wtyczka KBanking dla KMyMoney2.

%package -n QtDesigner-plugin-kmymoney
Summary:	KMyMoney specific widget library for QtDesigner
Summary(pl.UTF-8):	Biblioteka widgetów KMyMoney dla QtDesignera
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtDesigner >= 4

%description -n QtDesigner-plugin-kmymoney
KMyMoney specific widget library for QtDesigner.

%description -n QtDesigner-plugin-kmymoney -l pl.UTF-8
Biblioteka widgetów KMyMoney dla QtDesignera.

%prep
%setup -q -n kmymoney-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
install -d build
cd build
%cmake .. \
	%{?with_kbanking:-DENABLE_KBANKING=ON} \
	-DUSE_QT_DESIGNER=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_datadir}/apps/appdata \
	$RPM_BUILD_ROOT%{_datadir}

%find_lang %{real_name} --with-kde

# not supported in pld
%{__rm} -r $RPM_BUILD_ROOT%{_iconsdir}/locolor

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{real_name}.lang
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
%attr(755,root,root) %{_libdir}/kde4/kcm_kmm_icalendarexport.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kmm_printcheck.so
%attr(755,root,root) %{_libdir}/kde4/kmm_csvexport.so
%attr(755,root,root) %{_libdir}/kde4/kmm_csvimport.so
%attr(755,root,root) %{_libdir}/kde4/kmm_icalendarexport.so
%attr(755,root,root) %{_libdir}/kde4/kmm_ofximport.so
%attr(755,root,root) %{_libdir}/kde4/kmm_printcheck.so
%attr(755,root,root) %{_libdir}/kde4/kmm_reconciliationreport.so
%attr(755,root,root) %{_libdir}/kde4/kmm_weboob.so
%attr(755,root,root) %{_libdir}/kde4/konlinetasks_national.so
%attr(755,root,root) %{_libdir}/kde4/konlinetasks_sepa.so
%attr(755,root,root) %{_libdir}/kde4/payeeidentifier_iban_bic_delegates.so
%attr(755,root,root) %{_libdir}/kde4/payeeidentifier_ibanbic_storageplugin.so
%attr(755,root,root) %{_libdir}/kde4/payeeidentifier_nationalAccount_ui.so
%attr(755,root,root) %{_libdir}/kde4/payeeidentifier_nationalaccount_storageplugin.so
%dir %{_datadir}/apps/kmymoney
%{_datadir}/apps/kmymoney/icons
%{_datadir}/apps/kmymoney/html
%{_datadir}/apps/kmymoney/ibanbicdata
%{_datadir}/apps/kmymoney/misc
%{_datadir}/apps/kmymoney/pics
%dir %{_datadir}/apps/kmymoney/templates
%{_datadir}/apps/kmymoney/templates/C
%lang(de_AT) %{_datadir}/apps/kmymoney/templates/de_AT
%lang(de_CH) %{_datadir}/apps/kmymoney/templates/de_CH
%lang(de_DE) %{_datadir}/apps/kmymoney/templates/de_DE
%lang(dk) %{_datadir}/apps/kmymoney/templates/dk
%lang(el_GR) %{_datadir}/apps/kmymoney/templates/el_GR
%lang(en_CA) %{_datadir}/apps/kmymoney/templates/en_CA
%lang(en_GB) %{_datadir}/apps/kmymoney/templates/en_GB
%lang(en_US) %{_datadir}/apps/kmymoney/templates/en_US
%lang(es_AR) %{_datadir}/apps/kmymoney/templates/es_AR
%lang(es_ES) %{_datadir}/apps/kmymoney/templates/es_ES
%lang(es_MX) %{_datadir}/apps/kmymoney/templates/es_MX
%lang(fr_CA) %{_datadir}/apps/kmymoney/templates/fr_CA
%lang(fr_CH) %{_datadir}/apps/kmymoney/templates/fr_CH
%lang(fr_FR) %{_datadir}/apps/kmymoney/templates/fr_FR
%lang(gl_ES) %{_datadir}/apps/kmymoney/templates/gl_ES
%lang(hu_HU) %{_datadir}/apps/kmymoney/templates/hu_HU
%lang(it) %{_datadir}/apps/kmymoney/templates/it
%lang(ja) %{_datadir}/apps/kmymoney/templates/jp
%lang(nl_NL) %{_datadir}/apps/kmymoney/templates/nl_NL
%lang(pt_PT) %{_datadir}/apps/kmymoney/templates/pt_PT
%lang(pt_BR) %{_datadir}/apps/kmymoney/templates/pt_BR
%lang(sk) %{_datadir}/apps/kmymoney/templates/sk
%lang(ro_RO) %{_datadir}/apps/kmymoney/templates/ro_RO
%lang(ru_RU) %{_datadir}/apps/kmymoney/templates/ru_RU
%lang(tr_TR) %{_datadir}/apps/kmymoney/templates/tr_TR
%lang(uk_UA) %{_datadir}/apps/kmymoney/templates/uk_UA
%lang(zh_CN) %{_datadir}/apps/kmymoney/templates/zh_CN
%lang(zh_HK) %{_datadir}/apps/kmymoney/templates/zh_HK
%lang(zh_TW) %{_datadir}/apps/kmymoney/templates/zh_TW
%{_datadir}/apps/kmymoney/tips
%{_datadir}/apps/kmymoney/kmymoneyui.rc
%{_datadir}/apps/kconf_update/kmymoney.upd
%{_datadir}/apps/kmm_csvexport
%{_datadir}/apps/kmm_csvimport
%{_datadir}/apps/kmm_icalendarexport
%{_datadir}/apps/kmm_ofximport
%{_datadir}/apps/kmm_printcheck
%{_datadir}/apps/kmm_weboob
%{_datadir}/appdata/kmymoney.appdata.xml
%{_datadir}/config/csvimporterrc
%{_datadir}/config.kcfg/kmymoney.kcfg
%{_datadir}/mime/packages/x-kmymoney.xml
%dir %{_datadir}/kde4/services/ibanbicdata
%{_datadir}/kde4/services/ibanbicdata/germany.desktop
%{_datadir}/kde4/services/kcm_kmm_icalendarexport.desktop
%{_datadir}/kde4/services/kcm_kmm_printcheck.desktop
%{_datadir}/kde4/services/kmm_csvexport.desktop
%{_datadir}/kde4/services/kmm_csvimport.desktop
%{_datadir}/kde4/services/kmm_icalendarexport.desktop
%{_datadir}/kde4/services/kmm_kbanking.desktop
%{_datadir}/kde4/services/kmm_ofximport.desktop
%{_datadir}/kde4/services/kmm_printcheck.desktop
%{_datadir}/kde4/services/kmm_reconciliationreport.desktop
%{_datadir}/kde4/services/kmm_weboob.desktop
%{_datadir}/kde4/services/kmymoney-ibanbic-delegate.desktop
%{_datadir}/kde4/services/kmymoney-ibanbic-storageplugin.desktop
%{_datadir}/kde4/services/kmymoney-nationalaccount-delegate.desktop
%{_datadir}/kde4/services/kmymoney-nationalaccount-storageplugin.desktop
%{_datadir}/kde4/services/kmymoney-nationalorders.desktop
%{_datadir}/kde4/services/kmymoney-nationalordersui.desktop
%{_datadir}/kde4/services/kmymoney-nationalstorageplugin.desktop
%{_datadir}/kde4/services/kmymoney-sepaorders.desktop
%{_datadir}/kde4/services/kmymoney-sepaordersui.desktop
%{_datadir}/kde4/services/kmymoney-sepastorageplugin.desktop
%{_datadir}/kde4/servicetypes/ibanbicdata.desktop
%{_datadir}/kde4/servicetypes/kmymoney-importerplugin.desktop
%{_datadir}/kde4/servicetypes/kmymoney-nationalaccountnumberplugin.desktop
%{_datadir}/kde4/servicetypes/kmymoney-onlinetaskui.desktop
%{_datadir}/kde4/servicetypes/kmymoney-payeeidentifierdelegate.desktop
%{_datadir}/kde4/servicetypes/kmymoney-plugin.desktop
%{_datadir}/kde4/servicetypes/kmymoney-sqlstorageplugin.desktop
%{_desktopdir}/kde4/kmymoney.desktop
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

%files -n QtDesigner-plugin-kmymoney
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt4/plugins/designer/kmymoneywidgets.so
