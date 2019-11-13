import time
from lib import BloomFilters


FIFTY_THOUSAND_WORDS = []
with open("./static/58110_words.txt", "r") as fifty_thousand_words_file:
    FIFTY_THOUSAND_WORDS = fifty_thousand_words_file.read().splitlines()

WORD_TO_CHECK = "hardis"

bf = BloomFilters.from_list(FIFTY_THOUSAND_WORDS, 0.05)

in_operator_proc_start = time.time()
test = WORD_TO_CHECK in FIFTY_THOUSAND_WORDS
in_operator_proc_en = time.time()
in_operator_proc_time = in_operator_proc_en - in_operator_proc_start

bloom_filters_proc_start = time.time()
test = bf.check(WORD_TO_CHECK)
bloom_filters_proc_end = time.time()
bloom_filters_proc_time = bloom_filters_proc_end - bloom_filters_proc_start

print(
    f"Checking word \"{WORD_TO_CHECK}\" "
    + f"with 'in' operator: {in_operator_proc_time} ms"
)
print(
    f"Checking word \"{WORD_TO_CHECK}\" "
    + f"with Bloom filters: {bloom_filters_proc_time} ms"
)
print(
    f"Bloom filters are "
    + f"{in_operator_proc_time / bloom_filters_proc_time:.2f} "
    + f"times faster than 'in' operator"
)
