def all_thing_is_obj(object: any) -> int:
    #your code here

    # Get the type of the object
    ObjectType = type(object)

    # Define a set of types (as in the subject example)
    type_names = {"list", "tuple", "set", "dict"}
    
    # Check if the object is a string to handle it like in the subject example
    if ObjectType.__name__ == "str":
        print(object, " is a string: <class 'str'>")
    # Check if the object is one of the specified types
    elif ObjectType.__name__ in type_names:
        print(f"{ObjectType.__name__.capitalize()}: {ObjectType}")
    else:
        print("Type not found")
    return 42
