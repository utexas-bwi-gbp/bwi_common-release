^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package bwi_tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.3.1 (2015-03-16)
------------------

0.3.0 (2015-03-15)
------------------
* fix many catkin lint errors
  For remaining error, see `#13 <https://github.com/utexas-bwi/bwi_common/issues/13>`_
* indigo: fix opencv2 dependencies (`#10 <https://github.com/utexas-bwi/bwi_common/issues/10>`_)
* added missing dependency on roslib.
* added a resource resolver from multimap code.
* a lot of small utility functions.
* Contributors: Jack O'Quin, Piyush Khandelwal, piyushk

0.2.4 (2014-04-29)
------------------

0.2.3 (2014-04-24)
------------------

0.2.2 (2014-04-19)
------------------

0.2.1 (2014-04-18)
------------------

0.2.0 (2014-04-16)
------------------

* Initial release to Hydro.
* Now passes catkin_lint checks.
* Added ability to control the botton of bars and colors.
* Added convenience function. expand legend automatically.
* Added some common graphing functions.
* Added roslaunch helper to bwi_tools.
* Fixed dependencies in package.xml, fixed greyscale color in pgm
  image, added a python mapper helper.
* Added a boost convenience wrapper.
* Moved the unified point structure to bwi_common.
* Migrated bwi_tools to bwi_common.
