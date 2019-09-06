import bpy

from . import test01.py

# bl_info
bl_info = {
  "name": "BlenderTest",
  "description": "This AddOn is first AddOn",
  "author": "masataka",
  "version": (1, 0, 0, 0),
  "blender": (2, 80, 0),
  "support": "TESTING",
  "category": "Tutorial",
  "location": "",
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
