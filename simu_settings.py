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
        for cam in D.cameras:
            print("remove : " + cam.name)
            D.cameras.remove(cam)
        print("---RESET OBJECTS---")

        # set frame parameter
        frame_s = 1
        frame_e = 600

        # set collection
        new_col = D.collections.new("objects")
        C.scene.collection.children.link(new_col)

        # sphere01
        bpy.ops.mesh.primitive_ico_sphere_add(
            subdivisions=2, radius=0.2, calc_uvs=True, enter_editmode=False,
            align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0)
        )
        C.object.name = "sphere01"
        sphere01 = D.objects["sphere01"]
        bpy.ops.rigidbody.object_add(type='ACTIVE')
        new_col.objects.link(sphere01)
        C.scene.collection.objects.unlink(sphere01)
        sphere01.animation_visualization.motion_path.frame_start = frame_s
        sphere01.animation_visualization.motion_path.frame_end = frame_e

        # sphere02
        bpy.ops.mesh.primitive_ico_sphere_add(
            subdivisions=2, radius=0.1, calc_uvs=True, enter_editmode=False,
            align='WORLD', location=(10, 0.0, 0.0), rotation=(0.0, 0.0, 0.0)
        )
        C.object.name = "sphere02"
        sphere02 = D.objects["sphere02"]
        bpy.ops.rigidbody.object_add(type='PASSIVE')
        bpy.ops.object.forcefield_toggle()
        C.object.field.strength = -50
        new_col.objects.link(sphere02)
        C.scene.collection.objects.unlink(sphere02)

        # sphere03
        bpy.ops.mesh.primitive_ico_sphere_add(
            subdivisions=2, radius=0.1, calc_uvs=True, enter_editmode=False,
            align='WORLD', location=(10, 20, 0.0), rotation=(0.0, 0.0, 0.0)
        )
        C.object.name = "sphere03"
        sphere03 = D.objects["sphere03"]
        bpy.ops.rigidbody.object_add(type='PASSIVE')
        bpy.ops.object.forcefield_toggle()
        C.object.field.strength = -50
        new_col.objects.link(sphere03)
        C.scene.collection.objects.unlink(sphere03)

        # sphere04
        bpy.ops.mesh.primitive_ico_sphere_add(
            subdivisions=2, radius=0.1, calc_uvs=True, enter_editmode=False,
            align='WORLD', location=(40, 20, 0.0), rotation=(0.0, 0.0, 0.0)
        )
        C.object.name = "sphere04"
        sphere04 = D.objects["sphere04"]
        bpy.ops.rigidbody.object_add(type='PASSIVE')
        bpy.ops.object.forcefield_toggle()
        C.object.field.strength = -50
        new_col.objects.link(sphere04)
        C.scene.collection.objects.unlink(sphere04)

        # Camera
        bpy.ops.object.camera_add(
            enter_editmode=False, align='WORLD',
            location=(40, -40, 35),
            rotation=(math.radians(60), math.radians(0.0), math.radians(23.6))
        )
        C.object.name = "Camera"
        camera = D.objects["Camera"]
        D.cameras["Camera"].lens = 35
        new_col.objects.link(camera)
        C.scene.collection.objects.unlink(camera)

        # Light
        light_obj = bpy.data.objects.new(
            name="Light", object_data=D.lights[0]
        )
        light_obj.location = [50, -20, 30]
        new_col.objects.link(light_obj)

        # set rigidbody_world
        D.scenes["Scene"].frame_current = 1
        D.scenes["Scene"].rigidbody_world.point_cache.frame_start = frame_s
        D.scenes["Scene"].rigidbody_world.point_cache.frame_end = frame_e
        D.scenes["Scene"].rigidbody_world.collection = new_col
        # D.scenes["Scene"].rigidbody_world.constraints = new_col

        print("---SET OBJECTS---")

        return {"FINISHED"}