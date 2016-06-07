Name:           ros-indigo-bwi-common
Version:        0.3.8
Release:        0%{?dist}
Summary:        ROS bwi_common package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-bwi-gazebo-entities
Requires:       ros-indigo-bwi-interruptable-action-server
Requires:       ros-indigo-bwi-kr-execution
Requires:       ros-indigo-bwi-mapper
Requires:       ros-indigo-bwi-msgs
Requires:       ros-indigo-bwi-planning-common
Requires:       ros-indigo-bwi-tasks
Requires:       ros-indigo-bwi-tools
Requires:       ros-indigo-stop-base
Requires:       ros-indigo-utexas-gdc
BuildRequires:  ros-indigo-catkin

%description
Common packages and data for the Building-Wide Intelligence project of the
University of Texas at Austin.

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
* Mon Jun 06 2016 Piyush Khandelwal <piyushk@gmail.com> - 0.3.8-0
- Autogenerated by Bloom

* Tue Sep 22 2015 Piyush Khandelwal <piyushk@gmail.com> - 0.3.7-0
- Autogenerated by Bloom

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

