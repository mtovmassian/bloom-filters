import time
import sys
from lib import BloomFilters


FIFTY_THOUSAND_WORDS = []
with open("./static/58110_words.txt", "r") as fifty_thousand_words_file:
    FIFTY_THOUSAND_WORDS = fifty_thousand_words_file.read().splitlines()

WORD_TO_CHECK = "hardis"

bf = BloomFilters.from_list(FIFTY_THOUSAND_WORDS, 0.05)


def test_for_loop() -> float:
    for_loop_proc_start = time.time()
    for word in FIFTY_THOUSAND_WORDS:
        if word == WORD_TO_CHECK:
            break
    for_loop_proc_end = time.time()

    return for_loop_proc_end - for_loop_proc_start


def test_in_operator() -> float:
    in_operator_proc_start = time.time()
    _ = WORD_TO_CHECK in FIFTY_THOUSAND_WORDS
    in_operator_proc_end = time.time()

    return in_operator_proc_end - in_operator_proc_start


def test_bloom_filters() -> float:
    bloom_filters_proc_start = time.time()
    _ = bf.contains(WORD_TO_CHECK)
    bloom_filters_proc_end = time.time()

    return bloom_filters_proc_end - bloom_filters_proc_start


def perf():
    for_loop_proc_time = test_for_loop()
    in_operator_proc_time = test_in_operator()
    bloom_filters_proc_time = test_bloom_filters()

    FIFTY_THOUSAND_WORDS_size = sys.getsizeof(FIFTY_THOUSAND_WORDS)
    bf_bit_field_size = sys.getsizeof(bf.bit_field)

    print("MEMORY USAGE\n============")
    print(
        "FIFTY_THOUSAND_WORDS list size:"
        + f"\n|___{FIFTY_THOUSAND_WORDS_size} bytes"
    )
    print(
        "Bloom filters size: "
        + f"\n|___{bf_bit_field_size} bytes"
    )

    print("\nSEARCH\n======")
    print(
        f"Checking word \"{WORD_TO_CHECK}\" "
        + f"with for loop:\n|____{for_loop_proc_time} ms"
    )
    print(
        f"Checking word \"{WORD_TO_CHECK}\" "
        + f"with 'in' operator:\n|____{in_operator_proc_time} ms"
    )
    print(
        f"Checking word \"{WORD_TO_CHECK}\" "
        + f"with Bloom filters:\n|____{bloom_filters_proc_time} ms"
    )
    print("\n")
    print(
        "Bloom filters are:\n"
        + f"- {FIFTY_THOUSAND_WORDS_size / bf_bit_field_size:.0f}"
        + " times memory efficient\n"
        + f"- {for_loop_proc_time / bloom_filters_proc_time:.0f} "
        + "times faster than for loop\n"
        f"- {in_operator_proc_time / bloom_filters_proc_time:.0f} "
        + "times faster than 'in' operator (Boyer-Moore algorithm)"
    )
    print("\n")


if __name__ == "__main__":
    perf()