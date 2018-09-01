__author__ = 'logan.bender'

"""
import idanim.lib.id_paths as id_paths

name="generic_male"
asset_type="character"
subtype="humans" # note the plural s -must match existing folders
pathclass=id_paths.GhostPaths()

id_paths.create_asset_folders(pathclass,name,asset_type,subtype,include_animation=True, include_motion=True,
                        include_art=True, include_rigging=True, test=False)
"""


from ConfigParser import ConfigParser
from idanim.lib.path import Path
from idanim.lib.random_quote import random_quote

PROJECT_LIST = ["ghost", "zion"]


# TODO: get master rig, animation rig, md6rig t-pose script.
# TODO: get picker path

def read_config(config_path="W:/ghost/id_project_config.cfg"):
   config=ConfigParser()
   config.read(config_path)
   print "config file: ", config_path
   print "sections: ", config.sections()
   for section in config.sections():
       options=config.options(section)
       print options

def path_class_from_maya_workspace():
   import pymel.core as pm
   workspace_path = pm.workspace.getPath()
   path_class = None
   if 'zion' in workspace_path:
       path_class = ZionPaths
   if 'ghost' in workspace_path:
       path_class = GhostPaths
   if path_class == None:
       print 'id_paths.path_class_from_maya_workspace()\n\tcould not determine a path class. workspace_path = {}'.format(
           workspace_path)
   # print 'id_paths.path_class_from_maya_workspace({})'.format(path_class)
   return path_class


def get_path_class(scene_path):
   path_class = None
   if 'zion' in scene_path:
       path_class = ZionPaths
   if 'ghost' in scene_path:
       path_class = GhostPaths
   if path_class == None:
       print 'id_paths.get_path_class()\n\tcould not determine a path class for scene_path({})'.format(
           scene_path)
   # print 'id_paths.get_path_class({})'.format(path_class)
   return path_class


def stub_folders(path_list,test=False):
   for path in path_list:
       if test:
           print "stub_folder : {}".format(path)
       else:
           try:
               path.makedirs_p()
               stub = path.joinpath(".stub")
               print stub
               with open(stub, "w+") as f:
                   try:
                       f.write(random_quote())
                   except:
                       pass
                   pass
           except Exception as e:
               print e


def create_asset_folders(pathclass, name, asset_type, subtype, subsubtype, include_animation=True, include_motion=True,
                        include_art=True, include_rigging=True, test=False):
   if include_animation:
       create_animation_asset_folders(pathclass, name, asset_type, subtype, include_motion=include_motion,test=test)
   if include_art:
       create_art_asset_folders(pathclass, name, asset_type, subtype,test=test)
   if include_rigging:
       create_rigging_asset_folders(pathclass, name, asset_type, subtype,test=test)


def create_animation_asset_folders(pathclass, name, asset_type, subtype, include_motion=True,test=False):
   asset_root = pathclass.animation_source.joinpath(asset_type, subtype, name)
   path_list = []
   for path in pathclass.animation_asset_subfolders:
       path_list.append(asset_root.joinpath(path))
   if include_motion:
       for path in pathclass.animation_motion_subfolders:
           path_list.append(asset_root.joinpath(path))
   stub_folders(path_list, test=test)


def create_rigging_asset_folders(pathclass, name, asset_type, subtype,test=False):
   path_list = []
   rig_root = pathclass.rigging.joinpath(asset_type, subtype, name)
   rigging_subfolders = ['model','rigging/_master', 'rigging/wip/useful']
   for path in rigging_subfolders:
       path_list.append(rig_root.joinpath(path))
   stub_folders(path_list,test=test)


def create_art_asset_folders(pathclass, name, asset_type, subtype,test=False):
   asset_root = pathclass.art_source.joinpath(asset_type, subtype, name)
   path_list = []
   for path in pathclass.art_subfolders:
       path_list.append(asset_root.joinpath(path))
   stub_folders(path_list,test=test)


def is_rigging(path):
   return "RIGGING" in path


def is_animation(path):
   return "animation" in path


def is_art(path):
   return "art" in path


def is_sound(path):
   return "sound" in path


def is_effect(path):
   return "effect" in path


def is_player(path):
   return "player" in path


def is_character(path):
   return "characters" in path


def is_weapon(path):
   return "weapons" in path


def is_syncentity(path):
   return "syncentities" in path


def is_rig(path):
   return "rig" in path


def is_mesh(path):
   return "mesh" in path


def is_motion(path):
   return "motion" in path


def is_md6mesh(path):
   return "md6mesh" in path


def is_md6skl(path):
   return "md6skl" in path


def is_md6mask(path):
   return "md6mask" in path


def is_md6def(path):
   return "md6def" in path


def is_animweb(path):
   return "animweb" in path.lower()


def is_entitydef(path):
   return "entitydef" in path.lower()


class ProjectPaths(object):
   '''
   a class to hold and manipulate project critical paths for a project
   '''
   # roots
   game = Path("C:/project/game/base")
   source = Path("C:/project/source/base")
   animtools = Path("W:/animation-pipeline")

   # departments
   animation_source = source.joinpath("animation")
   art_source = source.joinpath("art")
   rigging = Path("//id-vault/Animation/RIGGING/project/source/animation")
   animation_asset_subfolders = [
       'base/assets/mesh',
       'base/assets/rig',
   ]
   animation_motion_subfolders = [
       'base/motion/ambient',
       'base/motion/combat',
       'base/motion/death',
       'base/motion/pain',
       'base/motion/traversal',
   ]

   rigging_subfolders = ['_master', 'wip']
   art_subfolders = ['handoff', 'master', 'texture', 'wip']

   # data
   anim_data = Path(source + '/animation/data')

   # md6
   md6 = Path(game + "/md6")

   # decl roots
   decl = Path(game + "/declTree")
   animweb = Path(decl + "/animWeb/animweb")
   md6def = Path(decl + "/md6Def/md6def")
   entitydef = Path(decl + "/entityDef")

   # ai decls
   ai_entitydef = Path(entitydef + "/ai")
   ai_attachments = Path(entitydef + "/demon/AI_NAME/attachments/")
   ai_actor_population = Path(decl + "/actorPopulation/actorpopulation/default/default_complete.decl")

   # interact decls
   interact_animweb = Path(animweb + "/interact")
   interact_entitydef = Path(entitydef + "/interact")

   # cineractive  decls
   cineractive_animweb = Path(animweb + "/cineractive")
   cineractive_entitydef = Path(entitydef + "/cineractive")

   # cinematic  decls
   cinematic_animweb = Path(animweb + "/interact")
   cinematic_entitydef = Path(entitydef + "/interact")

   # syncmelee  decls
   syncmelee_animweb = Path(animweb + "/syncmelee")
   syncmelee_entitydef = Path(entitydef + "/syncmelee")
   syncmelee_interaction = Path(decl + "/syncInteractions")

   # player  decls
   player_md6def = Path("md6def/player/human/base/tp_body.md6")
   player_rig = Path(source + 'animation/player/human/base/assets/rig/marine.mb')

   # p4 configs
   p4config_source = Path('w:/ghost/source/p4config.txt')
   p4config_game = Path('w:/ghost/p4config.txt')


class GhostPaths(ProjectPaths):
   '''
   a class to hold and manipulate project critical paths for ghost
   '''

   game = Path("W:/ghost/game/base")
   source = Path("W:/ghost/source/base")
   animtools = Path("W:/animation-pipeline")

   # departments
   animation_source = source.joinpath("animation")
   art_source = source.joinpath("art")
   rigging = Path("//id-vault/Animation/RIGGING/ghost/")

   # data
   anim_data = Path(source + '/animation/data')

   # md6
   md6 = Path(game + "/md6")

   # decl roots
   decl = Path(game + "/declTree")
   animweb = Path(decl + "/animWeb/animweb")
   md6def = Path(decl + "/md6Def/md6def")
   entitydef = Path(decl + "/entityDef")

   # ai
   ai_entitydef = Path(entitydef + "/ai")
   ai_attachments = Path(entitydef + "/demon/AI_NAME/attachments/")
   ai_actor_population = Path(decl + "/actorPopulation/actorpopulation/default/default_complete.decl")

   # interact
   interact_animweb = Path(animweb + "/interact")
   interact_entitydef = Path(entitydef + "/interact")

   # cineractive
   cineractive_animweb = Path(animweb + "/cineractive")
   cineractive_entitydef = Path(entitydef + "/cineractive")

   # cinematic
   cinematic_animweb = Path(animweb + "/interact")
   cinematic_entitydef = Path(entitydef + "/interact")

   # syncmelee
   syncmelee_animweb = Path(animweb + "/syncmelee")
   syncmelee_entitydef = Path(entitydef + "/syncmelee")
   syncmelee_interaction = Path(decl + "/syncInteractions")

   # player
   player_md6def = Path("md6def/player/human/base/tp_body.md6")
   player_rig = Path(source + 'animation/player/human/base/assets/rig/marine.mb')

   # p4 configs
   p4config_source = Path('w:/ghost/source/p4config.txt')
   p4config_game = Path('w:/ghost/p4config.txt')


def create_prop_folders(prop_name):
   pathclass = GhostPaths()
   create_asset_folders(pathclass, prop_name,  "objects", "props", include_animation=True, include_motion=False,
                                 include_art=True, include_rigging=False, test=False)

# Test #######################################


def dotest():

   pathclass = GhostPaths
   create_asset_folders(pathclass, "bfg", "objects", "weapons",include_art=False,test=False)
   #todo:" allow for even more subtypes as in : create_asset_folders(pathclass, "bfg", ["objects", "weapons", "energey",] include_art=False,test=False)
# def dotest():
#     read_config()

if __name__ == "__main__":
   dotest()
   pass

