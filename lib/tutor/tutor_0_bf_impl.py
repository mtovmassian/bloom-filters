from typing import List
import math
import mmh3
from bitarray import bitarray


class BloomFilters:

    def __init__(self, items_count: int, fp_prob: float):
        pass
        # self.fp_prob = fp_prob
        # self.size = self.get_size(items_count, fp_prob)
        # self.hash_count = self.get_hash_count(self.size, items_count)
        # self.bit_array = bitarray(self.size)
        # self.bit_array.setall(0)

    def add(self, item: str):
        pass

    def contains(self, item: str):
        pass

    def get_digest_index(self, item: any, seed: int) -> int:
        pass

    @staticmethod
    def get_size(n: int, p: float) -> int:
        pass

    @staticmethod
    def get_hash_count(m: int, n: int) -> int:
        pass
