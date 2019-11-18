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
# print("STEP 1\n======")
# print(f"Number of items: {words_len}")
# print(f"False positive ratio: {FALSE_POSITIVE_PROB}")
# print(f"Bit filed size: {bf.size}")
# print(f"Number of hash functions to use: {bf.hash_count}")
# print(bf.bit_field)

"""STEP 2"""
# print("\nSTEP 2\n======")
# bf.add(words[0])
# print(bf.bit_field)

"""STEP 3"""
# print("\nSTEP 3\n======")
# for word in words[1:]:
#     bf.add(word)
# print(bf.bit_field)

"""STEP 4"""
# print("\nSTEP 4\n======")
# print(f"Contains \"genial\": {bf.contains('genial')}")
# print(f"Contains \"hardis\": {bf.contains('hardis')}")
