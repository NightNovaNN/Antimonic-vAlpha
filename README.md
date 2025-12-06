<h1>Antimonic Rendering Engine</h1>

<p>
  <img src="https://img.shields.io/badge/BUILD-PASSING-brightgreen?style=flat-square">
  <img src="https://img.shields.io/badge/LANGUAGE-C%20%7C%20C++%20%7C%20Fortran%20%7C%20Python-blue?style=flat-square">
  <img src="https://img.shields.io/badge/TYPE-Software%20Renderer-orange?style=flat-square">
  <img src="https://img.shields.io/badge/NO-GPU-lightgrey?style=flat-square">
</p>

Antimonic is a **low-level software rendering engine** built purely on CPU power.  
No OpenGL. No Vulkan. No DirectX.  
Just raw pixels being yeeted onto the screen.

This project exists to explore rendering fundamentals without hiding behind GPU abstractions.  
It’s tiny, fast, and hackable — perfect for learning graphics from the metal up.

---

## 🚀 Features

- CPU-only rendering pipeline
- Implementations in **C**, **C++**, **Fortran**, and bindings via **Python**
- Super modular header (`anm.h`)
- Multiple language entry points for experimentation
- Cross-platform: Windows, Linux, macOS
- Designed for teaching + small custom engines

---

## 📂 Project Structure

```sh
Antimonic/
│ LICENSE
│ MakeFile
│ README.md
│
└───src/
    ├── anm.h       # Core rendering header
    ├── main.c      # C implementation
    ├── main.cpp    # C++ implementation
    ├── main.f90    # Fortran implementation
    └── main.py     # Python bindings / control
```

---

## 🛠️ Build Instructions

### Using Make

```sh
make
```

Outputs will depend on the selected compiler in the MakeFile.

### Run

```sh
./antimonic
```

Or whichever executable your compiler outputs.

---

## 📜 License

This project is licensed under the terms stated in `LICENSE`.

---

## 🧪 Why Antimonic Exists

Because GPUs are cool, but understanding **how pixels actually get drawn** makes you unstoppable.
Antimonic gives you that “graphics from scratch” superpower.

---

## 💬 Contribute

Pull requests, optimizations, rewrites in cursed languages (COBOL renderer??),
everything is welcome.

---

## Portability

Antimonic ships with a fully cross-platform Makefile that works on:

- Windows (PowerShell / CMD)
- Linux
- macOS

The Makefile automatically detects your OS using `$(OS)` on Windows and `uname` on Unix-like systems.  
Based on the platform, it builds one of the following shared libraries:

- **Windows:** `antimonic.dll`
- **Linux:** `libantimonic.so`
- **macOS:** `libantimonic.dylib`

### When Make Works
Just run:
```sh
make
```
The Makefile handles:
- choosing the correct compilers (`gcc`, `g++`, `gfortran`)
- setting platform-specific flags  
- linking OS-specific libraries (like `gdi32` on Windows)
- bundling C, C++ and Fortran objects into one shared library

### If Make Fails
Some systems (especially Windows without MinGW/MSYS2) may not have a full Unix-style environment.  
If Make fails, try one of the following:

#### 1. Install a proper build environment
**Windows users** should install one of:
- MSYS2 (recommended)
- MinGW-w64
- Cygwin

Once installed, `make` should work correctly.

#### 2. Compile manually (fallback mode)
If you want to build everything yourself without Make:

##### C:
```
gcc -c src/main.c -o main_c.o -Wall -O2
```

##### C++:
```
g++ -c src/main.cpp -o main_cpp.o -Wall -O2
```

##### Fortran:
```
gfortran -c src/main.f90 -o main_f90.o
```

##### Link into a shared library (pick your OS):

**Windows (.dll):**
```
g++ -shared -o antimonic.dll main_c.o main_cpp.o main_f90.o -lgdi32 -lgfortran
```

**Linux (.so):**
```
g++ -shared -fPIC -o libantimonic.so main_c.o main_cpp.o main_f90.o -lgfortran -lm -ldl
```

**macOS (.dylib):**
```
g++ -shared -fPIC -o libantimonic.dylib main_c.o main_cpp.o main_f90.o -lgfortran -lm
```

This gives you the same output as `make`.

---

