Name:           ros-indigo-utexas-gdc
Version:        0.3.6
Release:        0%{?dist}
Summary:        ROS utexas_gdc package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-bwi-gazebo-entities
Requires:       ros-indigo-bwi-planning-common
Requires:       ros-indigo-gazebo-ros
Requires:       ros-indigo-map-server
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roslaunch

%description
Simulation environment for the Gates Dell Complex of the University of Texas At
Austin

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
* Tue Aug 25 2015 Piyush Khandelwal <piyushk@gmail.com> - 0.3.6-0
- Autogenerated by Bloom

* Sat Aug 22 2015 Piyush Khandelwal <piyushk@gmail.com> - 0.3.5-0
- Autogenerated by Bloom

* Wed Aug 19 2015 Piyush Khandelwal <piyushk@gmail.com> - 0.3.4-0
- Autogenerated by Bloom

* Wed Aug 05 2015 Piyush Khandelwal <piyushk@gmail.com> - 0.3.3-0
- Autogenerated by Bloom

* Wed Mar 25 2015 Piyush Khandelwal <piyushk@gmail.com> - 0.3.2-0
- Autogenerated by Bloom

