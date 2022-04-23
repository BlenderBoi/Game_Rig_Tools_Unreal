
import bpy

ENUM_Select_Target = [("ROOT","Root","Root"),("TWEAK","Tweak","Tweak"),("DEFORM","Deform","Deform")]

class GRT_OT_Select_Rig(bpy.types.Operator):
    """Select Rig, Hold Shift to Add to Selection"""
    bl_idname = "grt.select_rig"
    bl_label = "Select Rig"

    select_target: bpy.props.EnumProperty(items=ENUM_Select_Target)
    deselect: bpy.props.BoolProperty()

    @classmethod
    def poll(cls, context):
        scn = context.scene
        settings = scn.grt_unreal_module_settings

        if settings.tweak and settings.root and settings.deform:
            return True


    def invoke(self, context, event):


        self.deselect = True

        if event.shift:
            self.deselect = False 



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
  
        if self.deselect:
            for loop_obj in bpy.data.objects:
                loop_obj.select_set(False)

        if obj is not None:
            obj.select_set(True)
            context.view_layer.objects.active = obj 


        return {'FINISHED'}


def register():
    bpy.utils.register_class(GRT_OT_Select_Rig)


def unregister():
    bpy.utils.unregister_class(GRT_OT_Select_Rig)


if __name__ == "__main__":
    register()

