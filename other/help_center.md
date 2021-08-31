### 调查将doc/docx转换为html/Markdown的工具
1. 目前已经使用win32com, PyDoc, html2text可以实现这个功能
2. 问题
    - 转换结果不是很好看，表格和代码太丑了
    - 文档的首页没有处理
3. 步骤：
    - [Python将DOCX转换为markdown文件](https://blog.csdn.net/weixin_43431593/article/details/105185702)
    - [如何利用python将.doc文件转换为.docx文件](https://blog.csdn.net/xtfge0915/article/details/83541965)
    - [安装win32com](https://blog.csdn.net/a15986714591/article/details/78181034?locationNum=1&fps=1)
4. 使用系统工具unoconv pandoc
5. 问题
    - html的结果仍然不美观
    - html2markdown更丑了
6. docx2html
    - 这个包安不上去
    - 因为他的依赖包pillow是用python2写的？
7. pypandoc
    - 依赖pandoc，但是pandoc win安不上，Centos 安不上高版本的
8. mammoth
    - 功能太单一了，而且效果也不好
9. 尝试安装pandoc的高版本