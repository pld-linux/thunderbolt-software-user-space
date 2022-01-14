Summary:	User-space components for handling Thunderbolt controller and devices
Summary(pl.UTF-8):	Komponenty przestrzeni użytkownika do obsługi kontrolerów i urządzeń Thunderbolt
Name:		thunderbolt-software-user-space
Version:	0.9.3
Release:	6
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/01org/thunderbolt-software-user-space/releases
Source0:	https://github.com/01org/thunderbolt-software-user-space/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	45047cb57cc7c70d2db473628bf29c12
URL:		https://01.org/thunderbolt-sw/
BuildRequires:	boost-devel
BuildRequires:	cmake >= 3.5
# C++14
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	pkgconfig
BuildRequires:	txt2tags
BuildRequires:	udev-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Thunderbolt(TM) technology is a transformational high-speed, dual
protocol I/O that provides unmatched performance with up to 40Gbps
bi-directional transfer speeds. It provides flexibility and simplicity
by supporting both data (PCIe, USB3.1) and video (DisplayPort) on a
single cable connection that can daisy-chain up to six devices.

This package includes the user-space components for device approval
support:
- Easier interaction with the kernel module for approving connected
  devices.
- ACL for auto-approving devices white-listed by the user.

%description -l pl.UTF-8
Technologia Thunderbolt(TM) to bardzo szybkie, używające dwóch
protokołów wejście/wyjście, zapewniające wydajność przesyłu danych do
40Gb/s w obie strony. Zapewnia elastyczność i prostotę, obsługując
zarówno dane (PCIe, USB3.1), jak i obraz (DisplayPort) na połączeniu
pojedynczym kablem, pozwalającym na połączenie szeregowe do sześciu
urządzeń.

Ten pakiet zawiera komponenty przestrzeni użytkownika do zatwierdzania
urządzeń:
- łatwej interakcji z modułem jądra do zatwierdzania podłączonych
  urządzeń,
- ACL do automatycznego zatwierdzania urządzeń zaakceptowanych przez
  użytkownika.

%package -n bash-completion-tbtadm
Summary:	Bash completion for Thunderbolt tbtadm command
Summary(pl.UTF-8):	Bashowe uzupełnianie parametrów polecenia tbtadm do sprzętu Thunderbolt
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-tbtadm
Bash completion for Thunderbolt tbtadm command.

%description -n bash-completion-tbtadm -l pl.UTF-8
Bashowe uzupełnianie parametrów polecenia tbtadm do sprzętu
Thunderbolt.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/lib/thunderbolt/acl

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc COPYING
%{__rm} $RPM_BUILD_ROOT%{_docdir}/thunderbolt-user-space/copyright

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING Description MAINTAINERS README.md
# udev service
%attr(755,root,root) /lib/udev/tbtacl
%attr(755,root,root) /lib/udev/tbtacl-write
%attr(755,root,root) /lib/udev/tbtxdomain
/lib/udev/rules.d/60-tbtacl.rules
/lib/udev/rules.d/60-tbtxdomain.rules
%dir /var/lib/thunderbolt
%dir /var/lib/thunderbolt/acl
# CLI utility (controls kernel module and udev service)
%attr(755,root,root) %{_bindir}/tbtadm
%{_mandir}/man1/tbtadm.1*

%files -n bash-completion-tbtadm
%defattr(644,root,root,755)
%{bash_compdir}/tbtadm
