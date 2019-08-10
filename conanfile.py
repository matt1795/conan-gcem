from conans import ConanFile, CMake, tools


class GcemConan(ConanFile):
    name = "gcem"
    version = "1.12.0"
    license = "Apache-2.0"
    author = "Matthew Knight <mgk1795@gmail.com"
    url = "https://github.com/kthohr/gcem"
    homepage = "https://github.com/kthohr/gcem"
    description = "A C++ compile-time math library using generalized constant expressions"
    topics = ("math", "compile-time", "constexpr")
    generators = "cmake"
    
    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_folder)
        return cmake

    def source(self):
        git = tools.Git()
        git.clone(self.homepage, "v{}".format(self.version))

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
