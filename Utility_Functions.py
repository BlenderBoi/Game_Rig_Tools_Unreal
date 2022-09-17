

import bpy
import os
import pathlib

asset_version = {
        "UE4": "pre_extracted_manny_system_ue5.blend", 
        "UE5": "pre_extracted_mannequin_system_ue4.blend"
        }





def get_asset_folder():
    
    my_path = __file__
    addon_directory = os.path.dirname(__file__)
    asset_directory = os.path.join(addon_directory, "Assets")

    return asset_directory

def get_pre_extracted_mannequin_path(version):
    


    asset_directory = get_asset_folder() 
    mannequin_path = os.path.join(asset_directory, asset_version[version])
    
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


def apply_all_bone_constraints_and_pose(obj,constraint=True, mute=True, pose=True):

    if obj is not None:

        obj.hide_viewport = False
        obj.hide_set(False)

        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

        bpy.ops.object.mode_set(mode='POSE', toggle=False)


        if obj.type == "ARMATURE":

            bones = obj.data.bones
            # for bone in bones:
            #     bones.active = bone
            #     bpy.ops.constraint.apply(constraint="Copy Transforms", owner='BONE')
    
            if constraint:
                for bone in obj.pose.bones:

                    mat = bone.matrix.copy()
                    bone.matrix = mat

            if mute:
                for bone in obj.pose.bones:
                    for constraint in bone.constraints:
                        constraint.mute = True

            if pose:
                bpy.ops.pose.armature_apply(selected=False)


