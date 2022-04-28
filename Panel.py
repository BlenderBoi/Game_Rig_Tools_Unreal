import bpy
import os

from Game_Rig_Tools_Unreal import Utility_Functions

script_file = os.path.realpath(__file__)
addon_directory = os.path.dirname(script_file)
addon_name = os.path.basename(addon_directory)





def draw_rig_ui(layout, obj):

    col = layout.column()


    row = col.row(align=True)
    row.prop(obj.data,'layers', index=0, toggle=True, text='Body Parts')
    row.prop(obj.data,'layers', index=1, toggle=True, text='Joint Tweak')

    row = col.row(align=True)
    row.prop(obj.data,'layers', index=2, toggle=True, text='Fingers')
    row.prop(obj.data,'layers', index=3, toggle=True, text='Fingers Tweak')


    col.separator()
    col.separator()

    row = col.row(align=True)
    row.prop(obj.data,'layers', index=5, toggle=True, text='Reference Skeleton')


    # col.separator()
    # col.separator()
    #
    # row = col.row(align=True)
    # row.prop(obj.data,'layers', index=23, toggle=True, text='UE4 Skeleton')




class GRT_PT_Unreal_Module_Panel(bpy.types.Panel):

    bl_label = "GRT: Unreal Module"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Game Rig Tools"

    def draw(self, context):

        layout = self.layout

        row = layout.row(align=True)
        row.operator("grt.append_mannequin", text="Initiate Mannequin", icon="OUTLINER_OB_ARMATURE")
        row.operator("grt.reset", text="", icon="FILE_REFRESH")
        
        scn = context.scene
        settings = scn.grt_unreal_module_settings


        #
        # layout.separator()
        # layout.separator()
        #
        # if settings.tweak is not None:
        #     box = layout.box()
        #     draw_rig_ui(box, settings.tweak)
        #
        #
        #     layout.separator()
        #     layout.separator()
        #
        #     row = layout.row(align=True)
        #     row.operator("grt.tweak_rig", text="Tweak", icon="MODIFIER")
        #     row.operator("grt.bind_rig", text="Bind", icon="OUTLINER_OB_ARMATURE")
        #
        #     row = layout.row(align=True)
        #     row.operator("grt.inspect_unreal_rig", text="Inspect Mannequin", icon="USER")
        #
        #     layout.separator()
        #     layout.operator("grt.show_all", text="Show All", icon="HIDE_OFF")
        #     layout.separator()
        #     layout.separator()
        #

        # box = layout.box()
        # if Utility_Functions.draw_subpanel(box, "Manual Operators", settings, "manual_operator"):



        row = layout.row(align=True)
        row.label(text="Tweak")


        if settings.tweak:

            operator = row.operator("grt.select_rig", text="", icon="RESTRICT_SELECT_OFF")
            operator.select_target = "TWEAK"


            row.prop(settings.tweak, "hide_viewport", text="") 

            operator = row.operator("grt.solo_rig", text="", icon="RADIOBUT_ON")
            operator.select_target = "TWEAK"

        else:

            row.label(text="Not Found", icon="INFO")


        row = layout.row(align=True)
        row.label(text="Deform")


        if settings.deform:


            operator = row.operator("grt.select_rig", text="", icon="RESTRICT_SELECT_OFF")
            operator.select_target = "DEFORM"

            row.prop(settings.deform, "hide_viewport", text="") 


            operator = row.operator("grt.solo_rig", text="", icon="RADIOBUT_ON")
            operator.select_target = "DEFORM"

        else:

            row.label(text="Not Found", icon="INFO")


        row = layout.row(align=True)
        row.label(text="Unreal")

        if settings.root:
            operator = row.operator("grt.select_rig", text="", icon="RESTRICT_SELECT_OFF")
            operator.select_target = "ROOT"
            row.prop(settings.root, "hide_viewport", text="") 

            operator = row.operator("grt.solo_rig", text="", icon="RADIOBUT_ON")
            operator.select_target = "ROOT"

        else:

            row.label(text="Not Found", icon="INFO")




        layout.separator()
        layout.separator()



        if settings.tweak:
            box = layout.box()
            draw_rig_ui(box, settings.tweak)

        layout.separator()
        layout.separator()

        row = layout.row(align=True)


         
        row.operator("grt.tweak_rig", text="Tweak", icon="MODIFIER")
        row.operator("grt.apply_rig", text="Apply Rig")

        layout.operator("grt.unmute_constraint", text="Constraint")
        layout.operator("grt.switch_parent_armature", text="Switch Parent Armature", icon="UV_SYNC_SELECT")
        layout.operator("grt.copy_additional_bones_to_root", text="Copy Additional Bones To Root", icon="BONE_DATA")



        box = layout.box()
        if Utility_Functions.draw_subpanel(box, "Armature", settings, "show_armatures"):
            self.draw_armatures(context, box)

    
    def draw_armatures(self, context, layout):


        scn = context.scene
        settings = scn.grt_unreal_module_settings

        row = layout.row(align=True)
        row.prop(settings, "root", text="Root")
        operator = row.operator("grt.select_rig", text="", icon="RESTRICT_SELECT_OFF")
        operator.select_target = "ROOT"

        row = layout.row(align=True)
        row.prop(settings, "tweak", text="Tweak")
        operator = row.operator("grt.select_rig", text="", icon="RESTRICT_SELECT_OFF")
        operator.select_target = "TWEAK"

        row = layout.row(align=True)
        row.prop(settings, "deform", text="Deform")
        operator = row.operator("grt.select_rig", text="", icon="RESTRICT_SELECT_OFF")
        operator.select_target = "DEFORM"




classes = [GRT_PT_Unreal_Module_Panel]


def register():

    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
