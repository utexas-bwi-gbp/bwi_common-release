Name:           ros-hydro-bwi-interruptable-action-server
Version:        0.3.1
Release:        0%{?dist}
Summary:        ROS bwi_interruptable_action_server package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-actionlib
Requires:       ros-hydro-actionlib-tutorials
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-std-srvs
BuildRequires:  ros-hydro-actionlib
BuildRequires:  ros-hydro-actionlib-tutorials
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-std-srvs

%description
This wraps the move_base node from the standard ROS navigation stack. The
purpose of the interruptable navigator is to allow seamless multi-robot
interactions by temporarily interrupting robots and diverting them when two
robots are about to collide.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Mar 16 2015 Piyush Khandelwal <piyushk@gmail.com> - 0.3.1-0
- Autogenerated by Bloom

