import bpy


class TEST_PT_SAMPLEPANEL(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "TestPanel"
    bl_label = "TestPanel"

    # draw
    def draw(self, context):
        layout = self.layout
        layout.label(text="Hello")
        layout.operator(TEST_OT_SAMPLEHELLO.bl_idname, text="Hello")


class TEST_OT_SAMPLEHELLO(bpy.types.Operator):
    bl_idname = "test.samplehello"
    bl_label = "TestSampleHello"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        print("Hello")

        return {"FINISHED"}




