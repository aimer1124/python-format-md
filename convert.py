import os
# -*- coding: UTF-8 -*-

def convert(sourceFile, targetFile):

    sourceFile = open(sourceFile, "r")
    targetFile = open(targetFile,"w")

    sourceFileList = sourceFile.readlines()

    sourceFileList.insert(0,"---\n")
    for line in sourceFileList:
        # print(line)
        if "thumbnail" in line:
            sourceFileList.remove(line)

    targetFile.writelines(sourceFileList)

    targetFile.close()
    sourceFile.close()

sourcePath = "/Users/yuanjie/Documents/blog/source/_posts/"
targetPath = "/Users/yuanjie/Documents/blogSite/content/posts/"

sourceFileList = os.listdir(sourcePath)

for fileName in sourceFileList:
    print("Convert file: " + fileName)
    target = "./target.md"

    convert(sourcePath + fileName, targetPath + fileName)