
%define plugin	mlist
%define name	vdr-plugin-%plugin
%define version	0.0.4
%define rel	3

Summary:	VDR plugin: Displays the message history
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL+
URL:		http://joachim-wilke.de/vdr-mlist.htm
Source:		vdr-%plugin-%version.tgz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
This plugin displays a list of all shown OSD-Messages since VDR
startup.

%prep
%setup -q -n %plugin-%version
chmod 0644 README HISTORY

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


