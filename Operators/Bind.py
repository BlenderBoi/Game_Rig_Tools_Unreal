

import bpy

ENUM_Select_Target = [("ROOT","Root","Root"),("TWEAK","Tweak","Tweak"),("DEFORM","Deform","Deform")]

class GRT_OT_Bind(bpy.types.Operator):
    """Show Deform Rig"""
    bl_idname = "grt.bind_rig"
    bl_label = "Bind Rig"


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


            root.hide_viewport = True 
            deform.hide_viewport = False 
            tweak.hide_viewport = True 

            deform.hide_set(False)

            if deform is not None:
                deform.select_set(True)
                context.view_layer.objects.active = deform 

                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

        return {'FINISHED'}


def register():
    bpy.utils.register_class(GRT_OT_Bind)


def unregister():
    bpy.utils.unregister_class(GRT_OT_Bind)


if __name__ == "__main__":
    register()

