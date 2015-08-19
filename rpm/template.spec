Name:           ros-indigo-bwi-planning-common
Version:        0.3.4
Release:        0%{?dist}
Summary:        ROS bwi_planning_common package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/bwi_planning_common
Source0:        %{name}-%{version}.tar.gz

Requires:       SDL_image-devel
Requires:       ros-indigo-bwi-mapper
Requires:       ros-indigo-bwi-tools
Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-python-qt-binding
Requires:       ros-indigo-qt-gui
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rqt-gui
Requires:       ros-indigo-rqt-gui-py
Requires:       ros-indigo-std-msgs
BuildRequires:  SDL_image-devel
BuildRequires:  ros-indigo-bwi-mapper
BuildRequires:  ros-indigo-bwi-tools
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-std-msgs

%description
Common data structures, messages and service defintions used for deterministic
planning work in the BWI project at the University of Texas at Austin

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
* Wed Aug 19 2015 Piyush Khandelwal <piyushk@gmail.com> - 0.3.4-0
- Autogenerated by Bloom

* Wed Aug 05 2015 Piyush Khandelwal <piyushk@gmail.com> - 0.3.3-0
- Autogenerated by Bloom

* Wed Mar 25 2015 Piyush Khandelwal <piyushk@gmail.com> - 0.3.2-0
- Autogenerated by Bloom

