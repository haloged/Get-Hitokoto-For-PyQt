# 一言生成器 For PyQt

[English](https://github.com/haloged/get_hitokoto/blob/main/README_EN.md)

> [!CAUTION]
> 此版本为实验性版本，不保证功能能够正常使用。如需稳定版，请前往[普通仓库](https://github.com/haloged/get_hitokoto)

此版本不提供已编译版本，如需使用，请自行编译。
# 安装教程
## Windows
编译版本需要下载Python环境。

**如果您是第一次使用，您需执行4步，如不是第一次使用，只需执行第四步即可。**
1. 点击[这里](https://www.python.org/ftp/python/3.8.3/python-3.8.3-macosx10.9.pkg)下载并点击安装
2. 下载完成后，打开[这里](https://github.com/haloged/get_hitokoto/blob/main/gui.py),同时按下`Ctrl+Shift+S`,选择一个位置保存，记住这个位置。
3. 点按任务栏中的“搜索”图标 ，在搜索栏中键入“命令提示符”，然后点按“命令提示符”。在终端中输入`pip install openai PyQt5`。
4. 找到你第三步保存的位置，点击`gui.py`即可运行。爬取的一言文件将保存在`gui.py`同目录的`log.txt`中。

## MacOS
编译版本需要下载Python环境。

**如果您是第一次使用，您需执行4步，如不是第一次使用，只需执行第四步即可。**
1. 点击[这里](https://www.python.org/ftp/python/3.8.3/python-3.8.3-macosx10.9.pkg)下载并点击安装
2. 下载完成后，打开[这里](https://github.com/haloged/get_hitokoto/blob/main/gui.py),同时按下`Command+Shift+S`,选择一个位置保存，记住这个位置。
3. 点按程序坞中的“启动台”图标 ，在搜索栏中键入“终端”，然后点按“终端”。在终端中输入`pip install openai PyQt5`。
4. 找到你第三步保存的位置，点击`gui.py`即可运行。爬取的一言文件将保存在`gui.py`同目录的`log.txt`中。
## Linux
Linux版本需要下载Python环境
1. 查看当前python环境版本
```sh
python --version
```
2. 首先安装编译安装时需要的依赖包，编译python源码时，需要一些依赖包，一次安装完毕
```sh
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel
```
3. 根据需要下载对应的Python版本：
服务器下载较慢时，可以在官网下载到本地之后，再上传到服务器。
```sh
wget https://www.python.org/ftp/3.7.0/Python-3.7.2.tgz
```
4. 解压python安装包
```sh
cd opttar -zxvf Python-3.7.2.tgz
```
5. 新建一个python3的安装目录
```sh
mkdir -p /usr/local/python3
```
6. 编译安装
```sh
cd Python-3.7.2/./configure --prefix=/usr/local/python3make && make install
```
7. 添加软连接
```sh
ln -s /usr/local/python3/bin/python3 /usr/bin/python3ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```
8. 验证是否安装成功
```sh
python3 --versionpip -V
```
9. 打开[这里](https://github.com/haloged/get_hitokoto/blob/main/gui.py),选择一个位置保存，记住这个位置。
10. 打开终端，输入以下代码：
```sh
pip install openai PyQt5
```
11. 找到你第九步保存的位置，点击`gui.py`即可运行。爬取的一言文件将保存在`gui.py`同目录的`log.txt`中。
