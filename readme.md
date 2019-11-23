# tensorflow
## 安装：使用pip安装，需更换清华的源，速度快。

- 在user文件夹下新建pip。新建pip.ini文件，写入
- [global]
- timeout = 6000 
- index-url = https://pypi.tuna.tsinghua.edu.cn/simple 
- trusted-host = pypi.tuna.tsinghua.edu.cn 
- 然后使用pip install tensorflow即可






# OpenCV
## 色彩空间
RGB HSV HIS YCrCb yuv

##  H S V
使用hsv可以容易区分色彩

# 双线性模糊可以达到美颜的效果




# git使用说明

- git config --gobal user.name "" 配置姓名
- git config --gobal user.email   配置邮箱
- git init      在本地目录创建一个仓库
- git status 查看目录下文件的状态
- git add 添加文件，可以单独添加文件，也可以全部添加

一般情况下，我们总会有些文件不需要纳入Git 的管理，比如：

编译生成的中间文件、临时文件、可执行文件等等；
日志文件
……
解决方法：在工作目录下创建一个名为.gitignore的文件来列出忽略文件的模式。

文件.gitignore的格式规范如下：

所有空行或者以#开头的行会被Git忽略；
可以使用标准的glob模式匹配；
匹配模式可以以（/）开头防止递归；
匹配模式可以以（/）结尾指定目录；
要忽略指定模式以外的文件或目录，可以在模式前加（!）表示取反；


- git log查看提交记录
- git reset --hard <> 滚动到指定版本号
