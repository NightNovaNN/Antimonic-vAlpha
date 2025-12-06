import ctypes
from time import sleep
import time 

# Load the Antimonic renderer DLL
ar = ctypes.CDLL("./antimonic.dll")

# Function signatures
ar.ar_init.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
ar.ar_clear.argtypes = [ctypes.c_uint32]
ar.ar_draw_rect.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint32]
ar.ar_present.argtypes = []

# Init window
ar.ar_init(800, 600, b"Antimonic Renderer Python Test")

start = time.perf_counter_ns()
ar.ar_clear(0x202020)        # Dark gray
ar.ar_draw_rect(100, 100, 64, 64, 0xFF0000)  # Red square
ar.ar_present()
end = time.perf_counter_ns()
print(f"Frame rendered in {(end - start) / 1_000_000} ms")
sleep(0.016)                 # ~60 FPS
