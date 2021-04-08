%define name rtl8812au
%define version 5.6.4.2
%define release 1
%define target_kern_ver 5.4.64-altera

Summary: RTL8812AU/21AU Wireless drivers
Name: %{name}
Version: %{version}
Release: %{release}
Group: System Environment/Kernel
License: GPL 2.0
Packager: Kohei Nagasu <kohei@lcarsnet.pgw.jp>
Vendor: aircrack-ng

%undefine _disable_source_fetch
Source0: https://github.com/aircrack-ng/rtl8812au/archive/refs/heads/v%{version}.tar.gz
Patch0: cv_platform-rtl8812au.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: kernel-image-zimage = 5.4.64+lts+git0+1f2f1ded05-r0
BuildRequires: kernel-devsrc = 1.0 make patch
BuildArch: cyclone5

%description
RTL8812AU/21AU Wireless drivers

%prep
rm -rf ${RPM_BUILD_ROOT}

%setup -n %{name}-%{version}
%patch0 -p1

%build
make

%install
install -p -m 644 -D -t ${RPM_BUILD_ROOT}/lib/modules/%{target_kern_ver}/extramodules 88XXau.ko

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
# This routine is executed at first installation
if [ "${1}" = '1' ]
then
	depmod -a %{target_kern_ver}
fi

%preun
modprobe -r 88XXau

%postun
depmod -a %{target_kern_ver}

# This routine is executed at update
if [ "${1}" = '1' ]
then
	modprobe 88XXau
fi

%files
%defattr(-, root, root)
/lib/modules/%{target_kern_ver}/extramodules/88XXau.ko

%changelog
* Thu Apr 08 2021 Kohei Nagasu <kohei@lcarsnet.pgw.jp> %{version}
- Initial release

