Summary: Implementation of ubctl
Name: ubctl
Version: 1.0.0
Release: 2
License: MIT
URL: https://gitee.com/openeuler/ubctl
Source0: %{name}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

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
DESTDIR=%{buildroot} cmake --install build

%files
%{_bindir}/ubctl


%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Nov 14 2025 Jiaqi Cheng <chengjiaqi3@huawei.com> - 1.0.0-2
- Modify the core dump issue that occurred during the query

* Tue Nov 4 2025 Jiaqi Cheng <chengjiaqi3@huawei.com> - 1.0.0-1
- Add ubctl tool to query desired information
