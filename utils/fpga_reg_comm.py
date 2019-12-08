#!/usr/bin/env python3
#
# Author: Yipeng Sun
# License: BSD 2-clause
# Last Change: Sun Dec 08, 2019 at 02:37 AM -0500

import pydim

from platform import node

PREFIX = 'Gbt/{}/'.format(node())


def cmnd(name, cmd, dev='TELL40_Dev1_0.top_tell40'):
    pydim.dic_sync_cmnd_service(PREFIX+'CmndOperation/'+dev+'.'+name, cmd)


def srvc(name, srvc='SrvcReadings/', dev='TELL40_Dev1_0.top_tell40'):
    return pydim.dic_sync_info_service(PREFIX+srvc+dev+'.'+name)


def decode(ret):
    if isinstance(bytes, ret[1]):
        return [hex(i) for i in ret[1]]
    elif isinstance(str, ret[1]):
        return [ord(i) for i in ret[1]]
