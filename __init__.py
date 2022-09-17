
bl_info = {
    "name": "Game Rig Tools - Unreal Module",
    "author": "BlenderBoi",
    "version": (1, 1, 0),
    "blender": (3, 1, 0),
    "description": "Game Rig Tools With Tools Caters to Unreal Workflow",
    "warning": "",
    "doc_url": "https://tarry-dill-523.notion.site/Game-Rig-Tools-Documentation-dc61839fd1d04147a42aa89e366575fb",
    "category": "Armature",
}

import bpy
from . import Operators
from . import Preferences
from . import Property



modules = [Property, Operators, Preferences]


def register():

    for module in modules:
        module.register()

def unregister():

    for module in modules:
        module.unregister()

if __name__ == "__main__":
    register()
