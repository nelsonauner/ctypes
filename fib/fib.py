import ctypes

_libfib=ctypes.CDLL('./_fib.so')

_totalLib = ctypes.CDLL('./_total.so')
def ctypes_total(arr,n):
	return _totalLib.total(arr.ctypes.data_as(ctypes.c_void_p),n)

def ctypes_fib(a):
	return _libfib.fib(ctypes.c_int(a))
