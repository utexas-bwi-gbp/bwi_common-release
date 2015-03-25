Name:           ros-hydro-bwi-gazebo-entities
Version:        0.3.2
Release:        0%{?dist}
Summary:        ROS bwi_gazebo_entities package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/bwi_gazebo_entities
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-gazebo-ros
Requires:       ros-hydro-xacro
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-roslaunch

%description
Simulation objects and avatars used in experiments.

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
* Tue Mar 24 2015 Piyush Khandelwal <piyushk@gmail.com> - 0.3.2-0
- Autogenerated by Bloom

* Mon Mar 16 2015 Piyush Khandelwal <piyushk@gmail.com> - 0.3.1-0
- Autogenerated by Bloom

