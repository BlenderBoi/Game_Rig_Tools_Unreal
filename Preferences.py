import bpy
import os
from . import Panel 


script_file = os.path.realpath(__file__)
addon_directory = os.path.dirname(script_file)
addon_name = os.path.basename(addon_directory)


def update_panel(self, context):

    addon_preferences = context.preferences.addons[addon_name].preferences
    message = ": Updating Panel locations has failed"
    try:

        if "bl_rna" in Panel.GRT_PT_Unreal_Module_Panel.__dict__:
            bpy.utils.unregister_class(Panel.GRT_PT_Unreal_Module_Panel)


        Panel.GRT_PT_Unreal_Module_Panel.bl_category = addon_preferences.unreal_module_panel_name
        bpy.utils.register_class(Panel.GRT_PT_Unreal_Module_Panel)



    except Exception as e:
        print("\n[{}]\n{}\n\nError:\n{}".format(__name__, message, e))
        pass



class GRT_UNREAL_user_preferences(bpy.types.AddonPreferences):
    bl_idname = __package__



    unreal_module_panel_name: bpy.props.StringProperty(default="Game Rig Tool", update=update_panel)




    def draw(self, context):
        layout = self.layout
        layout.prop(self, "unreal_module_panel_name", text="Panel Name")




classes = [GRT_UNREAL_user_preferences, Panel.GRT_PT_Unreal_Module_Panel]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    update_panel(None, bpy.context)



def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
