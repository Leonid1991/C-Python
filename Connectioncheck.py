import os
import ctypes

# Get the current script's directory
current_directory = os.path.dirname(os.path.realpath(__file__))  # Current folder
cpp_library = os.path.join(current_directory, "ConnectionCheck/ConnectionCheck")

handle = ctypes.CDLL(cpp_library+"/funclib.dll")

handle.Function.argtypes = [ctypes.c_int, ctypes.c_int]
handle.Function.restype = ctypes.c_int

def Function(a, b):
    return handle.Function(a, b)


print(Function(100, 200))    