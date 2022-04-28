

import bpy

ENUM_Select_Target = [("ROOT","Root","Root"),("TWEAK","Tweak","Tweak"),("DEFORM","Deform","Deform")]

class GRT_OT_Switch_Parent_Armature(bpy.types.Operator):
    """Switch Parent Armature"""
    bl_idname = "grt.switch_parent_armature"
    bl_label = "Switch Parent Armature"



    def execute(self, context):

        scn = context.scene
        settings = scn.grt_unreal_module_settings


        root = settings.root
        deform = settings.deform
        tweak = settings.tweak
        
        for object in bpy.data.objects:
            for modifier in object.modifiers:
                if modifier.type == "ARMATURE":

                    if modifier.object == deform:
                        modifier.object = root  

                    elif modifier.object == root:
                        modifier.object = deform

        return {'FINISHED'}


def register():
    bpy.utils.register_class(GRT_OT_Switch_Parent_Armature)


def unregister():
    bpy.utils.unregister_class(GRT_OT_Switch_Parent_Armature)


if __name__ == "__main__":
    register()

