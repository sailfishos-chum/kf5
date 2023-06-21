%global qt_version 5.15.8

Name:    opt-kf5
Version: 5.107.0
Release: 1%{?dist}
Summary: Filesystem and RPM macros for KDE Frameworks 5
License: BSD
URL:     http://www.kde.org
Source0: %{name}-%{version}.tar.bz2

%description
Filesystem and RPM macros for KDE Frameworks 5

%package rpm-macros
Summary: RPM macros for KDE Frameworks 5
Requires: cmake >= 3
Requires: opt-qt5-rpm-macros >= 5.11

# misc build environment dependencies
Requires: gcc-c++
BuildArch: noarch
%description rpm-macros
RPM macros for building KDE Frameworks 5 packages.

%prep
%setup -q

%install
install -Dpm644 macros.kf5 %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf5
sed -i \
  -e "s|@@KF5_VERSION@@|%{version}|g" \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf5

%files rpm-macros
%{_rpmconfigdir}/macros.d/macros.kf5
