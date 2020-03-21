# python-format-md
为什么做这个：需要把原来的文章内容从[Hexo](hexo.io/)转移至[Hugo](https://gohugo.io/)，但两者在MD文件头部处理不一致。

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
- 

Format markdown file

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

- Issue: Can't do change together
- 
## 参考
- 文件读写: [https://www.runoob.com/python/python-files-io.html](https://www.runoob.com/python/python-files-io.html)
