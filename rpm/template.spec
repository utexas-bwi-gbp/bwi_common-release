Name:           ros-indigo-bwi-rqt-plugins
Version:        0.3.3
Release:        0%{?dist}
Summary:        ROS bwi_rqt_plugins package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/bwi_rqt_plugins
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-bwi-msgs
Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-python-qt-binding
Requires:       ros-indigo-qt-gui
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rqt-gui
Requires:       ros-indigo-rqt-gui-cpp
Requires:       ros-indigo-rqt-gui-py
Requires:       ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-rqt-gui
BuildRequires:  ros-indigo-rqt-gui-cpp
BuildRequires:  ros-indigo-sensor-msgs

%description
Displays a simple GUI to the user. The GUI is capable of displaying a simple
message or image to the user, and ask a question. The message and question
plugins are also written in this package.

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
* Wed Aug 05 2015 Piyush Khandelwal <piyushk@gmail.com> - 0.3.3-0
- Autogenerated by Bloom

