from conan import ConanFile

class ExampleRecipe(ConanFile):
    generators = "SConsDeps"

    def requirements(self):
        self.requires("fmt/11.0.2")
