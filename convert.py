# -*- coding: UTF-8 -*-

source = "./source.md"
target = "./target.md"

sourceFile = open(source, "r")
targetFile = open(target,"w")

# targetFile.write("---\n" + sourceFile.read())

lines = (i for i in sourceFile if 'thumbnail' not in i )

targetFile.writelines(lines)

targetFile.close()
sourceFile.close()