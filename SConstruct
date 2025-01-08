#!/usr/bin/env python
import os
import sys

env = Environment()

# Glob search through source files given a specific file type pattern
sources = Glob("src/*.cpp")

# You can use conandeps to get the information
# for all the dependencies.
conandeps = SConscript('build/SConscript_conandeps')
conan_flags = conandeps["conandeps"]

# Or use the name of the requirement if
# you only want the information about that one.
fmt_flags = conandeps["fmt"]

# set C++ standard to 11
env.Append(CXXFLAGS=['-std=c++11'])

# Merge flags with optional other predefined flags 
env.MergeFlags(conan_flags)

# Create a runnable program given the source files with all their dependencies
env.Program("helloworld", sources)
