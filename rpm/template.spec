Name:           ros-indigo-bwi-joystick-teleop
Version:        0.3.12
Release:        0%{?dist}
Summary:        ROS bwi_joystick_teleop package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/bwi_joystick_teleop
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-joy
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-joy
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs

%description
Allows robots to be controlled with joysticks through the use of the joy
library.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Sep 14 2016 Alex Gonzales <musigonzales@gmail.com> - 0.3.12-0
- Autogenerated by Bloom

* Sat Aug 27 2016 Alex Gonzales <musigonzales@gmail.com> - 0.3.11-0
- Autogenerated by Bloom

* Mon Aug 15 2016 Alex Gonzales <musigonzales@gmail.com> - 0.3.10-0
- Autogenerated by Bloom

* Fri Aug 05 2016 Alex Gonzales <musigonzales@gmail.com> - 0.3.9-0
- Autogenerated by Bloom

* Mon Jun 06 2016 Alex Gonzales <musigonzales@gmail.com> - 0.3.8-0
- Autogenerated by Bloom

