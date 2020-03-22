# python-format-md

为什么做这个：
把原来博客的文章从[Hexo](hexo.io/)转移至[Hugo](https://gohugo.io/)，但两者在MD文件头部处理不一致。

- Hexo格式

```
title: 'Http-Header'
tags:
  - API测试
  - SuperTest
categories:
  - Tool
date: 2016-02-29 20:14:00
thumbnail: /img/a.png
---
```

- Hugo格式 

```
---
title: 'Http-Header'
tags:
  - API测试
  - SuperTest
categories:
  - Tool
date: 2016-02-29 20:14:00
---
```

暂时发现，需要处理的内容有两处：
- 在文件首行添加`---`
- 删除MD文件Header中的`thumbnail`字段

## ToDo

- [X] Read MD file content
    - [X] Create source MD file
    - [X] Create covert file
    - [X] Read MD file
- [X] Save the change to MD file
    - [X] Make Change to the MD file
    - [X] Save the change to `New` file
- [X] Add `---` to the first line of the MD file
- [X] Delete `thumbnail` in the file format
    - [X] Find `thumbnail` line
    - [X] Delete the line
- [ ] Batch to update MD files in the `folder`
    - [ ] read the list in the `folder`
    - [ ] make the convert to the file in the list
    - [ ] save the new file to the new `folder`

## Day by Day

### Day 1

- Set source md file, `source.md`
- Create `convert.py` as convert controller
- Use `open(file, "r").read()` to get MD file content

### Day 2

- Make Change and save to new MD file
- Add `---` to new MD file
- Delete the line with `thumbnail`

```
lines = (i for i in sourceFile if 'thumbnail' not in i )
targetFile.writelines(lines)
```

- Use `readlines` to convert file: `list.insert(index,obj)` for add `---` and `list.remove(obj)` for delete `thumbnail`

```
sourceFileList = sourceFile.readlines()

sourceFileList.insert(0,"---\n")
for line in sourceFileList:
    print(line)
    if "thumbnail" in line:
        sourceFileList.remove(line)

targetFile.writelines(sourceFileList)

```


## 参考
- 文件读写: [https://www.runoob.com/python/python-files-io.html](https://www.runoob.com/python/python-files-io.html)
- PythonList: [https://www.runoob.com/python/python-lists.html](https://www.runoob.com/python/python-lists.html)
