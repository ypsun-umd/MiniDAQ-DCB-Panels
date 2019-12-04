#!/usr/bin/env python3
#
# Author: Yipeng Sun
# License: BSD 2-clause
# Last Change: Wed Dec 04, 2019 at 03:31 AM -0500


#############
# Constants #
#############

GBT_PREF = 'Gbt'
GBT_SERV = 'UMDlab'


###########
# Helpers #
###########

def fill(s, max_len=128, char='\0'):
    if len(s) > max_len:
        raise ValueError('{} is longer than max length {}.'.format(s, max_len))
    else:
        return s.ljust(max_len, char)


def hex_pad(n):
    s = hex(n)[2:]
    if len(s) % 2 == 1:
        return '0'+s
    else:
        return s


def hex_rep(lst_of_num):
    return ''.join(map(hex_pad, lst_of_num))


#############################
# Regulate DIM input/output #
#############################

def hex_to_bytes(val):
    if len(val) % 2 == 1:
        val = '0'+val
    return bytes.fromhex(val)


def str_to_hex(val):
    if isinstance(val, int):
        return val
    elif isinstance(val, bytes):
        return hex_rep([int(c) for c in val])
    else:
        return hex_rep([int('{:2x}'.format(ord(c)), base=16) for c in val])


def default_dim_regulator(tp):
    return [str_to_hex(e) for e in tp]