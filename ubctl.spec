Summary: Implementation of ubctl
Name: ubctl
Version: 1.0.4
Release: 1
License: MIT
URL: https://gitee.com/openeuler/ubctl
Source0: %{name}.tar.gz

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
%setup -q -n ubctl

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
* Wed May 13 2026 Jiaqi Cheng <chengjiaqi3@huawei.com> - 1.0.4-1
- Modify the parsing policy for the speed_ability field in the port_info command. 

* Thu Mar 19 2026 Jiaqi Cheng <chengjiaqi3@huawei.com> - 1.0.3-2
- Modify the statistical port link up/down to only count 10 times

* Wed Mar 4 2026 Jiaqi Cheng <chengjiaqi3@huawei.com> - 1.0.3-1
- Incorporate minor optimizations for various scenarios

* Sat Feb 28 2026 Jiaqi Cheng <chengjiaqi3@huawei.com> - 1.0.3-0
- Adds support for query some functions

* Sat Jan 31 2026 Jiaqi Cheng <chengjiaqi3@huawei.com> - 1.0.2-0
- Modify the incorrect printing of register names in ubctl.

* Wed Dec 10 2025 Jiaqi Cheng <chengjiaqi3@huawei.com> - 1.0.1-0
- Modify TP/TA/SCC register query process.

* Fri Nov 14 2025 Jiaqi Cheng <chengjiaqi3@huawei.com> - 1.0.0-2
- Modify the core dump issue that occurred during the query

* Tue Nov 4 2025 Jiaqi Cheng <chengjiaqi3@huawei.com> - 1.0.0-1
- Add ubctl tool to query desired information
