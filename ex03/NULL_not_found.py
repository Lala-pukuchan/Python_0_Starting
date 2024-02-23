import math


def NULL_not_found(object: any) -> int:
    if object is None:
        print(object, type(object))
        return 0
    elif isinstance(object, float) and math.isnan(object):
        print(object, type(object))
        return 0
    elif isinstance(object, int) and object == 0:
        print(object, type(object))
        return 0
    elif isinstance(object, str) and object == "":
        print(object, type(object))
        return 0
    else:
        print("Type not Found")
        return 1
