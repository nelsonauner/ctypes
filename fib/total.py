#!/usr/bin/env python
import numpy as np
import ctypes
_libfib=ctypes.CDLL('./_fib.so')
_totalLib = ctypes.CDLL('./_total.so')
def ctypes_totalCtypes(arr,n):
	return _totalLib.total(arr.ctypes.data_as(ctypes.c_void_p),n)
def ctypes_fib(a):
	return _libfib.fib(ctypes.c_int(a))

def totalPython(arr):
	count = 0
	for i in range(len(arr)):
		count +=arr[i]
	return count

def totalNumpy(arr):
	return np.sum(arr)
