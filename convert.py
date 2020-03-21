# -*- coding: UTF-8 -*-

source = "./source.md"
target = "./target.md"

sourceFile = open(source, "r")
targetFile = open(target,"w")

targetFile.write("---\n" + sourceFile.read())


targetFile.close()
sourceFile.close()