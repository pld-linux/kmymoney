#
# TODO: - do something with rest of templates
#
# Conditional build:
%bcond_without	kbanking	# kbanking support
#
%define		real_name kmymoney
Summary:	Personal finance application similar to Microsoft Money
Summary(pl.UTF-8):	Program do finansów osobistych, podobny do Microsoft Money
Name:		kmymoney2
Version:	4.5
Release:	0.1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/kmymoney2/%{version}/%{real_name}-%{version}.tar.bz2
# Source0-md5:	a764fe259c7885f22a10049cef68398e
URL:		http://kmymoney2.sourceforge.net/
Patch0:		%{name}-desktop.patch
#%%{?with_kbanking:BuildRequires:	aqbanking-frontend-kbanking-devel >= 0.1.0.0}
#BuildRequires:	arts-qt-devel
#BuildRequires:	artsc-devel
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	kde4-kdepimlibs-devel
BuildRequires:	libassuan-devel
BuildRequires:	libofx-devel
#BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	pth-devel
BuildRequires:	rpmbuild(macros) >= 1.577
BuildRequires:	soprano-devel
#BuildRequires:	xrender-devel
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
#CONFIG_SHELL="/bin/bash" \
#%%configure \
#%	%{?with_kbanking:--enable-kbanking} \
#%	--with-qt-libraries=%{_libdir}

install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

#%%{__make} install \
#	DESTDIR=$RPM_BUILD_ROOT \
#	kde_htmldir=%{_kdedocdir}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

#mv $RPM_BUILD_ROOT%{_iconsdir}/{l,L}ocolor
#mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}

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
%attr(755,root,root) %{_libdir}/kde4/kcm_kmm_printcheck.so
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

%files kbanking
%defattr(644,root,root,755)
#%%attr(755,root,root) %{_libdir}/kde3/kmm_kbanking.so
#%%{_libdir}/kde3/kmm_kbanking.la
#%%{_datadir}/apps/kmm_kbanking
#%%{_datadir}/services/kmm_kbanking.desktop
