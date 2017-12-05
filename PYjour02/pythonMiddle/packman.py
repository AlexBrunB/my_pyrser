#!/usr/bin/env python3

import struct

def ushort_uint(my_str):
    my_arr = struct.unpack('>HI', my_str)
    return my_arr

def buf2latin(my_str):
    my_length = struct.unpack('>H', my_str[0:2])[0]
    my_tmp = my_str[2:my_length + 2]
    my_tmp = my_tmp.decode("latin-1")
    return my_length, my_tmp

def ascii2buf(*args):
    my_size = len(args)
    my_arr = bytearray(struct.pack('>I', my_size)) 
    for x in args:
        my_arr += struct.pack('>H', len(x))
        for c in x:
            my_arr += struct.pack('c', c.encode("utf-8"))
    return my_arr
    
