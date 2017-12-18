"""User made module that generates vanilla resources.

This module implements a user made module that generates functionally similar
JSON files to the default/vanilla resources.

The default resources have 64 unique frames. There is a linear relationship
between the frames and time, so the linear slope can be deduced as 1/64. The
default resources offset the frame times so the first frame doesn't start
exactly at time 0, but before it enough so the middle of the duration of the
first frame shows at time 0. This allows frames such as exactly noon to display
at noon while covering a difference before and after noon. Since this offset
would be negative, the first frame is applied to the start of the frame list and
mapped to time 0 to model the middle of the first frame's duration, and the
first frame is applied to the end of the frame list to model the start of the
first frame.

"""

frameList = [] # a later function and script initializes frameList
"""list(str): list of clock frame file names (no extention).
"""

# Functions

def index2Time(index: int) -> float:
    """Converts an index from frameList to a time.
    
    Args:
        index: An index. The value is expected to be between 0 (inclusive) and
            the length of frameList (exclusive).
    
    Returns:
        A time that is mapped to the index. The value is expected to be 0 for
        index = 0, to be less than 1 for the maximum index, and to be
        proportional to the index.
    
    """
    # the main linear function shifts below 0, so force time 0 on index 0
    if index is 0:
        return 0.0
    
    # most of the frames follow a linear function
    # slope is 1 (time) over 64 (number of unique frames)
    # the y intercept is minus half the slope
    return (1/64) * index - (1/64)/2

def populateFrameList():
    """Helper function to populate frameList.
    
    The format is 'clock_' followed by two digits. The digits count from '00' to
    '63' then follow with '00' again.
    
    """
    # first digit for loop
    for x in range(0,7):
        # second digit for loop
        for y in range(0,10):
            frameList.append("clock_" + str(x) + str(y))
            if x is 6 and y is 3:
                # stop loop
                break
        if x is 6 and y is 3:
            # stop loop
            break
    
    # append first frame
    frameList.append("clock_00")

# Script

# initialize frameList
populateFrameList()
