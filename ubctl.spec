Summary: Implementation of ubctl
Name: ubctl
Version: 1.0.3
Release: 3%{?dist}
License: MIT
URL: https://gitee.com/openeuler/ubctl
Source0: %{name}-%{version}.tar.gz
Source1: LICENSE

Patch1: 0001-ub-ubctl-Modify-the-incorrect-printing-of-register-n.patch
Patch2: 0002-ub-ubctl-Supports-query-commands-and-can-retrieve-st.patch
Patch3: 0003-ub-ubctl-Support-querying-statistical-indicators-at-.patch
Patch4: 0004-ub-ubctl-Support-querying-real-time-bandwidth-statis.patch
Patch5: 0005-ub-ubctl-Support-querying-firmware-version-numbers.patch
Patch6: 0006-ub-ubctl-Support-querying-the-historical-status-of-p.patch
Patch7: 0007-ub-ubctl-Incorporate-minor-optimizations-for-various.patch
Patch8: 0008-ub-ubctl-Modify-the-statistical-port-link-up-down-to.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-podlators
ExclusiveArch:  aarch64

%description
This implementation provides ubctl sending and reception.

%prep
%autosetup -p1 -n %{name}-%{version}
cp -p %{SOURCE1} LICENSE

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
%license LICENSE
%{_bindir}/ubctl
%doc %{_docdir}/ub/%{name}/*
%{_mandir}/man8/ubctl.8.gz

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Jul 15 2026 qiushengming <846759657@qq.com> - 1.0.3-3
- [Type] sync
- [DESC] Package init.
