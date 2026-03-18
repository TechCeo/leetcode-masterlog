from collections import defaultdict
from typing import List

# data = [('fruit', 'apple'), ('fruit', 'banana'), ('animal', 'dog'), ('animal', 'cat')]
# grouped_data = defaultdict(list)
# for key, value in data:
#     grouped_data[key].append(value) # No manual key check needed
# # grouped_data is defaultdict(list, {'fruit': ['apple', 'banana'], 'animal': ['dog', 'cat']})
# print(grouped_data)


from collections import defaultdict
def groupAnagrams(strs: List[str]) -> List[List[str]]:

    # result {act: [act, cat], hat: [hat]}
    str_map = defaultdict(list)

    for word in strs:
        print(word)
        print(sorted(word))
        str_map[sorted(word)].append(word)
        
    print(str_map)

    return list(str_map.values())
    
# groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])
num_rep = [0] * 25
print(num_rep)
