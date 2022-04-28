
import bpy
from Game_Rig_Tools_Unreal import Utility_Functions


import pathlib













class GRT_OT_Append_Mannequin(bpy.types.Operator):
    """Append Mannequin"""
    bl_idname = "grt.append_mannequin"
    bl_label = "Append Mannequin"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):


        scn = context.scene
        settings = scn.grt_unreal_module_settings

        if settings.root == None and settings.tweak == None and settings.deform == None:
            return True

    def execute(self, context):

        if context.active_object:
            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)


        objects = list(bpy.data.objects)
        collections = list(bpy.data.collections)

        mannequin_path = Utility_Functions.get_pre_extracted_mannequin_path()
        mannequin_path = pathlib.Path(mannequin_path)
        
        blendfile = str(mannequin_path)
        section = "\\Collection\\"
        collection = "Mannequin_UE4"


        filepath = blendfile + section + collection
        directory = blendfile + section 
        filename = collection

        bpy.ops.wm.append(filename=filename, directory=directory)

        appended_objects = []

        for obj in bpy.data.objects:
            if not obj in objects:
                appended_objects.append(obj) 








        scn = context.scene
        settings = scn.grt_unreal_module_settings





        for obj in appended_objects:
            if obj.type == "ARMATURE":

                if "root" in obj.name:
                    settings.root = obj
                    obj.show_in_front = True
                    obj.select_set(False)
                    # obj.hide_viewport = True

                if "UE4_mannequin_DEFORM" in obj.name:
                    settings.deform = obj
                    obj.show_in_front = True
                    obj.select_set(False)
                    # obj.hide_viewport = True

                if "UE4_mannequin_TWEAK" in obj.name:
                    settings.tweak = obj
                    obj.select_set(True)
                    obj.show_in_front = True
                    bpy.context.view_layer.objects.active = obj 
                    bpy.ops.object.mode_set(mode='POSE', toggle=False)





        return {'FINISHED'}


def register():
    bpy.utils.register_class(GRT_OT_Append_Mannequin)


def unregister():
    bpy.utils.unregister_class(GRT_OT_Append_Mannequin)


if __name__ == "__main__":
    register()

