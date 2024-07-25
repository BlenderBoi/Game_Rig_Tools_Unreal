import bpy
from .. import Utility_Functions


class GRT_OT_Unmute_Constraint(bpy.types.Operator):
    """Unmute Constraint"""

    bl_idname = "grt.unmute_constraint"
    bl_label = "Unmute Constraint"

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

        root = settings.root
        deform = settings.deform
        tweak = settings.tweak

        if deform and root and tweak:
            for bone in deform.pose.bones:
                # constraint = bone.constraints.new("COPY_TRANSFORMS")
                # constraint.target = settings.tweak
                # constraint.subtarget = bone.name
                for constraint in bone.constraints:
                    constraint.mute = False

            for bone in root.pose.bones:
                # constraint = bone.constraints.new("COPY_TRANSFORMS")
                # constraint.target = settings.tweak
                # constraint.subtarget = bone.name
                for constraint in bone.constraints:
                    constraint.mute = False

        return {"FINISHED"}


def register():
    bpy.utils.register_class(GRT_OT_Unmute_Constraint)


def unregister():
    bpy.utils.unregister_class(GRT_OT_Unmute_Constraint)


if __name__ == "__main__":
    register()
