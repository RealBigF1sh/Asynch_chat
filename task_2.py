import binascii

strs = [b'class', b'function', b'method']

for item in strs:
    print(type(item), binascii.hexlify(item), len(item))