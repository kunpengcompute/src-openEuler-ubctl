Summary: Implementation of ubctl
Name: ubctl
Version: 1.0.3
Release: 4
License: MIT
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

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
ExclusiveArch:  aarch64

BuildRoot:      %{name}-%{version}-%{release}

%description
This implementation provides ubctl sending and reception.

%package devel
Summary:  Implementation of ubctl(UB) - Tools and header files for developers
Group:    Development/Libraries/C
BuildRequires: pkgconfig
Requires: libubctl = %{version}-%{release}

%description devel
This package is required to develop alternate clients for ubctl.

The ubctl tool implements UB-related DFX functions by invoking the 
ub_fwctl deriver.
This tool is mainly used to parse the command line input by the user and 
send query commands to the kernel state. After the kernel state returns 
the query results, it parses and prints the expected results.

%prep
%setup -q -n %{name}-%{version}
%autopatch -p1

# %build
# mkdir ubctl/build
# cd ubctl/build
# cmake ../src
# make

%build
rm -rf build
cmake -S . -B build \
      -DCMAKE_INSTALL_PREFIX=/usr \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo

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

DESTDIR=%{buildroot} cmake --install build

%files
%{_bindir}/ubctl
%doc %{_docdir}/ub/%{name}/*
%{_mandir}/man8/ubctl.8.gz

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sat Jun 27 2026 zhao-lichang <zhaolichang@huawei.com> 1.0.3-4
- ub:ubctl:Change the time printing from UTC time to use local time.
- ub:ubctl:Add print fields to the queried port information.
- ub:ubctl:Modify TA layer to obtain WQE delay related registers.
- ub:ubctl:Modify debugfs verification matching rules.
- ub:ubctl:Add the debugfs function.
- ub:ubctl:add querying the peak bandwidth.
- ub:ubctl:Supports the configuration and query of packet statistics on the UBOE interface based on the NL-layer VL.
- ub:ubctl:modify the parsing policy for the speed_ability field in the port_info command.

* Thu May 21 2026 Jiaqi Cheng <chengjiaqi3@huawei.com> - 1.0.3-3
- Change source package name and spec file name.

* Fri Mar 20 2026 Jiaqi Cheng <chengjiaqi3@huawei.com> - 1.0.3-2
- Modify the statistical port link up/down to only count 10 times

* Tue Mar 10 2026 Jiaqi Cheng <chengjiaqi3@huawei.com> - 1.0.3-1
- Adds support for query some functions

* Tue Mar 10 2026 Jiaqi Cheng <chengjiaqi3@huawei.com> - 1.0.2-1
- Modify the incorrect printing of register names in ubctl.

* Wed Dec 10 2025 Jiaqi Cheng <chengjiaqi3@huawei.com> - 1.0.1-0
- Modify TP/TA/SCC register query process.

* Fri Nov 14 2025 Jiaqi Cheng <chengjiaqi3@huawei.com> - 1.0.0-2
- Modify the core dump issue that occurred during the query

* Tue Nov 4 2025 Jiaqi Cheng <chengjiaqi3@huawei.com> - 1.0.0-1
- Add ubctl tool to query desired information
