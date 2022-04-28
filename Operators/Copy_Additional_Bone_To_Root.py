

import bpy


class GRT_OT_Copy_Additional_Bones_To_Root(bpy.types.Operator):
    """Copy Additional Bones to Root"""
    bl_idname = "grt.copy_additional_bones_to_root"
    bl_label = "Copy Additional Bones To Root"

    remove_missing: bpy.props.BoolProperty(default=False)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "remove_missing", text="Remove Missing Bone")


    def invoke(self, context, event):

        return context.window_manager.invoke_props_dialog(self)


    @classmethod
    def poll(cls, context):
        scn = context.scene
        settings = scn.grt_unreal_module_settings

        if settings.tweak and settings.root and settings.deform:
            return True

    def execute(self, context):


        scn = context.scene
        settings = scn.grt_unreal_module_settings



        root = settings.root
        deform = settings.deform
        tweak= settings.tweak
  
        if root and deform and tweak:


            copy_armature= deform.copy()
            copy_armature.data = deform.data.copy()
            context.collection.objects.link(copy_armature)

            root.hide_set(False)
            root.hide_viewport =False

            copy_armature.hide_set(False)
            copy_armature.hide_viewport =False

            copy_armature.select_set(True)
            context.view_layer.objects.active = copy_armature 

            bpy.ops.object.mode_set(mode='EDIT', toggle=False)

            root_bones = [bone.name for bone in root.data.bones]
            
            deform_bones = [bone.name for bone in deform.data.bones]

            parents = []


            for bone in copy_armature.data.edit_bones:

                if not bone.name in root_bones:
                    if bone.parent:
                        if bone.parent.name in root_bones:
                            parents.append((bone.name, bone.parent.name))


            for bone in copy_armature.data.edit_bones:

                if bone.name in root_bones:
                    copy_armature.data.edit_bones.remove(bone)
                    


                

            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)


            c = {}
            c["object"] = root
            c["active_object"] = root
            c["selected_objects"] = [root, copy_armature]
            c["selected_editable_objects"] = [root, copy_armature]

            bpy.ops.object.join(c)

            root.select_set(True)
            context.view_layer.objects.active = root
            bpy.ops.object.mode_set(mode='EDIT', toggle=False)

               
            for pair in parents:
               
                child = root.data.edit_bones.get(pair[0])
                parent = root.data.edit_bones.get(pair[1])

                if child and parent:

                    child.parent = parent

            if self.remove_missing:
                for bone in root.data.edit_bones:
                    if not bone.name in deform_bones:
                        root.data.edit_bones.remove(bone)



            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)


        return {'FINISHED'}


def register():
    bpy.utils.register_class(GRT_OT_Copy_Additional_Bones_To_Root)


def unregister():
    bpy.utils.unregister_class(GRT_OT_Copy_Additional_Bones_To_Root)


if __name__ == "__main__":
    register()

