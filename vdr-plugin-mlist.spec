
%define plugin	mlist
%define name	vdr-plugin-%plugin
%define version	1.0.1
%define rel	3

Summary:	VDR plugin: Displays the message history
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL+
URL:		http://joachim-wilke.de/vdr-mlist.htm
Source:		vdr-%plugin-%version.tgz
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin displays a list of all shown OSD-Messages since VDR
startup.

%prep
%setup -q -n %plugin-%version
chmod 0644 README HISTORY
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 1.0.1-2mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Wed Jul 15 2009 Anssi Hannula <anssi@mandriva.org> 1.0.1-1mdv2010.0
+ Revision: 396130
- new version

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.5-3mdv2009.1
+ Revision: 359337
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.5-2mdv2009.0
+ Revision: 197949
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.5-1mdv2009.0
+ Revision: 197691
- new version
- add vdr_plugin_prep
- bump buildrequires on vdr-devel

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.4-3mdv2008.1
+ Revision: 145128
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4-2mdv2008.1
+ Revision: 103152
- rebuild for new vdr

* Fri Sep 07 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4-1mdv2008.0
+ Revision: 81871
- 0.0.4
- adapt license tag for new policy

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-10mdv2008.0
+ Revision: 50017
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-9mdv2008.0
+ Revision: 42103
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-8mdv2008.0
+ Revision: 22753
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-7mdv2007.0
+ Revision: 90941
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-6mdv2007.1
+ Revision: 74047
- rebuild for new vdr
- Import vdr-plugin-mlist

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-2mdv2007.0
- rebuild for new vdr

* Sat Jul 15 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-1mdv2007.0
- initial Mandriva release

