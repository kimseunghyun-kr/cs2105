import zlib

s = "1dKy9H"
hash_value = zlib.crc32(s.encode('utf-8')) & 0xffffffff 
print(hex(hash_value))