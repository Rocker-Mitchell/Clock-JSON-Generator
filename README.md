# Clock-JSON-Generator
As of Minecraft Java Edition 1.12, resources have changed for items that animate based on game events, such as the clock and compass. Before the update, frames for these items were stored in a sprite sheet, and the game could support different length sprite sheets in custom resources, allowing variants of frame amounts. Following the update, frames are stored as separate image files, and the logic for event-driven animation is defined in JSON model files. While this adds options to redesign the animation in custom resources, the process of generating the model files manually can get confusing and tedious. This repository provides a tool in Python code to automate the model file generation for the clock item specifically.

## Material Background
The resources for clock frame textures are located in `assets/minecraft/textures/items`. The model resources are located in `assets/minecraft/models/item`.

The JSON model files encode what textures to use and when to display the textures. The game calls `clock.json` as the root data, and `clock.json` defines an overrides parameter for event-driven assignment of models. Following clock models are used in the overrides, and define textures to use.

The overrides are a list of overrides. Each override defines a time and a model. The time can be set between 0 (inclusively) and 1 (exclusively). The time is reflected in game as starting at noon (time = 0) and moves through a cycle (counting up to 1). The general practice is to have the first override start at time = 0 and count upward following it. Multiple assignments of a model are allowed, while multiple assignments of time are not.

## Getting Started
The tool requres a user made module to be implemented and named `usercode.py`. Two parameters are needed from the module:

* `frameList` is a list of file names. The names should be exactly like the texture names, but excluding the extention (.png). The names are used to reference the texture names and to assign names to sub model files.

* `index2Time` is a function to map items in `frameList` to times. General requirements of the function are that it returns 0 for the first index, it doesn't return a value greater than 1 for any input between 0 and the maximum index, and a proportional relationship is observed between the index and time. The function signature should be:
```
def index2Time(index: int) -> float:
```

Samples of user made modules are available in the project as examples and templates. To run these modules, it is suggested to implement `usercode.py` as:
```
import name_usercode

frameList = name_usercode.frameList

def index2Time(index: int) -> float:
    return name_usercode.index2Time(index)
```
where `name_usercode` is the name of the module to run.

## Running the Tool
After `usercode.py` is implemented, run `clock_json_generator.py`, and a dicrectory named `output` will be created, containing all JSON files generated. All JSON files can be moved to `assets/minecraft/models/item` in a resource pack, and should work as long as the defined texture files are present in the resource pack.
