"""Tool to generate JSON files that define clock animation.

This module contains a script that will generate JSON files. The files are
intendend to be used as resource model data for the clock in Minecraft. The
files will be saved to an 'output' folder added in the same directory as this
module.

For modularity, this module imports from a user made module (usercode) to define
frames and times to encode. The module parameters frameList and index2Time are
expected to be implemented: frameList as a list of strings for the clock frame
file names (no extention) and index2Time as a function that takes in an integer
of an index for frameList and returns a float of a time. The time is expected to
be 0 for an index of 0, less than 1 for the largest index, and that the time is
proportional to the index.

Todo:
    * Exception checking

"""

# Imports

import os
import json
# user made module
from usercode import frameList, index2Time

# Functions

def makeOverride(time: float, model: str):
    """Generate override dictionary.
    
    Args:
        time: The time value.
        model: The model file name (no extention).
    
    Returns:
        An override dictionary.
    
    """
    return {
        "predicate" : {
            "time" : time
            },
        "model" : "item/" + model
        }

# Script

# setup output directory
outputDirectory = "./output/"
if not os.path.exists(outputDirectory):
    os.makedirs(outputDirectory)

# initialize core dictionary
coreDict = {
    "parent" : "item/generated",
    "textures" : {
        "layer0" : "items/" + frameList[0]
        }
    }

# populate list of overrides
overridesList = []
# first override takes the core file's name
overridesList.append(makeOverride(index2Time(0), "clock"))
for index in range(1, len(frameList)):
    model = frameList[index]
    # if first frame occurs again, modify frame name
    if model == frameList[0]:
        model = "clock"
    overridesList.append(makeOverride(index2Time(index), model))

# add override list to core dictionary
coreDict["overrides"] = overridesList

# save core dictionary to JSON
with open(outputDirectory + "clock.json", "w") as outFile:
    json.dump(coreDict, outFile, indent=4)

# format frameList to a set, removing first frame
frameSet = set(frameList) - set(frameList[0:1])

# generate and save model dictionaries
for texture in frameSet:
    # initialize dictionary
    modelDict = {
        "parent" : "item/generated",
        "textures" : {
            "layer0" : "items/" + texture
            }
        }
    
    # save dictionary to JSON
    with open(outputDirectory + texture + ".json", "w") as outFile:
        json.dump(modelDict, outFile, indent=4)
