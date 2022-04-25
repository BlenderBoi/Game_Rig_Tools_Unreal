

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


        view_layer_objects = list(context.view_layer.objects)

        for obj in bpy.data.objects:
            obj.select_set(False)

        if settings.root:
            if settings.root in view_layer_objects:
                settings.root.hide_viewport = False
                settings.root.hide_set(False)
                settings.root.select_set(True) 

        if settings.deform:
            if settings.deform in view_layer_objects:
                settings.deform.hide_viewport = False
                settings.deform.hide_set(False)
                settings.deform.select_set(True) 

        if settings.tweak:
            if settings.tweak in view_layer_objects:
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

