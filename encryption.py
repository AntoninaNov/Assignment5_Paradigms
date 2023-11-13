import ctypes
import os


# Load the dynamic library
def load_dynamic_library(lib_path):
    try:
        return ctypes.CDLL(lib_path)
    except OSError as e:
        print(f"Failed to load dynamic library: {e}")
        exit(1)


lib_path = '/Users/antoninanovak/CLionProjects/Assignment3_Paradigms/cmake-build-debug/libcaesar.dylib'
my_lib = load_dynamic_library(lib_path)


# Setting up the encryption and decryption functions
def setup_functions(lib):
    lib.encrypt.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
    lib.encrypt.restype = ctypes.c_char_p
    lib.decrypt.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
    lib.decrypt.restype = ctypes.c_char_p

setup_functions(my_lib)


# Encrypt function
def encrypt(text, key):
    try:
        encoded_text = text.encode()
        encrypted_text = my_lib.encrypt(encoded_text, key, len(text))
        return encrypted_text.decode()
    except (TypeError, ValueError, ctypes.ArgumentError) as e:
        print(f"Encryption error: {e}")
        return None


# Decrypt function
def decrypt(text, key):
    try:
        encoded_text = text.encode()
        decrypted_text = my_lib.decrypt(encoded_text, key, len(text))
        return decrypted_text.decode()
    except (TypeError, ValueError, ctypes.ArgumentError) as e:
        print(f"Decryption error: {e}")
        return None
