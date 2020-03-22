# -*- coding: UTF-8 -*-

source = "./source.md"
target = "./target.md"

sourceFile = open(source, "r")
targetFile = open(target,"w")

sourceFileList = sourceFile.readlines()

sourceFileList.insert(0,"---\n")
for line in sourceFileList:
    print(line)
    if "thumbnail" in line:
        sourceFileList.remove(line)

targetFile.writelines(sourceFileList)

targetFile.close()
sourceFile.close()