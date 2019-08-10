from conans import ConanFile, tools, CMake


class TestPackageConan(ConanFile):
    requires = "gcem/1.12.0@matt1795/stable"
    generators = "cmake_find_package"
    exports_sources = "*"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_folder)
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            self.run("./test_package")
