
%define name	fillets-ng-data
%define version	0.7.1
%define release	1

%define mainname fillets-ng

Summary:	Data files for the Fish Fillets NG game
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
License:	GPL
Group:		Games/Arcade
URL:		http://fillets.sourceforge.net/
# gz smaller than bz2
Source0:	http://prdownloads.sourceforge.net/fillets/%name-%version.tar.gz
Requires:	%{mainname}
Provides:	fillets-ng-data-cs
Obsoletes:	fillets-ng-data-cs
BuildArch:	noarch

%description
Data files for the Fish Fillets NG game.

%prep
%setup -q

%install
rm -rf %{buildroot}

install -m 755 -d %{buildroot}%{_gamesdatadir}/%{mainname}
cp -a font images music script sound %{buildroot}%{_gamesdatadir}/%{mainname}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING doc
%{_gamesdatadir}/%{mainname}

