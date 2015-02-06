%define	version	0.1
%define release	8

Summary:	Shared data files and scripts for Logitech mice
Name:		logitech-mouse-common
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Configuration/Hardware		
Source0:	logitechmouse-sysconfig.bz2
Source1:	logitech-mouse.rules.bz2
Source2:	logitech-mouse-udev.sh.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	lmctl

%description
This package contains scripts that turn on/off some certain feature
of recent Logitech USB mouse automatically when device is plugged
into system.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
bzip2 -dc %{SOURCE0} > $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/logitechmouse
chmod 0644 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/logitechmouse

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d
bzip2 -dc %{SOURCE1} > $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/80-logitech-mouse.rules
chmod 0644 $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/80-logitech-mouse.rules

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/udev/scripts
bzip2 -dc %{SOURCE2} > $RPM_BUILD_ROOT%{_sysconfdir}/udev/scripts/logitech-mouse.sh
chmod 0755 $RPM_BUILD_ROOT%{_sysconfdir}/udev/scripts/logitech-mouse.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/sysconfig/logitechmouse
%config(noreplace) %{_sysconfdir}/udev/rules.d/*.rules
%{_sysconfdir}/udev/scripts/*.sh

