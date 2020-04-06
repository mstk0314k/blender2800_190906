import bpy
import math


class SIMU_PT_SETTINGS(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "SimuSettings"
    bl_label = "SimuSettings"

    # draw
    def draw(self, context):
        layout = self.layout
        layout.label(text="RESET_OBJECTS")
        layout.operator(SIMU_OT_RESETOBJECTS.bl_idname, text="RESET")
        # split = layout.split(factor=0.4)
        # split.label(text="RESET_OBJECTS")
        # row = split.row(align=True)
        # row.operator(SIMU_OT_RESETOBJECTS.bl_idname, text="RESET")


class SIMU_OT_RESETOBJECTS(bpy.types.Operator):
    bl_idname = "simu.resetobjects"
    bl_label = "SimuResetObjects"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        C = bpy.context
        D = bpy.data

        for obj in D.objects:
            print("remove : " + obj.name)
            D.objects.remove(obj)
        for col in D.collections:
            print("remove : " + col.name)
            D.collections.remove(col)
        print("---RESET OBJECTS---")

        # set collection
        new_col = D.collections.new("objects")
        C.scene.collection.children.link(new_col)

        # sphere01
        bpy.ops.mesh.primitive_ico_sphere_add(
            subdivisions=2, radius=1.0, calc_uvs=True, enter_editmode=False,
            align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0)
        )
        C.object.name = "sphere01"
        sphere01 = D.objects["sphere01"]
        bpy.ops.rigidbody.object_add(type='ACTIVE')
        new_col.objects.link(sphere01)
        C.scene.collection.objects.unlink(sphere01)

        # sphere02
        bpy.ops.mesh.primitive_ico_sphere_add(
            subdivisions=2, radius=1.0, calc_uvs=True, enter_editmode=False,
            align='WORLD', location=(10, 0.0, 0.0), rotation=(0.0, 0.0, 0.0)
        )
        C.object.name = "sphere02"
        sphere02 = D.objects["sphere02"]
        bpy.ops.rigidbody.object_add(type='ACTIVE')
        new_col.objects.link(sphere02)
        C.scene.collection.objects.unlink(sphere02)

        # Camera
        bpy.ops.object.camera_add(
            enter_editmode=False, align='WORLD',
            location=(12.54, -18.62, 10.88),
            rotation=(math.radians(60), math.radians(0.0), math.radians(23.6))
        )
        C.object.name = "Camera"
        camera = D.objects["Camera"]
        new_col.objects.link(camera)
        C.scene.collection.objects.unlink(camera)

        # Light
        light_obj = bpy.data.objects.new(
            name="Light", object_data=D.lights[0]
        )
        light_obj.location = [8.0, -6.0, 7.0]
        new_col.objects.link(light_obj)

        print("---SET OBJECTS---")

        return {"FINISHED"}