# Conan package manager library integration with scons
This project is an example on how libraries built via the conan package manager with the cmake build-system could be integrated into a C++ program built using the scons build-system. It is part of a blog post of mine explaining how to use the scons build-system either manually with cmake built libraries and package managers such as vcpkg and conan.

## Build requirements
- Conan
- Python
- SCons
- CMake
- C++ compiler

## Build instructions
1. Create a conan profile (Conan tries to guess a build configuration)
```sh
conan profile detect --force
```

This will give out something like this depending on your system:
```yml
detect_api: Found apple-clang 16.0
detect_api: apple-clang>=13, using the major as version

Detected profile:
[settings]
arch=armv8
build_type=Release
compiler=apple-clang
compiler.cppstd=gnu17
compiler.libcxx=libc++
compiler.version=16
os=Macos
```

2. In the root directory, install the libraries specified by the `conanfile.py` file (here the `fmt` library). The `--build` argument specifies that only the packages whose binaries are not found will be built from source by Conan. 
```sh
conan install . --output-folder=build --build=missing
```

2. Call `scons` to compile the program into the executable `helloworld`
```sh
scons
```

3. Run program (This may differ slightly on Windows)
```sh
./helloworld
```
