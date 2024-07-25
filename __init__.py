bl_info = {
    "name": "Game Rig Tools - Unreal Module",
    "author": "BlenderBoi",
    "version": (4, 2, 0),
    "blender": (4, 1, 0),
    "description": "Game Rig Tools With Tools Caters to Unreal Workflow",
    "warning": "",
    "doc_url": "https://cgdive.notion.site/Game-Rig-Tools-Documentation-dc61839fd1d04147a42aa89e366575fb",
    "tracker_url": "https://support.tinkerboi.com/t/bug-report",
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
