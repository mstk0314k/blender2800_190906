import bpy
import math


class SIMU_PT_PLAY_TEST(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "SimuSettings"
    bl_label = "SimuPlayTest"

    # draw
    def draw(self, context):
        layout = self.layout
        layout.label(text="PLAY")
        layout.operator(SIMU_OT_PLAY_TEST.bl_idname, text="PLAY")


class SIMU_OT_PLAY_TEST(bpy.types.Operator):
    bl_idname = "simu.playtest"
    bl_label = "SimuPlayTest"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        C = bpy.context
        D = bpy.data

        print("---PLAY---")
        bpy.ops.screen.animation_play()

        return {"FINISHED"}
