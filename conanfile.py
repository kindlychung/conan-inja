#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class InjaConan(ConanFile):
    name = "inja"
    version = "1.0.999"
    url = "https://github.com/kindlychung/conan-inja"
    description = "A C++ template engine"
    license = "https://github.com/pantor/inja/blob/master/LICENSE"
    no_copy_source = True
    requires = "jsonformoderncpp/[~= 3.1]@vthiery/stable"

    def source(self):
        source_url = "https://github.com/pantor/inja"
        git = tools.Git(folder="inja")
        git.clone(source_url, "master")
        # Rename to "sources" is a convention to simplify later steps

    def package_id(self):
        self.info.header_only()

    def package(self):
        self.copy("inja.hpp", dst="include",
                  src="inja/src", keep_path=False)
