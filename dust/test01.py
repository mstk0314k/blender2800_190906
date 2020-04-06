import bpy

# TUTORIAL_PT_SamplePanel
class TUTORIAL_PT_SamplePanel(bpy.types.Panel):
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
  bl_category = "TestPanel"
  bl_label = "TestPanel"

  # draw
  def draw(self, context):
    layout = self.layout
    layout.label(text="Hello")
        
class TUTORIAL_PT_TestPanel(bpy.types.Panel):
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
  bl_category = "TestPanel"
  bl_label = "TestPanel"

  bpy.types.Scene.shadow_on_off = bpy.props.BoolProperty(name="",)
  bpy.types.Scene.renderborder = bpy.props.BoolProperty(name="",)
  bpy.types.Scene.jacket_lapel = bpy.props.BoolProperty(name="",)  
  
  # draw
  def draw(self, context):
    layout = self.layout
    scene = context.scene
    
    layout.operator(TUTORIAL_OT_PrintOK.bl_idname, text="Run OK")
    layout.prop(scene, "shadow_on_off", text="影のon")
    layout.prop(scene, "renderborder", text="RenderBorder")
    layout.label(text="レンダリングするパーツ")
    layout.prop(scene, "jacket_lapel", text="jacket_lapel")
    
    
    
class TUTORIAL_OT_PrintOK(bpy.types.Operator):
  bl_idname = "tutorial.printok"
  bl_label = "PrintOK"
  bl_options = {"REGISTER", "UNDO"}
  
  def execute(self, context):
    scene = context.scene
    
    print("TEST OK")

    # sceneでの分岐
    if context.scene["shadow_on_off"]:
      print("shadow_on")
    else:
      print("shadow_off")

    # TODO なんか上手くボーダーを設定できない
    if context.scene["renderborder"]:
      print("renderborder_on")
      # bpy.context.scene.render.border_min_x = 500
      # bpy.context.scene.render.border_max_x = 800
      # bpy.context.scene.render.border_min_y = 300
      # bpy.context.scene.render.border_max_y = 450
      # bpy.context.scene.render.use_border = True
      bpy.ops.view3d.render_border(xmin=500, xmax=800, ymin=300, ymax=550)
      # context.scene.renderborder = True
    else:
      print("renderborder_off")
      bpy.ops.view3d.clear_render_border()
      # bpy.ops.image.clear_render_border()
      # bpy.context.scene.render.use_border = False
      

    WhiteCube = bpy.data.objects["WhiteCube"]
    print(WhiteCube)
    # WhiteCube.hide_viewport = True
    # WhiteCube.hide_render = True
    # WhiteCube.hide_select = True
    
    # TODO collectionのホールドアウトの設定がうまくいかない
    # TODO hide_viewportはいける
    # Col1 = bpy.data.collections["Collection 1"]
    # Col1.hide_select = True
    # Col1.hide_render = True
    
    # Col1.holdout = True
    # bpy.context.scene.holdout = True
    
    

    
    Col3 = bpy.data.collections.new("Col3")
    
    

    
      

    
    
    return {"FINISHED"}
    