
import bpy
from Game_Rig_Tools_Unreal import Utility_Functions

class GRT_OT_Apply_Rig(bpy.types.Operator):
    """Apply Rig Pose"""
    bl_idname = "grt.apply_rig"
    bl_label = "Apply Rig"

    @classmethod
    def poll(cls, context):
        scn = context.scene
        settings = scn.grt_unreal_module_settings

        if settings.tweak and settings.root and settings.deform:
            return True

    def execute(self, context):


        scn = context.scene
        settings = scn.grt_unreal_module_settings

        obj = None

        # if context.active_object is not None:
        #     bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

        bpy.ops.grt.unmute_constraint()
         

        root = settings.root
        deform = settings.deform
        tweak = settings.tweak
  


        if deform and tweak:

            for obj in bpy.data.objects:
                obj.select_set(False)


            deform.select_set(True)
            tweak.select_set(True)
            context.view_layer.objects.active = deform 


            Utility_Functions.apply_all_bone_constraints_and_pose(deform) 
            Utility_Functions.apply_all_bone_constraints_and_pose(root) 







                







        return {'FINISHED'}


def register():
    bpy.utils.register_class(GRT_OT_Apply_Rig)


def unregister():
    bpy.utils.unregister_class(GRT_OT_Apply_Rig)


if __name__ == "__main__":
    register()

