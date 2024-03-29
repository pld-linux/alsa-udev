Summary:	udev rules and scripts for Advanced Linux Sound Architecture
Summary(pl.UTF-8):	Reguły i skrypty udev dla Advanced Linux Sound Architecture
Name:		alsa-udev
Version:	0.2
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	%{name}.rules
Source1:	%{name}.sh
Source2:	%{name}.conf
Source3:	%{name}.init
URL:		http://www.alsa-project.org/
Requires(post,preun):	/sbin/chkconfig
Requires:	awk
Requires:	udev-core >= 127
Obsoletes:	alsa-init-tools
Obsoletes:	alsa-utils-init
Obsoletes:	alsaconf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
udev rules and scripts for Advanced Linux Sound Architecture.

%description -l pl.UTF-8
Reguły i skrypty udev dla Advanced Linux Sound Architecture.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/udev/rules.d
cp -a %{SOURCE0} $RPM_BUILD_ROOT/etc/udev/rules.d/alsa.rules
install -D %{SOURCE1} $RPM_BUILD_ROOT/lib/udev/alsa-udev
install -D %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/alsa-udev
install -D %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/alsa-udev

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add alsa-udev

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del alsa-udev
fi

%files
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/*
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/alsa-udev
/etc/udev/rules.d/alsa.rules
%attr(754,root,root) /lib/udev/alsa-udev
