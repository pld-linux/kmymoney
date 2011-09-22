#
# TODO: - do something with rest of templates
#	- do we really need kmymoney2-devel package?
#
# Conditional build:
%bcond_without	kbanking	# kbanking support
#
%define		real_name kmymoney
Summary:	Personal finance application similar to Microsoft Money
Summary(pl.UTF-8):	Program do finansów osobistych, podobny do Microsoft Money
Name:		kmymoney2
Version:	4.6.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/kmymoney2/%{real_name}-%{version}.tar.bz2
# Source0-md5:	166131b53da426643bd40a0ca6f5c022
URL:		http://kmymoney2.sourceforge.net/
Patch0:		%{name}-desktop.patch
%{?with_kbanking:BuildRequires:	aqbanking-devel >= 5.0.0}
BuildRequires:	automoc4
BuildRequires:	cmake
%{?with_kbanking:BuildRequires:	gwenhywfar-devel >= 4.0.0}
%{?with_kbanking:BuildRequires:	gwenhywfar-qt-devel >= 4.0.0}
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	kde4-kdepimlibs-devel
BuildRequires:	libalkimia-devel
BuildRequires:	libassuan-devel
BuildRequires:	libofx-devel >= 0.9.4
BuildRequires:	pth-devel
BuildRequires:	qt4-build
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	soprano-devel
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

%description kbanking
KBanking plugin for KMyMoney2.

%description kbanking -l pl.UTF-8
Wtyczka KBanking dla KMyMoney2.

%prep
%setup -q -n kmymoney-%{version}
%patch0 -p1

%build

install -d build
cd build
%cmake .. \
	%{?with_kbanking:-DENABLE_KBANKING="on"}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{real_name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{real_name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmymoney
%attr(755,root,root) %{_libdir}/libkmm_kdchart.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_kdchart.so.4
%attr(755,root,root) %{_libdir}/libkmm_mymoney.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_mymoney.so.4
%attr(755,root,root) %{_libdir}/libkmm_plugin.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_plugin.so.4
%attr(755,root,root) %{_libdir}/libkmm_widgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmm_widgets.so.4
%attr(755,root,root) %{_libdir}/kde4/kcm_kmm_icalendarexport.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kmm_printcheck.so
%attr(755,root,root) %{_libdir}/kde4/kmm_icalendarexport.so
%attr(755,root,root) %{_libdir}/kde4/kmm_ofximport.so
%attr(755,root,root) %{_libdir}/kde4/kmm_printcheck.so
%attr(755,root,root) %{_libdir}/kde4/kmm_reconciliationreport.so
%dir %{_datadir}/apps/kmymoney/
%{_datadir}/apps/kmymoney/icons
%{_datadir}/apps/kmymoney/pics
%dir %{_datadir}/apps/kmymoney/templates
%lang(en_GB) %{_datadir}/apps/kmymoney/templates/en_GB
%lang(en_US) %{_datadir}/apps/kmymoney/templates/en_US
%lang(it) %{_datadir}/apps/kmymoney/templates/it
%lang(pt_BR) %{_datadir}/apps/kmymoney/templates/pt_BR
%lang(sk) %{_datadir}/apps/kmymoney/templates/sk
%lang(zh_CN) %{_datadir}/apps/kmymoney/templates/zh_CN
%lang(zh_HK) %{_datadir}/apps/kmymoney/templates/zh_HK
%lang(zh_TW) %{_datadir}/apps/kmymoney/templates/zh_TW
%{_datadir}/apps/kmymoney/tips
%{_datadir}/apps/kmymoney/kmymoneyui.rc
%dir %{_datadir}/apps/kmm_ofximport
%{_datadir}/apps/kmm_ofximport/kmm_ofximport.rc
%dir %{_datadir}/apps/kmm_printcheck
%{_datadir}/apps/kmm_printcheck/kmm_printcheck.rc
%dir %{_iconsdir}/*
%dir %{_iconsdir}/*/*
%dir %{_iconsdir}/*/*/*
%{_iconsdir}/*/*/*/*.png
%{_desktopdir}/kde4/kmymoney.desktop
%{_datadir}/kde4/services/*.desktop
%{_datadir}/kde4/servicetypes/*.desktop
%{_mandir}/man1/kmymoney.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkmm_kdchart.so
%attr(755,root,root) %{_libdir}/libkmm_mymoney.so
%attr(755,root,root) %{_libdir}/libkmm_plugin.so
%attr(755,root,root) %{_libdir}/libkmm_widgets.so
%dir %{_includedir}/kmymoney
%{_includedir}/kmymoney/*.h

%if %{with kbanking}
%files kbanking
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kmm_kbanking.so
%endif
