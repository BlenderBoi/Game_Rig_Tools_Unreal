
import bpy

from . import Append_Mannequin
from . import Select_Rig
from . import Solo_Rig
from . import Apply_Rig
from . import Unmute_Constraint
from . import Tweak
from . import Bind
from . import Inspect_Unreal_Rig
from . import Show_All
from . import Reset
from . import Switch_Parent_Armature
from . import Copy_Additional_Bone_To_Root

modules = [Copy_Additional_Bone_To_Root, Switch_Parent_Armature, Reset, Show_All, Inspect_Unreal_Rig, Tweak, Bind, Unmute_Constraint, Apply_Rig, Append_Mannequin, Select_Rig, Solo_Rig]


def register():

    for module in modules:
        module.register()

def unregister():

    for module in modules:
        module.unregister()

if __name__ == "__main__":
    register()
