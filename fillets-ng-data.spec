%define name fillets-ng-data
%define version 1.0.0
%define release 2

%define mainname fillets-ng

Summary: Data files for the Fish Fillets NG game
Name: %{name}
Version:	1.0.1
Release:	1
License: GPLv2+
Group: Games/Puzzles
URL: https://fillets.sourceforge.net/
# gz smaller than bz2
Source0: http://downloads.sourceforge.net/fillets/%name-%version.tar.gz
Requires: %{mainname}
Provides: fillets-ng-data-cs
Obsoletes: fillets-ng-data-cs
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildArch: noarch

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


%changelog
* Wed Jan 05 2011 Tomas Kindl <supp@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 628824
- update to 1.0.0

* Tue Dec 29 2009 Tomas Kindl <supp@mandriva.org> 0.9.2-2mdv2011.0
+ Revision: 483204
- rebuild

* Sun Oct 18 2009 Samuel Verschelde <stormi@mandriva.org> 0.9.2-1mdv2010.1
+ Revision: 458111
- update to new version 0.9.2

* Sun Sep 20 2009 Funda Wang <fwang@mandriva.org> 0.9.0-2mdv2010.0
+ Revision: 444912
- reupload

* Sat Jul 18 2009 Frederik Himpe <fhimpe@mandriva.org> 0.9.0-1mdv2010.0
+ Revision: 397216
- Update to new version 0.9.0

* Wed May 13 2009 Samuel Verschelde <stormi@mandriva.org> 0.8.1-2mdv2010.0
+ Revision: 375245
- fix Group
- fix Licence

* Sun Mar 15 2009 Funda Wang <fwang@mandriva.org> 0.8.1-1mdv2009.1
+ Revision: 355309
- New version 0.8.1

* Wed Mar 05 2008 Guillaume Bedot <littletux@mandriva.org> 0.8.0-1mdv2008.1
+ Revision: 179686
- 0.8.0

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1mdv2008.1-current
+ Revision: 136415
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Dec 02 2006 Olivier Blin <oblin@mandriva.com> 0.7.1-1mdv2007.0
+ Revision: 89927
- Import fillets-ng-data

* Fri Dec 23 2005 Anssi Hannula <anssi@mandriva.org> 0.7.1-1mdk
- 0.7.1
- split from fillets-ng.spec

