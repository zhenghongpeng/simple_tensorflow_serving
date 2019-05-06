import os
import sys
if 'pybuilder' in sys.modules:
    from pybuilder.core import use_plugin, init
else:
    use_plugin = init = id

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.flake8")


name = "aquapion"
version = os.popen(r"git describe --dirty | sed -e 's/[_+~]/-/g' -e 's/\([0-9.]*[0-9]\)[.-]*\(.*\)/\1+\2/' -e 's/-/./g' -e 's/+$//'").read().strip()
default_task = ["analyze", "publish"]

@init
def set_properties(project):
    project.set_property("dir_source_main_python", "")
    project.set_property("dir_source_unittest_python", "test")
    project.set_property("dir_source_main_scripts", "bin")
    project.set_property("coverage_break_build", False)