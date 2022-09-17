
import bpy



def filter_armature_root(self, object):

    if object.type == "ARMATURE":
        filter_objects = [self.root, self.tweak, self.deform]
    
        if not object in filter_objects:
            return True


ENUM_Rig = [("UE5","Unreal 5 (Manny)","Manny"),("UE4","Unreal 4 (Mannequin)","Mannequin")]

class GRT_Unreal_Module_Settings(bpy.types.PropertyGroup):

    root: bpy.props.PointerProperty(type=bpy.types.Object, poll=filter_armature_root)
    tweak: bpy.props.PointerProperty(type=bpy.types.Object, poll=filter_armature_root)
    deform: bpy.props.PointerProperty(type=bpy.types.Object, poll=filter_armature_root)

    show_armatures: bpy.props.BoolProperty(default=False)
    manual_operator: bpy.props.BoolProperty(default=False)

    rig: bpy.props.EnumProperty(items=ENUM_Rig)



classes = [GRT_Unreal_Module_Settings]


def register():

    for cls in classes:
        bpy.utils.register_class(cls)

    
    bpy.types.Scene.grt_unreal_module_settings = bpy.props.PointerProperty(type=GRT_Unreal_Module_Settings)



def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)



    del bpy.types.Scene.grt_unreal_module_settings





if __name__ == "__main__":

    register()

