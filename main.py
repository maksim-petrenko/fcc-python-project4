# https://www.freecodecamp.org/
# Curriculum: Python Certification
# Project: Build a Hash Table
# Copyright (C) 2026 Maksim Petrenko


########################################################################
# Class

class HashTable:

    def __init__(self) -> None:
        self.collection = {}

    def hash(self, key: str) -> int:
        return sum(map(ord, key))

    def add(self, key: str, value: str) -> None:
        hash_value = self.hash(key)
        if hash_value not in self.collection:
            self.collection[hash_value] = {}
        self.collection[hash_value].update({key: value})

    def remove(self, key: str) -> None:
        hash_value = self.hash(key)
        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                del self.collection[hash_value][key]

    def lookup(self, key: str) -> str:
        hash_value = self.hash(key)
        if hash_value in self.collection:
            return self.collection[hash_value].get(key)
