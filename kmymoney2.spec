Summary:	Personal finance application similar to Microsoft Money
Summary(pl):	Program do finans�w osobistych, podobny do Microsoft Money
Name:		kmymoney2
Version:	0.8
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kmymoney2/%{name}-%{version}.tar.bz2
# Source0-md5:	a944bcfb7556d20e79d6e8cfc1e30333
Patch0:		%{name}-includehints.patch
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
KMyMoney stara si� by� w pe�ni funkcjonalnym zamiennikiem dla
windowsowych program�w finansowych. Jest to oprogramowanie o podw�jnej
roli, do u�ytku osobistego i dla ma�ych firm.

%package devel
Summary:	kmymoney2 - header files and development documentation
Summary(pl):	kmymoney2 - pliki nag��wkowe i dokumentacja do kdelibs
Summary(pt_BR):	Arquivos de inclus�o e documenta��o para compilar aplicativos kmymoney2
Summary(ru):	������ � ������������ ��� ����������� �������� kmymoney2
Summary(uk):	������ �� ���������æ� ��� ���Ц��æ� ������� kmymoney2
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This package contains header files and development documentation for
kMyMoney2.

%description devel -l pl
Pakiet ten zawiera pliki nag��wkowe i dokumentacj� potrzebn� przy
pisaniu w�asnych program�w wykorzystuj�cych kMyMoney2.

%description devel -l pt_BR
Este pacote cont�m os arquivos de inclus�o que s�o necess�rios para
compilar aplicativos kMyMoney2.

%description devel -l ru
���� ����� �������� ������, ����������� ��� ���������� �������� ���
kMyMoney2.

%description devel -l uk
��� ����� ͦ����� ������, ����Ȧ�Φ ��� ���Ц��æ� ������� ���
kMyMoney2


%prep
%setup -q
%patch -p1

%build
CONFIG_SHELL="/bin/bash" \
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

echo "Categories=Qt;KDE;Utility;" >> \
	$RPM_BUILD_ROOT%{_desktopdir}/kde/kmymoney2.desktop

mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/apps/kmymoney2
%dir %{_datadir}/apps/kmymoney2/templates
%dir %{_datadir}/apps/kmymoney2/templates/C
%{_datadir}/apps/kmymoney2/templates/C/*
%{_datadir}/apps/kmymoney2/templates/README
%{_datadir}/apps/kmymoney2/templates/en_GB/*
%{_datadir}/apps/kmymoney2/templates/en_US/*
%lang(de) %{_datadir}/apps/kmymoney2/templates/de_DE/*
%lang(fr) %{_datadir}/apps/kmymoney2/templates/fr_FR/*
%lang(gl) %{_datadir}/apps/kmymoney2/templates/gl_ES/*
%lang(pt_BR) %{_datadir}/apps/kmymoney2/templates/pt_BR/*
%lang(ru) %{_datadir}/apps/kmymoney2/templates/ru_SU/*
%dir %{_datadir}/apps/kmymoney2/html
%{_datadir}/apps/kmymoney2/html/home.html
%{_datadir}/apps/kmymoney2/html/whats_new.html
%{_datadir}/apps/kmymoney2/html/*.css
%{_datadir}/apps/kmymoney2/html/images
%lang(br) %{_datadir}/apps/kmymoney2/html/home_br.pt_BR.html
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
%{_desktopdir}/*
%{_iconsdir}/*/*/*/*
%{_datadir}/mimelnk/application/x-kmymoney2.desktop
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_mandir}/man1/*
%attr(755,root,root) %{_libdir}/libkmm_mymoney.so.*
%attr(755,root,root) %{_libdir}/libkmm_mymoney.so.*.*.*
%attr(755,root,root) %{_libdir}/libkmm_plugin.so.*.*.*
%attr(755,root,root) %{_libdir}/libkmm_plugin.so.*
%attr(755,root,root) %{_libdir}/kde3/kmm_ofximport.so
%{_libdir}/kde3/kmm_ofximport.la
%{_libdir}/libkmm_mymoney.la
%{_libdir}/libkmm_plugin.la

%files devel
%defattr(644,root,root,755)
%{_includedir}/kmymoney
%attr(755,root,root) %{_libdir}/libkmm_mymoney.so
%attr(755,root,root) %{_libdir}/libkmm_plugin.so
