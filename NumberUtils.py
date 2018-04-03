import sys

# params only support string

# decimal number system conversion
def dec_2_bin(dec):
    return '{0:b}'.format(int(dec))

def dec_2_oct(dec):
    return '{0:o}'.format(int(dec))

def dec_2_hex(dec):
    return '{0:x}'.format(int(dec)).upper()


# binary number system conversion
def bin_2_oct(bin):
    return dec_2_oct(bin_2_dec(bin))

def bin_2_dec(bin):
    return int(bin ,2)

def bin_2_hex(bin):
    return dec_2_hex(bin_2_dec(bin))


# octonary number system conversion
def oct_2_bin(oct):
    return dec_2_bin(oct_2_dec(oct))

def oct_2_dec(oct):
    return int(oct,8)

def oct_2_hex(oct):
    return dec_2_hex(oct_2_dec(oct))


# hexadecimal number system conversion
def hex_2_bin(hex):
    return dec_2_bin(hex_2_dec(hex))

def hex_2_oct(hex):
    return dec_2_oct(hex_2_dec(hex))

def hex_2_dec(hex):
    return int(hex,16)

