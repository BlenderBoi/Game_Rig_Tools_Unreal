

import bpy
import os

def get_asset_folder():
    
    my_path = __file__
    addon_directory = os.path.dirname(__file__)
    asset_directory = os.path.join(addon_directory, "Assets")

    return asset_directory

def get_pre_extracted_mannequin_path():
    
    asset_directory = get_asset_folder() 
    mannequin_path = os.path.join(asset_directory, "pre_extracted_mannequin_system.blend")
    
    return mannequin_path


def draw_subpanel(layout, label, source, property):

    state = getattr(source, property)
    
    if state:
        icon = "TRIA_DOWN"    
    else:
        icon = "TRIA_RIGHT"

    row = layout.row(align=True)
    row.alignment = "LEFT"
    row.prop(source, property, text=label, icon=icon, emboss=False)

    return state 


def apply_all_bone_constraints_and_pose(obj):

    if obj is not None:

        obj.hide_viewport = False
        obj.hide_set(False)

        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

        bpy.ops.object.mode_set(mode='POSE', toggle=False)


        if obj.type == "ARMATURE":
            
            for bone in obj.pose.bones:


                mat = bone.matrix.copy()

                for constraint in bone.constraints:
                    constraint.mute = True
        
                bone.matrix = mat

        bpy.ops.pose.armature_apply(selected=False)


