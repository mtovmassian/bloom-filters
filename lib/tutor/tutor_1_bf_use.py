from lib import BloomFilters

FALSE_POSITIVE_PROB = 0.05

words = [
    "abound", "abounds", "abundance", "abundant", "accessable",
    "bloom", "blossom", "bolster", "bonny", "bonus", "bonuses",
    "coherent", "cohesive", "colorful", "comely", "comfort",
    "gems", "generosity", "generous", "generously", "genial"
]


words_len = len(words)

bf = BloomFilters(words_len, FALSE_POSITIVE_PROB)

"""STEP 1"""
# print(f"Number of items: {words_len}")
# print(f"False positive ratio: {FALSE_POSITIVE_PROB}")
# print(f"Bitarray size: {bf.size}")
# print(f"Number of hash functions to use: {bf.hash_count}")
# print(bf.bit_array)

"""STEP 2"""
# bf.add(words[0])
# print(bf.bit_array)

"""STEP 3"""
# for word in words:
#     bf.add(word)
# print(bf.bit_array)

"""STEP 4"""
# print(bf.contains("genial"))
# print(bf.contains("hardis"))
