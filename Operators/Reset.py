

import bpy

ENUM_Select_Target = [("ROOT","Root","Root"),("TWEAK","Tweak","Tweak"),("DEFORM","Deform","Deform")]

class GRT_OT_Reset(bpy.types.Operator):
    """Reset"""
    bl_idname = "grt.reset"
    bl_label = "Reset"



    def execute(self, context):

        if context.active_object:
            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

        scn = context.scene
        settings = scn.grt_unreal_module_settings

        for obj in bpy.data.objects:
            obj.select_set(False)

        if settings.root:
            settings.root.hide_viewport = False
            settings.root.hide_set(False)
            settings.root.select_set(True) 

        if settings.deform:
            settings.deform.hide_viewport = False
            settings.deform.hide_set(False)
            settings.deform.select_set(True) 

        if settings.tweak:
            settings.tweak.hide_set(False)
            settings.tweak.hide_viewport = False
            settings.tweak.select_set(True) 

            context.view_layer.objects.active = settings.tweak

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

