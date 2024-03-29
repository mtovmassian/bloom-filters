from typing import List
import math
import mmh3
from bitarray import bitarray


class BloomFilters:

    def __init__(self, items_count: int, fp_prob: float):
        self.fp_prob = fp_prob
        self.size = self.get_size(items_count, fp_prob)
        self.hash_count = self.get_hash_count(self.size, items_count)
        self.bit_field = bitarray(self.size)
        self.bit_field.setall(0)

    def add(self, item: str):
        for i in range(self.hash_count):
            digest_index = self.hash(item, i)
            self.bit_field[digest_index] = True

        return self

    def contains(self, item: str):
        for i in range(self.hash_count):
            digest_index = self.hash(item, i)
            if self.bit_field[digest_index] is False:
                return False

        return True

    def hash(self, item: any, seed: int) -> int:
        return mmh3.hash(item, seed=seed) % self.size

    @classmethod
    def from_list(cls, items: List[str], fp_prob: float):
        items_count = len(items)
        bf = cls(items_count, fp_prob)
        for item in items:
            bf.add(item)

        return bf

    @staticmethod
    def get_size(items_count: int, fp_prob: float) -> int:
        m = -(items_count * math.log(fp_prob)) / (math.log(2) ** 2)

        return int(m)

    @staticmethod
    def get_hash_count(bf_size: int, items_count: int) -> int:
        k = (bf_size / items_count) * math.log(2)

        return int(k)
