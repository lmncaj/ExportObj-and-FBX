#  ##### BEGIN GPL LICENSE BLOCK #####
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "ExportObjandFBX",
    "author": "FON(フォーン)",
    "version": (0, 0, 1),
    "blender": (2, 92, 0),
    "location": "In the info header",
    "description": "Export selected Object as Obj and FBX",
    "warning": "",
    "category": "Object",
}

import bpy
import os
from os.path import join, normpath
import platform

# Set export directory --------------------- 
type_os = platform.system()

if type_os == "Windows":
    user_home = os.getenv('userprofile')

else:
    user_home = os.path.expanduser("~")
  
copypaste_dir = normpath(join("/Desktop/exportedObjFBX"))
dirpath = str(user_home) + copypaste_dir + "/"

if not "Desktop" in os.listdir(user_home):  
    os.makedirs(dirpath)

#----------------------------------------------

class ExportObject(bpy.types.Operator):
    bl_idname = "object.export_object"
    bl_label = "ExportObj/FBX"
    bl_description = "Export selected object as Obj and FBX"
    bl_options = {'REGISTER', 'UNDO'}

    # >>>>>>>>>>>>>>> Export selected models <<<<<<<<<<<<<<< #

    def execute(self, context):

        sel = bpy.context.selected_objects

        for obj in sel:
            # deselect all meshes
            bpy.ops.object.select_all(action='DESELECT')

            # select the object
            obj.select_set(state = True)

            Objfull_dirpath = normpath(join(dirpath + obj.name + ".obj"))
            # export object as Obj
            bpy.ops.export_scene.obj(
                filepath=Objfull_dirpath,
                check_existing=True,
                axis_forward='-Z',
                axis_up='Y',
                filter_glob=".obj;.mtl",
                use_selection=True,
                use_animation=False,
                use_mesh_modifiers=True,
                use_edges=True,
                use_smooth_groups=False,
                use_smooth_groups_bitflags=False,
                use_normals=True,
                use_uvs=True,
                use_materials=True,
                use_triangles=False,
                use_nurbs=False,
                use_vertex_groups=False,
                use_blen_objects=True,
                group_by_object=False,
                group_by_material=False,
                keep_vertex_order=False,
                global_scale=1.0,
                path_mode='AUTO'
                )

            FBXfull_dirpath = normpath(join(dirpath + obj.name + ".fbx"))
            # export object as FBX
            bpy.ops.export_scene.fbx(
                filepath=FBXfull_dirpath, 
                check_existing=True,
                filter_glob='*.fbx',
                use_selection=True,
                use_active_collection=False,
                global_scale=1.0,
                apply_unit_scale=True,
                apply_scale_options='FBX_SCALE_NONE',
                use_space_transform=True,
                bake_space_transform=False,
                object_types={'ARMATURE', 'CAMERA', 'EMPTY', 'LIGHT', 'MESH', 'OTHER'},
                use_mesh_modifiers=True,
                use_mesh_modifiers_render=True,
                mesh_smooth_type='OFF',
                use_subsurf=False,
                use_mesh_edges=False,
                use_tspace=False,
                use_custom_props=False,
                add_leaf_bones=False,
                primary_bone_axis='Y',
                secondary_bone_axis='X',
                use_armature_deform_only=False,
                armature_nodetype='NULL',
                bake_anim=False,
                bake_anim_use_all_bones=True,
                bake_anim_use_nla_strips=True,
                bake_anim_use_all_actions=True,
                bake_anim_force_startend_keying=True,
                bake_anim_step=1.0,
                bake_anim_simplify_factor=1.0,
                path_mode='AUTO',
                embed_textures=False,
                batch_mode='OFF',
                use_batch_own_dir=True,
                use_metadata=True,
                axis_forward='-Z',
                axis_up='Y'
                )

        return {"FINISHED"}
    
# Register all operators and panels    

#Define "ExportObj/FBX" menu
def export_menu(self, context):
  self.layout.operator("object.export_object")


def register():
    bpy.utils.register_class(ExportObject)
    # Add "ExportObj/FBX" menu to the "Object" menu
    bpy.types.TOPBAR_HT_upper_bar.append(export_menu)
        
def unregister():
    bpy.utils.unregister_class(ExportObject)
    bpy.types.TOPBAR_HT_upper_bar.append(export_menu)
    
if __name__ == "__main__":
    register()
