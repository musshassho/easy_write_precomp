#######################################################################################################################

__author__ = "Boris Martinez Castillo"
__version__ = "1.0.1"
__maintainer__ = "Boris Martinez Castillo"
__email__ = "boris.vfx@outlook.com"

########################################################################################################################

import nuke
import os


print "IMPORTING easy_write_precomp, NEW ONE "


# FUNCTION DEFINITIONS

def normalize_path(str):
    return os.path.normpath(str)

def from_script_to_precomp_path():
    script_path_norm = os.path.normpath(nuke.root()["name"].value())
    precomp_path = script_path_norm.replace("work", "renders")
    try:
        seq_name = precomp_path.split("\\")[8]
        shot_name = precomp_path.split("\\")[9]
        shot = seq_name + "_" + shot_name
        padding = 6 * "#"
        n = nuke.thisNode()
        name = n["fname"].value()
        extension = n["fformat"].value()
        if n["version_1"].value() == "":
            n["version_1"].setValue(str(1))
			
        version = int(n["version_1"].value())

        final_path = ("\\").join(precomp_path.split("\\")[:11]) + "\\" + "precomp" + "\\" + shot + "_" + name + "v" + str(version) + "\\" + shot + "_" + name + "v" + str(version) + "." + padding + "." + extension
        final_path1 = final_path.replace("\\", "/")

        nuke.thisNode()["file"].setValue(final_path1)
        nuke.thisNode()["version_1"].setValue(str(version + 1))
        #nuke.message("you are welcome")
		
        return final_path1
    except:
        nuke.message("This guy will only work if you render from a BB Nuke Script, sorry.")


