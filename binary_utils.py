"""
Functions used for binary processing.
"""

import socket

def num2bytes(num, octet_num, overflow_escape=False) -> bytes:
    """
    Convert the number into the binary expression with 1 octet
    `octet_num` should usually be 1 or 2.
    """
    bit_num = 8*octet_num
    if not 0 <= num < 2**bit_num:
        if not overflow_escape:
            raise ValueError(f"The number {num} is not in the range 0-{2**bit_num-1}")
        num = num % (2**bit_num)  # Wrap around if out of range
    return num.to_bytes(octet_num, byteorder="big")

# # This part is annotated because there is a different definition with the same name in `basic_types.py`.
# def ip2bytes(ip) -> bytes:
#     """
#     Converts an IPv4 address from its dotted-decimal string format into a 4-byte binary representation.
#     """
#     return socket.inet_aton(ip)

def substitute(original, new_field, begin_byte_num) -> bytes:
    """
    Replace part of the original bytes with the substitute bytes starting at `begin_byte_num`.
    """
    if not 0 <= begin_byte_num <= len(original):
        raise ValueError(f"The length of {begin_byte_num} ({len(begin_byte_num)}) is out of range")

    return original[:begin_byte_num] + new_field + original[begin_byte_num + len(new_field):]

def bstr2bytes(bstr):
    """
    Convert a binary string into bytes
    """
    if len(bstr) % 8 != 0:
        raise ValueError("Binary string length must be a multiple of 8")
    if not is_binary_string(bstr):
        raise ValueError(f"The string must contain only 0 and 1 (your string: {bstr})")
    print(int(bstr[:8], 2))
    return b''.join(int(bstr[i:i+8], 2).to_bytes(1, byteorder="big") for i in range(0, len(bstr), 8))

def bytes2bstr(b:bytes):
    """
    Convert bytes into a binary string
    """
    return ''.join(f'{byte:08b}' for byte in b)

def bytes2num(b: bytes) -> int:
    """
    Convert bytes into a number.
    """
    return int.from_bytes(b, byteorder='big')

def is_binary_string(s):
    """
    Check if a python string contains only `0` and `1`.
    """
    return set(s).issubset({'0', '1'})
