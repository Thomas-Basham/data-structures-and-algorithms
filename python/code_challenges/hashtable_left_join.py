from data_structures.hashtable import Hashtable


"""
Arguments: two hash maps

    The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
    The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.

Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic
Input:
synonyms = {
    "diligent": "employed",
    "fond": "enamored",
    "guide": "usher",
    "outfit": "garb",
    "wrath": "anger",
}
antonyms = {
    "diligent": "idle",
    "fond": "averse",
    "guide": "follow",
    "flow": "jam",
    "wrath": "delight",
}
Output:
[
   ["fond", "enamored", "averse"],       synonym keys + values + matching key's antonym value
   ["wrath", "anger", "delight"],
   ["diligent", "employed", "idle"],
   ["outfit", "garb", NULL],
   ["guide", "usher","follow"]
]

"""


def left_join(synonyms, antonyms):
    ht = Hashtable()
    syn_ant_list = []
    ant_keys_list = antonyms.keys()
    for k, v in synonyms.items():
        ht.set(k, v)

    for k, v in antonyms.items():
        if ht.contains(k):
            syn_ant_list.append([k, (ht.get(k)), v])

    for k, v in synonyms.items():
        if k not in ant_keys_list:
            syn_ant_list.append([k, v, "NONE"])

    return syn_ant_list
