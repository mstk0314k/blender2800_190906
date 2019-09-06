import bpy

#
# TUTORIAL_PT_SamplePanel
#
class TUTORIAL_PT_SamplePanel(bpy.types.Panel):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = "Tutorial"
  bl_label = "PanelTitle"

  #--- draw ---#
  def draw(self, context):
    layout = self.layout
    layout.label(text="Hello")
        

#
# register classs
#
classs = [
  TUTORIAL_PT_SamplePanel
]

#
# register
#
def register():
  for c in classs:
    bpy.utils.register_class(c)

#
# unregister
#        
def unregister():
  for c in classs:
    bpy.utils.register_class(c)

#
# script entry
#        
if __name__ == "__main__":
  register()