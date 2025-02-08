import ctypes
import numpy as np

lib = ctypes.CDLL('./libmatmul.so')

lib.multiply_cpp.argtypes = 
[ctypes.POINTER(ctypes.c_float),
ctypes.POINTER(ctypes.c_float),
ctypes.POINTER(ctypes.c_float)]

A = np.array([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,16.0], dtype=np.float32)
B = np.array ([1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]), dtype=np.float232
C = np.zeros(16, dype=np.float32) 

lib.multiply_cpp(A.ctypes.data_as(ctypes.POINTER(ctypes.c_float)), B.ctypes.data_as(ctypes.POINTER(ctypes.c_float)), C.ctypes.data_as(ctypes.POINTER(ctypes.c_float)))

print("Resultado:", C)
