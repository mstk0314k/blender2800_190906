# bl_info
bl_info = {
    "name": "BlenderTest",
    "description": "Test AddOn",
    "author": "Masataka",
    "version": (1, 0, 0, 0),
    "blender": (2, 80, 0),
    "support": "TESTING",
    "category": "Tutorial",
    "location": "View3D > Sidebar > View Tab",
    "warning": "",
    "wiki_url": "",
    "tracker_url": ""
}

import bpy
import imp
import inspect

from . import test_200406
from . import simu_settings

pythonfiles = [
    test_200406,
    simu_settings,
]

for pyfile in pythonfiles:
    from . import pyfile
    if "bpy" in locals():
        imp.reload(pyfile)
    else:
        from . import pyfile


# register
def register():
    print("------")
    for cls in classes:
        print("Register : "+str(cls[0]))
        bpy.utils.register_class(cls[1])
    print("------")


# unregister
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls[1])
    print("unregist addon")


# class list
classes = []
for pyfile in pythonfiles:
    classes.extend(inspect.getmembers(pyfile, inspect.isclass))


# AddOn Entry
if __name__ == "__main__":
    register()
