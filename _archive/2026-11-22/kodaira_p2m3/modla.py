import ctypes, numpy as np, os
_lib=ctypes.CDLL(os.path.join(os.path.dirname(os.path.abspath(__file__)),'libmodla.so'))
_lib.rref_mod.restype=ctypes.c_int
def rref(A,p):
    """A: 2D int array (any dtype) -> (RREF uint32 array, pivots list) mod p"""
    A=np.ascontiguousarray(np.mod(A,p).astype(np.uint32)); R,C=A.shape
    piv=np.zeros(min(R,C)+1,dtype=np.int32)
    r=_lib.rref_mod(A.ctypes.data_as(ctypes.c_void_p),R,C,ctypes.c_uint32(p),piv.ctypes.data_as(ctypes.c_void_p))
    return A[:r],list(piv[:r])
def rank(A,p): return len(rref(A,p)[1])
def nullspace(A,p):
    """basis (rows) of {x: A x = 0 mod p}"""
    Rm,piv=rref(A,p); C=A.shape[1]; free=[j for j in range(C) if j not in set(piv)]
    N=np.zeros((len(free),C),dtype=np.int64)
    for i,f in enumerate(free):
        N[i,f]=1
        for r,pc in enumerate(piv): N[i,pc]=(-int(Rm[r,f]))%p
    return N
