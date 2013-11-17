def dict_to_list(dict_,nodes):
    for key in dict_.iterkeys():
        nodes.append(key)
        dict_to_list(dict_[key],nodes)