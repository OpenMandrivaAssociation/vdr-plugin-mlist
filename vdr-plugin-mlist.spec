%define plugin	mlist

Summary:	VDR plugin: Displays the message history
Name:		vdr-plugin-%plugin
Version:	1.0.1
Release:	5
Group:		Video
License:	GPL+
URL:		http://joachim-wilke.de/vdr-mlist.htm
Source:		vdr-%plugin-%{version}.tgz
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin displays a list of all shown OSD-Messages since VDR
startup.

%prep
%setup -q -n %plugin-%{version}
chmod 0644 README HISTORY
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%doc README HISTORY


