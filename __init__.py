import bpy

from . import test01

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
  print("regist addon")

# unregister
def unregister():
  print("unregist addon")

# AddOn Entry
if __name__ == "__main__":
  register()
