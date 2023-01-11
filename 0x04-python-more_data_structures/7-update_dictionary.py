def update_dictionary(a_dictionary, key, value):
    if not a_dictionary:
        return {key: value}
    a_dictionary[key] = value
    return a_dictionary 
