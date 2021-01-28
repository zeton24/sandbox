from copy import copy, deepcopy

print('\n| Default python copy |\n')
a = [1,2,3]
print(f"a before: {a}")
c = a
c += [4,5]
print(f"c: {c}")
print(f"a after: {a}")
print(f"id a: {id(a)}") 
print(f"id c: {id(c)}")


print('\n\n| Shallow vs deep copy... |\n')
print(f"a before: {a}")
copy_a = copy(a)
deepcopy_a = deepcopy(a)
copy_a += [66]
deepcopy_a += [67]
print(f"a after: {a}")
print(f"shallow copy: {copy_a}")
print(f"deep copy: {deepcopy_a}")
print(f"copy id: {id(copy_a)}")
print(f"deepcopy id: {id(deepcopy_a)}")


print('\n\n| ...in nested arrays |\n')
array = [100,200,[0,1,2]]
print(f"{array}  -> array before changes")
copy_arr = copy(array)
deepcopy_arr = deepcopy(array)
copy_arr[0] = 105
copy_arr[2][1] = 3
deepcopy_arr[1] = 204
deepcopy_arr[2][2] = 8
print(f"{array} -> after changes")
print(f"{copy_arr} -> shallow copy")
print(f"{deepcopy_arr} -> deep copy")
print(f" org id: {id(array)}, nested: {id(array[2])}")
print(f"copy id: {id(copy_arr)}, nested: {id(copy_arr[2])}")
print(f"deepcopy id: {id(deepcopy_arr)}, nested: {id(deepcopy_arr[2])}")


print('\n\n| ...in nested dicts |\n')
dict1 = { 0: 'abc', 1:'xyz', 'nested': {2: 'qqq', 3: 'xxxx'}}
print(f"{dict1}  -> dict before changes")
copy_dict = copy(dict1)
deepcopy_dict = deepcopy(dict1)
copy_dict[0] = 'def'
copy_dict['nested'][2] = 'ppp'
deepcopy_dict[1] = 'zyx2'
deepcopy_dict['nested'][3] = 'yyy'
print(f"{dict1} -> after changes")
print(f"{copy_dict} -> shallow copy")
print(f"{deepcopy_dict} -> deep copy")
print(f"org id: {id(dict1)}, id_nested: {id(dict1['nested'])}")
print(f"copy id: {id(copy_dict)}, id_nested: {id(copy_dict['nested'])}")
print(f"deepcopy id: {id(deepcopy_dict)}, id_nested: {id(deepcopy_dict['nested'])}")


## pandas?
