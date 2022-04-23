

import bpy

ENUM_Select_Target = [("ROOT","Root","Root"),("TWEAK","Tweak","Tweak"),("DEFORM","Deform","Deform")]

class GRT_OT_Tweak(bpy.types.Operator):
    """Tweak Your Rig"""
    bl_idname = "grt.tweak_rig"
    bl_label = "Tweak Rig"


    @classmethod
    def poll(cls, context):
        scn = context.scene
        settings = scn.grt_unreal_module_settings

        if settings.tweak and settings.root and settings.deform:
            return True

    def execute(self, context):


        scn = context.scene
        settings = scn.grt_unreal_module_settings



        root = settings.root
        deform = settings.deform
        tweak= settings.tweak
  
        if root and deform and tweak:

            for loop_obj in bpy.data.objects:
                loop_obj.select_set(False)

            root.hide_viewport = True 
            deform.hide_viewport = True 
            tweak.hide_viewport = False
            tweak.hide_set(False)

            bpy.ops.grt.unmute_constraint()

            if tweak is not None:
                tweak.select_set(True)
                context.view_layer.objects.active = tweak 

                bpy.ops.object.mode_set(mode='POSE', toggle=False)

        return {'FINISHED'}


def register():
    bpy.utils.register_class(GRT_OT_Tweak)


def unregister():
    bpy.utils.unregister_class(GRT_OT_Tweak)


if __name__ == "__main__":
    register()

