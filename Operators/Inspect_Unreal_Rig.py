

import bpy

ENUM_Select_Target = [("ROOT","Root","Root"),("TWEAK","Tweak","Tweak"),("DEFORM","Deform","Deform")]

class GRT_OT_Inspect_Unreal_Rig(bpy.types.Operator):
    """Inspect Unreal Rig"""
    bl_idname = "grt.inspect_unreal_rig"
    bl_label = "Inspect Unreal Rig"


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



            root.hide_viewport = False 
            deform.hide_viewport = False 
            tweak.hide_viewport = False 

            bpy.ops.grt.apply_rig()


            root.hide_viewport = False 
            deform.hide_viewport = True 
            tweak.hide_viewport = True 

            root.hide_set(False)



            if root is not None:
                root.select_set(True)
                context.view_layer.objects.active = root

                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

        return {'FINISHED'}


def register():
    bpy.utils.register_class(GRT_OT_Inspect_Unreal_Rig)


def unregister():
    bpy.utils.unregister_class(GRT_OT_Inspect_Unreal_Rig)


if __name__ == "__main__":
    register()

