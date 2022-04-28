

import bpy

ENUM_Select_Target = [("ROOT","Root","Root"),("TWEAK","Tweak","Tweak"),("DEFORM","Deform","Deform")]

class GRT_OT_Reset(bpy.types.Operator):
    """Reset"""
    bl_idname = "grt.reset"
    bl_label = "Reset"



    def execute(self, context):

        scn = context.scene
        settings = scn.grt_unreal_module_settings


        settings.root = None
        settings.deform = None
        settings.tweak = None 
  

        return {'FINISHED'}


def register():
    bpy.utils.register_class(GRT_OT_Reset)


def unregister():
    bpy.utils.unregister_class(GRT_OT_Reset)


if __name__ == "__main__":
    register()

