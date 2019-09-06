import bpy
import os.path
import time
import pathlib
import sys


# AddMaterials
class AddMaterials(bpy.types.Operator):
    bl_idname = "run.add_materials"
    bl_label = "auto add materials"
    bl_description = "add materials to material_master"
    bl_options = {"REGISTER", "UNDO"}

    # remove duplicates
    def remove_duplicates(self, context):
        material_master = bpy.data.objects["material_master"]
        materials = []

        for mat in material_master.data.materials:
            materials.append(mat.name)

        # make duplicates list
        materials = list(set(materials))
        # remove dupulicate materials
        for i, mat in enumerate(material_master.data.materials):
            material_master.active_material_index = i
            bpy.ops.object.material_slot_remove()
        # append over-removed materials
        for mat in materials:
            material_master.data.materials.append(bpy.data.materials[mat])

    def execute(self, context):
        material_master = bpy.data.objects["material_master"]
        material_target = context.scene["mat_data"]
        for mat in bpy.data.materials:
            if mat.name.find(material_target) != -1:
                material_master.data.materials.append(mat)
        self.remove_duplicates(context)
        return {"FINISHED"}


# ResetMaterials
class ResetMaterials(bpy.types.Operator):
    bl_idname = "run.reset_materials"
    bl_label = "auto reset materials"
    bl_description = "reset materials of material_master"
    bl_options = {"REGISTER", "UNDO"}

    # reset
    def execute(self, context):
        material_master = bpy.data.objects["material_master"]
        for mat in material_master.data.materials:
            bpy.ops.object.material_slot_remove()
        return {"FINISHED"}


# control panel
class RenderingControlPanel(bpy.types.Panel):
    bl_idname = "panel.add_materials"
    bl_label = "Add Materials"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Rendering Control"

    bpy.types.Scene.mat_data = bpy.props.StringProperty(name="",)

    def draw(self, context):
        layout_shirt = self.layout
        scene = context.scene
        column_shirt = layout_shirt.column(align=True)

        # add materials
        column_shirt.label(text="マテリアルの一括追加")
        column_shirt.prop(scene, "mat_data")
        column_shirt.operator("run.add_materials", text="Assign")

        # reset materials
        column_shirt.label(text="マテリアルのリセット")
        column_shirt.operator("run.reset_materials", text="Reset")

classs = [AddMaterials, ResetMaterials, RenderingControlPanel]

def register():
    for c in classs:
        bpy.utils.register_class(c)


def unregister():
    for c in classs:
        bpy.utils.register_class(c)


if __name__ == "__main__":
    register()
