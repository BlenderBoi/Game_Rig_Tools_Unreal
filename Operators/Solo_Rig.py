
import bpy

ENUM_Select_Target = [("ROOT","Root","Root"),("TWEAK","Tweak","Tweak"),("DEFORM","Deform","Deform")]

class GRT_OT_Solo_Rig(bpy.types.Operator):
    """Select Rig, Hold Shift to Add to Selection"""
    bl_idname = "grt.solo_rig"
    bl_label = "Select Rig"

    select_target: bpy.props.EnumProperty(items=ENUM_Select_Target)
    unhide_all: bpy.props.BoolProperty()

    @classmethod
    def poll(cls, context):
        scn = context.scene
        settings = scn.grt_unreal_module_settings

        if settings.tweak and settings.root and settings.deform:
            return True


    def invoke(self, context, event):


        self.unhide_all = False 

        if event.shift:
            self.unhide_all = True 



        return self.execute(context)

    def execute(self, context):


        scn = context.scene
        settings = scn.grt_unreal_module_settings

        obj = None

        if self.select_target == "ROOT":

            obj = settings.root

        if self.select_target == "DEFORM":

            obj = settings.deform

        if self.select_target == "TWEAK":

            obj = settings.tweak
  
        if self.unhide_all:
            if settings.root:
                settings.root.hide_viewport = False 

            if settings.deform:
                settings.deform.hide_viewport = False 

            if settings.tweak:
                settings.tweak.hide_viewport = False 
        else:

            if settings.root:
                settings.root.hide_viewport = True 

            if settings.deform:
                settings.deform.hide_viewport = True 

            if settings.tweak:
                settings.tweak.hide_viewport = True



            if obj is not None:
                obj.hide_viewport = False


        if obj is not None:
            obj.select_set(True)
            context.view_layer.objects.active = obj 


        return {'FINISHED'}


def register():
    bpy.utils.register_class(GRT_OT_Solo_Rig)


def unregister():
    bpy.utils.unregister_class(GRT_OT_Solo_Rig)


if __name__ == "__main__":
    register()

