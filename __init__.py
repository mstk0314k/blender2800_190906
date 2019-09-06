import bpy

from . import test01

if "bpy" in locals():
  import imp
  imp.reload(test01)
else:
  from . import test01

# class list
classes = [
  test01.TUTORIAL_PT_SamplePanel,
  test01.TUTORIAL_PT_TestPanel,
  test01.TUTORIAL_OT_PrintOK
]

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

# register
def register():
  for cls in classes:
    print("Register : "+str(cls))
    bpy.utils.register_class(cls)

# unregister
def unregister():
  for cls in classes:
    bpy.utils.unregister_class(cls)
  print("unregist addon")

# AddOn Entry
if __name__ == "__main__":
  register()
