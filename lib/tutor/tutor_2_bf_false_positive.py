from pprint import pprint
from lib import BloomFilters

FALSE_POSITIVE_PROB = 0.05

words = [
    "abound", "abounds", "abundance", "abundant", "accessable",
    "bloom", "blossom", "bolster", "bonny", "bonus", "bonuses",
    "coherent", "cohesive", "colorful", "comely", "comfort",
    "gems", "generosity", "generous", "generously", "genial"
]

words_len = len(words)

bf = BloomFilters(words_len - 1, FALSE_POSITIVE_PROB)

for word in words:
    bf.add(word)

"""STEP 1"""
# print("STEP 1\n======")
# print(f"Contains \"twitter\": {bf.contains('twitter')}")

"""STEP 2"""
# print("\nSTEP 2\n======")
# word_digest_indexes = [
#   (bf.hash(word, seed), word)
#   for word in words
#   for seed in range(4)
# ]

# twitter_digest_indexes = [
#   (bf.hash("twitter", seed), "twitter")
#   for seed in range(4)
# ]

# print("twitter digest indexes:")
# pprint(sorted(twitter_digest_indexes, key=lambda x: x[0]), indent=4, width=50)
# print("\n")
# print("word digest indexes:")
# pprint(sorted(word_digest_indexes, key=lambda x: x[0]), indent=4)
