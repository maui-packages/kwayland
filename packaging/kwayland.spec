# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kwayland

# >> macros
# << macros

Summary:    Wayland support for Plasma
Version:    5.1.0
Release:    2
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kwayland.yaml
Source101:  kwayland-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  qt5-qttools-linguist

%description
Wayland support for Plasma.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
%find_lang kcoreaddons5_qt --with-qt --all-name || :
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%doc COPYING.LIB
%{_kf5_libdir}/lib*.so.*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/*
%{_kf5_libdir}/*.so
%{_kf5_cmakedir}/*
# >> files devel
# << files devel
