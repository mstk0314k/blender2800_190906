import bpy


class SIMU_PT_SETTINGS(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "SimuSettings"
    bl_label = "SimuSettings"

    # draw
    def draw(self, context):
        layout = self.layout
        split = layout.split(factor=0.4)
        split.label(text="RESET_OBJECTS")
        row = split.row(align=True)
        row.operator(SIMU_OT_RESETOBJECTS.bl_idname, text="RESET")


class SIMU_OT_RESETOBJECTS(bpy.types.Operator):
    bl_idname = "simu.resetobjects"
    bl_label = "SimuResetObjects"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        print("ok")
        return {"FINISHED"}
        