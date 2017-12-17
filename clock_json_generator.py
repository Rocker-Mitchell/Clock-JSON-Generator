"""Tool to generate JSON files that define clock animation.

This module contains a script that will generate JSON files. The files are
intendend to be used as resource model data for the clock in Minecraft. The
files will be added to an 'output' folder added in the same directory as this
module.

For modularity, this module imports from a user made module (usercode) to define
frames and times to encode. The module parameters frameList and index2Time are
expected to be implemented: frameList as a list of strings for the clock frame
file names (no extention) and index2Time as a function that takes in an integer
of an index for frameList and returns a float of a time. The time is expected to
be 0 for an index of 0, less than 1 for the largest index, and that the time is
proportional to the index.

Todo:
    * Implement JSON file attributes
    * Save files to output folder

"""

# Imports

import json
# user made module
from usercode import frameList, index2Time

# Functions

# Script

# initialize core dictionary

# populate list of overrides

# add override list to core dictionary

# save core dictionary to JSON

# generate and save model dictionaries
    # initialize dictionary
    
    # save dictionary to JSON
