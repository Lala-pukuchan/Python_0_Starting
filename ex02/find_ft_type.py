def all_thing_is_obj(object: any) -> int:
    if (isinstance(object, str)):
        print(f"{object} is in the kitchen : {type(object)}")
    elif (isinstance(object, int)):
        print("Type not found")
    elif (isinstance(object, list)):
        print(f"List: {type(object)}")
    elif (isinstance(object, tuple)):
        print(f"Tuple: {type(object)}")
    elif (isinstance(object, set)):
        print(f"Set: {type(object)}")
    elif (isinstance(object, dict)):
        print(f"Dict: {type(object)}")
    return 42
