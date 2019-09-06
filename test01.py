import bpy


# TUTORIAL_OT_HELLOADDON
class TUTORIAL_OT_HELLOADDON(bpy.types.Operator):
  bl_idname = "tutorial.helloaddon"
  bl_label = "HelloAddOn"

  def execute(self, context):
    print("Hello AddOn")

    return {'FINISHED'}


# register
def register():
  print("regist addon")
  bpy.utils.register_class(TUTORIAL_OT_HELLOADDON)


# unregister
def unregister():
  print("unregist addon")
  bpy.utils.unregister_class(TUTORIAL_OT_HELLOADDON)


# AddOn Entry
if __name__ == "__main__":
  register()