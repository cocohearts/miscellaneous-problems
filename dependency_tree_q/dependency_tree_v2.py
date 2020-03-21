# using just a dictionary

def insert(list_tuples):
    our_dict = {}
    for pair in list_tuples:
        parent_key = pair[0]
        child_key = pair[1]
        if not child_key in our_dict:
            our_dict[child_key] = set([])
        if parent_key in our_dict:
            our_dict[parent_key].add(child_key)
        else:
            our_dict[parent_key] = set([child_key])
    return our_dict

def descendants(our_dict,key):
    out_list = set([key])
    visited = set([])
    recursive_descendants(our_dict,out_list,key,visited)
    return out_list

def recursive_descendants(our_dict,out_list,key,visited):
    if not key in visited:
        out_list.add(key)
        visited.add(key)
        for child in our_dict[key]:
            recursive_descendants(our_dict,out_list,child,visited)

def solve_problem(list_tuple,list_questions):
    my_dict = insert(list_tuple)
    our_list = []
    for question in list_questions:
        our_list.append(question[1] in descendants(my_dict,question[0]))
    return our_list