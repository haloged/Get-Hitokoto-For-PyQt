# One Sentence Generator

[Chinese](https://github.com/haloged/Get-Hitokoto-For-PyQt/blob/main/README.md)

> [!CAUTION]
> This version is experimental and does not guarantee full functionality. For a stable release, please visit the [main repository](https://github.com/haloged/get_hitokoto)

# Installation Tutorial 
## Windows
The compiled version requires downloading the Python environment. 

If it's your first time using it, you need to follow 4 steps. If it's not your first time, you only need to follow the fourth step. **
1. Click [here](https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe) to download and click to install.

2. After the download is complete, open [here](https://github.com/haloged/Get-Hitokoto-For-PyQt/blob/main/main.py), press `Command+Shift+S` simultaneously, choose a location to save, and remember this location.

3. Click the "Launchpad" icon in the Dock, type "Terminal" in the search bar, and then click "Terminal". In the Terminal, enter `pip install openai`.

4. Find the location where you saved in the third step, click `main.py` to run. The crawled quotes file will be saved in `log.txt` in the same directory as `main.py`. 

## MacOS

The compiled version requires downloading the Python environment. 

If it's your first time using it, you need to follow 4 steps. If it's not your first time, you only need to follow the fourth step. **
1. Click [here](https://www.python.org/ftp/python/3.8.3/python-3.8.3-macosx10.9.pkg) to download and click to install.

2. After the download is complete, open [here](https://github.com/haloged/Get-Hitokoto-For-PyQt/blob/main/main.py), press `Command+Shift+S` simultaneously, choose a location to save, and remember this location.

3. Click the "Launchpad" icon in the Dock, type "Terminal" in the search bar, and then click "Terminal". In the Terminal, enter `pip install openai`.

4. Find the location where you saved in the third step, click `main.py` to run. The crawled quotes file will be saved in `log.txt` in the same directory as `main.py`. 
## Linux
For the Linux version, you need to download the Python environment.

1. Check the current Python environment version.
 ```sh
python --version
```

2. First, install the required dependency packages for compilation and installation. When compiling the Python source code, some dependency packages are needed, and they should be installed all at once.
 ```sh
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel
```

3. Download the corresponding Python version as needed:
When the server download is slow, you can download it to your local machine from the official website first and then upload it to the server. 
```sh
wget https://www.python.org/ftp/3.7.0/Python-3.7.2.tgz
```

4. Unzip the Python installation package ```sh
cd opttar -zxvf Python-3.7.2.tgz

5. Create a new installation directory for Python 3.
 ```sh
mkdir -p /usr/local/python3
```

6. Compilation and Installation 
```sh
cd Python-3.7.2/ && ./configure --prefix=/usr/local/python3 && make && make install
```

7. Add soft link
```sh
ln -s /usr/local/python3/bin/python3 /usr/bin/python3ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```
8. Verify whether the installation was successful.
 ```sh
python3 --versionpip -V
```

9. Open [here](https://github.com/haloged/Get-Hitokoto-For-PyQt/blob/main/main.py), choose a location to save it, and remember this location.

10. Open the terminal and enter the following code:
 ```sh
pip install openai
```

11. Locate the position you saved in Step 9, and click on `main.py` to run it. The crawled one-sentence files will be saved in `log.txt` in the same directory as `main.py`.