# -*- coding:utf-8 -*-
#@Time : 2020/4/27 下午5:32
#@Author: 手写
#@File : hashlib01.py

import hashlib


# ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512',
#                       'blake2b', 'blake2s',
#                       'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512',
#                       'shake_128', 'shake_256')
# print(hashlib.md5('hello world')) # TypeError: Unicode-objects must be encoded before hashing

hashStr = hashlib.md5('hello world'.encode('utf-8'))
print(hashStr)  # <md5 HASH object @ 0x108181550>

print(len(hashStr.hexdigest()), hashStr.hexdigest()) # 32 32 5eb63bbbe01eeed093cb22bb8f5acdc3


sha1 = hashlib.sha1('hello world'.encode('utf-8'))
sha1_r = sha1.hexdigest()
print(len(sha1_r), sha1_r) # 40 2aae6c35c94fcfb415dbe95f408b9ce91ee846ed

sha256 = hashlib.sha256('hello world'.encode('utf-8'))
sha256_r = sha256.hexdigest()
print(len(sha256_r), sha256_r) # 64 b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
