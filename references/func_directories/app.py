import os


def generate_directories(path):
    '''
    Signature:  Generator | String -> Tuples 
    Purpose:    Produce tuples, for each tuple that contains
                dirpath, dirnames, filesnames, from a given string
                acting as a parent directory path
    Stub:       generate_directories(path): return ()
    Tests:      below
    Template:   generate_directories(path):
                    ...path
    '''
    for entry in os.walk(path):
        yield entry
'''Test'''
print("Test: generate_directories(path)\n" + 20*'-')
path = './test'
for entry in generate_directories(path):
    print(entry)


def filter_directories(path):
    '''
    Signature:  String -> List
    Purpose:    Produce a list of entries, each entry is a tuple
                that contains dirpath, dirnames, filenames and
                has to satisfied 2 conditions: is dead-end
                (no sub-directory) and has files (filenames exist),
                from a given string acting as a parent directory path
    Stub:       filter_directories(path): return []
    Tests:      below
    Template:   filter_directories(path):
                    ... path
    '''
    entries = []
    for entry in generate_directories(path):
        if entry[1] == [] and entry[2]:
            # If this directory (entry) is dead-end (no sub-directory)
            # and has files (filenames exist)  then print this directory
            entries.append(entry)
    
    return entries
'''
Tests
'''
print("Test: filter_directories(path)\n" + 20*'-')
path = './test'
print(filter_directories(path))

