Summary: Implementation of ubctl
Name: ubctl
Version: 1.0.3
Release: 5%{?dist}
License: MIT
%global major_version 1
URL: https://gitee.com/openeuler/ubctl
Source0: %{name}-%{version}.tar.gz

Patch1: 0001-ub-ubctl-Modify-the-incorrect-printing-of-register-n.patch
Patch2: 0002-ub-ubctl-Supports-query-commands-and-can-retrieve-st.patch
Patch3: 0003-ub-ubctl-Support-querying-statistical-indicators-at-.patch
Patch4: 0004-ub-ubctl-Support-querying-real-time-bandwidth-statis.patch
Patch5: 0005-ub-ubctl-Support-querying-firmware-version-numbers.patch
Patch6: 0006-ub-ubctl-Support-querying-the-historical-status-of-p.patch
Patch7: 0007-ub-ubctl-Incorporate-minor-optimizations-for-various.patch
Patch8: 0008-ub-ubctl-Modify-the-statistical-port-link-up-down-to.patch
Patch9: 0009-ub-ubctl-modify-the-parsing-policy-for-the-speed_abi.patch
Patch10: 0010-ub-ubctl-Supports-the-configuration-and-query-of-pac.patch
Patch11: 0011-ub-ubctl-add-querying-the-peak-bandwidth.patch
Patch12: 0012-ub-ubctl-Add-the-debugfs-function.patch
Patch13: 0013-ub-ubctl-Modify-debugfs-verification-matching-rules.patch
Patch14: 0014-ub-ubctl-Modify-TA-layer-to-obtain-WQE-delay-related.patch
Patch15: 0015-ub-ubctl-Add-print-fields-to-the-queried-port-inform.patch
Patch16: 0016-ub-ubctl-Change-the-time-printing-from-UTC-time-to-u.patch
Patch17: 0017-ub-ubctl-Add-librt-link-dependency.patch
Patch18: 0018-ub-ubctl-Extract-folders-and-modify-file-locations.patch
Patch19: 0019-ub-ubctl-Support-users-to-use-query-function-in-non-.patch
Patch20: 0020-ub-ubctl-Support-libubctl.so-to-user.patch
Patch21: 0021-ub-ubctl-Enhance-the-query-information-of-ubctl.patch
Patch22: 0022-ub-ubctl-Support-SDC-fault-detection-for-switching-c.patch
Patch23: 0023-ub-ubctl-Provide-a-user-interface-for-ubase-query-fu.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-podlators
ExclusiveArch:  aarch64

BuildRoot:      %{name}-%{version}-%{release}

%description
This implementation provides ubctl sending and reception.

%package devel
Summary:  Implementation of ubctl(UB) - Tools and header files for developers
Group:    Development/Libraries/C
BuildRequires: pkgconfig
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package is required to develop alternate clients for ubctl.

The ubctl tool implements UB-related DFX functions by invoking the 
ub_fwctl deriver.
This tool is mainly used to parse the command line input by the user and 
send query commands to the kernel state. After the kernel state returns 
the query results, it parses and prints the expected results.

%prep
%autosetup -p1 -n %{name}-%{version}

# %build
# mkdir ubctl/build
# cd ubctl/build
# cmake ../src
# make

%build
rm -rf build
cmake -S . -B build \
      -DCMAKE_INSTALL_PREFIX=/usr \
      -DCMAKE_INSTALL_LIBDIR=lib64 \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo \
      -DCMAKE_C_FLAGS="%{optflags}" \
      -DCMAKE_CXX_FLAGS="%{optflags}" \
      -DPROJECT_VERSION=%{version} \
      -DLIB_SOVERSION=%{major_version}

cmake --build build -- -j$(nproc)

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}
mkdir -p %{buildroot}%{_docdir}/ub/%{name}/
mkdir -p %{buildroot}%{_mandir}/man8/
pod2man doc/ubctl.pod ./ubctl.8
install -m 644 README.md %{buildroot}%{_docdir}/ub/%{name}/
install -m 644 ./ubctl.8 %{buildroot}%{_mandir}/man8/ubctl.8
gzip -f9n %{buildroot}%{_mandir}/man8/ubctl.8

cmake --install build --prefix=%{buildroot}/usr

%files
%{_bindir}/ubctl
%{_libdir}/libubctl.so.*
%doc %{_docdir}/ub/%{name}/*
%{_mandir}/man8/ubctl.8.gz

%files devel
%{_libdir}/libubctl.so
%{_includedir}/u_utool_user_api.h

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Nov 13 2026 zhao-lichang <zhaolichang@huawei.com> - 1.0.3-5
- [Type] sync
- [DESC] update to 0930
* Wed Jul 15 2026 qiushengming <846759657@qq.com> - 1.0.3-3
- [Type] sync
- [DESC] Package init.
