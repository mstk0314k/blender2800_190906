import bpy

# TUTORIAL_PT_SamplePanel
class TUTORIAL_PT_SamplePanel(bpy.types.Panel):
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
  bl_category = "Tutorial"
  bl_label = "PanelTitle"

  # draw
  def draw(self, context):
    layout = self.layout
    layout.label(text="Hello")
        
class TUTORIAL_PT_TestPanel(bpy.types.Panel):
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
  bl_category = "Tutorial"
  bl_label = "TestPanel"
  
  #draw
  def draw(self, context):
    layout = self.layout
    layout.operator(TUTORIAL_OT_PrintOK.bl_idname, text="Run OK")
    
class TUTORIAL_OT_PrintOK(bpy.types.Operator):
  bl_idname = "tutorial.printok"
  bl_label = "PrintOK"
  bl_options = {"REGISTER", "UNDO"}
  
  def execute(self, context):
    print("OKOKOKOKOKOK")
    return {"FINISHED"}
    