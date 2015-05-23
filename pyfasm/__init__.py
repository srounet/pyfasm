# -*- coding: UTF-8 -*-
"""Python wrapper for fasm

Credits goes to Abyx for the initial python code version
http://board.flatassembler.net/topic.php?t=12105
"""

import struct
import ctypes
import os

import pyfasm.constants

__all__ = 'version', 'assemble'

try:
    dllpath = os.path.join(os.path.dirname(__file__), 'ressources\\fasm.dll')
    _fasm = ctypes.WinDLL(dllpath)
except:
    raise RuntimeError("PyFASM: can't locate fasm.dll")


def version():
    """Returns tuple (major version, minor version)"""
    verDW = _fasm.fasm_GetVersion()
    return verDW & 0xFFFF, verDW >> 16

def assemble(src, memorySize=0x10000, passesLimit=100):
    """Assembles string and returns assembled bytes"""
    buf = ctypes.create_string_buffer(memorySize)
    err = _fasm.fasm_Assemble(ctypes.c_char_p(src), buf, len(buf), passesLimit, 0)
    if err == pyfasm.constants.conditions['OK']:
        cb, addr = struct.unpack_from('II', buf, 4)
        ofs = addr - ctypes.addressof(buf)
        return buf[ofs:ofs + cb]
    if err != pyfasm.constants.conditions['ERROR']:
        raise RuntimeError('FASM error: ' + pyfasm.constants.conditions[err])
    cb, addr = struct.unpack_from('II', buf, 4)
    errCode, errLine = struct.unpack_from('iI', buf, 4)
    raise RuntimeError('FASM error: ' + pyfasm.constants.errorCodes[errCode])
