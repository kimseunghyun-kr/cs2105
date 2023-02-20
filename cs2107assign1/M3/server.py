#!/usr/bin/python3

from zlib import crc32
from random import randint
from os import getenv

range_max = 100000000000
print(f"I am going to generate a number between 1 and {range_max}")

hehe = randint(1, range_max)

findme = f"Hehe, my value is {hehe}"

print("I will not help you. I can only give this: " + hex(crc32(findme.encode())))

test = input("Can you achieve happiness >")

if crc32(test.encode()) == crc32(findme.encode()):
    print("Congratulations, you have attained nirvana: " + "CS2107{m1nd_th3_coll15i0n}")
else:
    print("Back to the abyss you go...")
