# pyfasm
Python wrapper for FASM

This wrapper **only works with python x86** as fasm.dll as been compiled for x86. Feel free to contribute if you want x64 support.

## Using pyfasm

```python
import pyfasm

# some inline asm which does nothing just to show how the library works
# __asm as to be bytes.
__asm = b"""
    pushfd
    pushad
    popad
    popfd
"""
bytecode = pyfasm.assemble(__asm)
print(bytecode)

> b'f\x9cf`faf\x9d'
```
