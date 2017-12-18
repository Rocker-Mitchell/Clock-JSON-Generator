"""Sample user made module to define frames and time.

This is an example of a user made module. It has frames named in frameList, and
index2Time maps time linearly to the size of frameList.

"""

frameList = [
    "clock_00",
    "clock_01",
    "clock_02",
    "clock_03"
    ]
"""list(str): list of clock frame file names (no extention).
"""

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
    # the slope is 1 (time) over number of frames (len(frameList)
    # the y intercept is 0, as required for the function behavior
    return (1/len(frameList)) * index
