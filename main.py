import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QRadioButton,QHBoxLayout,QAction,QMessageBox,QInputDialog
import os
import requests
import json
from PyQt5.QtCore import QThread
import time
import openai

# 装饰器，用于测量阻塞计时
def test_time(func1):
    def train(self):
        start_time = time.time()
        res = func1(self)
        end_time = time.time()
        print(end_time - start_time)
        # logger.info(f'the ocr parse time is {end_time-start_time} s')
        return res

    return train


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("一言生成器 For PyQt")
        self.setGeometry(100, 100, 400, 310)  # x, y, width, height

        self.label=QLabel('一言生成器',self)
        self.label.setGeometry(140,25,200,30)
        self.label.setStyleSheet('font-size: 30px; color: black;')
        
        
        # 创建按钮
        self.button = QPushButton("点击抓取", self)
        self.button.setGeometry(150, 150, 100, 30)
        self.button.clicked.connect(self.button_clicked)

        self.label1=QLabel('请选择抓取源:',self)
        self.label1.setGeometry(150, 180, 80, 30)


        self.btn0=QRadioButton('hitokoto.cn',self)
        self.btn0.setGeometry(150, 200, 90, 30)  # 设置具体位置
        #默认选中btn0
        self.btn0.setChecked(True)
        #toggled信号与槽函数绑定
        self.btn0.toggled.connect(lambda :self.btnstate(self.btn0))

        self.btn2 = QRadioButton('光环API',self)
        self.btn2.setGeometry(150, 220, 80, 30)  # 设置具体位置
        self.btn2.toggled.connect(lambda: self.btnstate(self.btn2))

        self.btn3 = QRadioButton('韩小韩API',self)
        self.btn3.setGeometry(150, 240, 80, 30)  # 设置具体位置
        self.btn3.toggled.connect(lambda: self.btnstate(self.btn3))

        self.btn4 = QRadioButton('ChatGPT(需自行提供API KEY)',self)
        self.btn4.setGeometry(150, 260, 200, 30)  # 设置具体位置
        self.btn4.toggled.connect(lambda: self.btnstate(self.btn4))

        self.btn5 = QRadioButton('DeepSeek(需自行提供API KEY)',self)
        self.btn5.setGeometry(150, 280, 200, 30)  # 设置具体位置
        self.btn5.toggled.connect(lambda: self.btnstate(self.btn5))

        self.create_menu_bar()

    def create_menu_bar(self):
        # 获取菜单栏
        menubar = self.menuBar()
        
        # 创建文件菜单
        file_menu = menubar.addMenu('文件(&F)')
        
        # 新建动作
        con_action = QAction('配置(&C)', self)
        con_action.setShortcut('Ctrl+Alt+C')
        con_action.setStatusTip('打开配置文件')
        con_action.triggered.connect(self.ope_config)
        file_menu.addAction(con_action)
        
        # 保存动作
        save_action = QAction('打开一言保存文件(&O)', self)
        save_action.setShortcut('Ctrl+Alt+O')
        save_action.setStatusTip('打开一言保存文件')
        save_action.triggered.connect(self.ope)
        file_menu.addAction(save_action)
        
        cal_action = QAction('清空一言保存文件(&L)', self)
        cal_action.setShortcut('Ctrl+Alt+L')
        cal_action.setStatusTip('清空一言保存文件')
        cal_action.triggered.connect(self.clean_hitokoto)
        file_menu.addAction(cal_action)
        
        zdy_action = QAction('自定义源', self)
        zdy_action.setStatusTip('自定义抓取源')
        zdy_action.triggered.connect(self.zdy)
        file_menu.addAction(zdy_action)

        # 添加分隔线
        file_menu.addSeparator()
        
        # 退出动作
        exit_action = QAction('退出(&Q)', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('退出应用程序')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # 创建编辑菜单
        edit_menu = menubar.addMenu('更多(&M)')
        
        opedoc_action = QAction('帮助文档', self)
        opedoc_action.triggered.connect(self.ope_help_doc)
        edit_menu.addAction(opedoc_action)
        
        paste_action = QAction('Github仓库', self)
        paste_action.triggered.connect(self.ope_github)
        edit_menu.addAction(paste_action)
        
        jcgx_action = QAction('检查更新', self)
        jcgx_action.triggered.connect(self.jcgx)
        edit_menu.addAction(jcgx_action)

        paste_action = QAction('关于', self)
        paste_action.triggered.connect(self.about)
        edit_menu.addAction(paste_action)

    # 菜单栏功能实现
    def ope_config(self):
        QMessageBox.information(self,"提示","QT版本暂未开发，如需使用请前往tkinter版本",QMessageBox.Yes,QMessageBox.Yes)
        
    def ope(self):
        os.system("log.txt")
        
    def clean_hitokoto(self):
        os.system("del log.txt")
        QMessageBox.information(self,"提示","删除成功",QMessageBox.Yes,QMessageBox.Yes)
    
    def zdy(self):
        QMessageBox.information(self,"提示","QT版本暂未开发，如需使用请前往tkinter版本",QMessageBox.Yes,QMessageBox.Yes)
    
    def ope_help_doc(self):
        os.system("start https://haloged-studio.feishu.cn/wiki/S554wi9cPiQi6yk1zhAcEEBfnjf")

    def jcgx(self):
        vertion=requests.get("https://tinywebdb.appinventor.space/api?user=haloged&secret=463de003&action=get&tag=bbh")
        vertion_jx=json.loads(vertion.text)
        bbh=vertion_jx["bbh"]
        print("当前最新版本："+bbh)
        if bbh=="1.1.0":
            QMessageBox.information(self,"提示","无更新",QMessageBox.Yes,QMessageBox.Yes)
        else:
            reply = QMessageBox.question(self,"提示","有新版本！\n点击“Yes”转到仓库",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
            print(reply)
            if reply==16384:
                os.system("start https://github.com/haloged/get_hitokoto/releases")
            else:
                pass

    @test_time
    def run(self):
        m = 0
        while True:
            time.sleep(2)  # 制造阻塞
            m += 1
            self.signal.emit(m)
            print('任务执行中')

    def refresh(self, m):
        self.main_win.line_edit.setText(str(m))

    def ope_github(self):
        os.system("start https://github.com/haloged/get_hitokoto")
    def about(self):
        QMessageBox.about(self,"关于软件","一言生成器 For PyQt\n作者：haloged\n软件版本：1.3.0\n作者B站：https://space.bilibili.com/518055250\nGithub仓库：https://github.com/haloged/get_hitokoto")
        

    def btnstate(self,btn):
    #输出按钮1与按钮2的状态，选中还是没选中
        if btn.text()=='Button1':
            if btn.isChecked()==True:
                print(btn.text()+"is selected")
            else:
                print(btn.text()+"is deselected")
        if btn.text()=="Button2":
            if btn.isChecked() == True:
                print(btn.text() + "is selected")
            else:
                print(btn.text() + "is deselected")

    def button_clicked(self):
        if self.btn0.isChecked():
            yuan=0
        elif self.btn2.isChecked():
            yuan=1
        elif self.btn3.isChecked():
            yuan=2
        elif self.btn4.isChecked():
            yuan=3
        elif self.btn5.isChecked():
            yuan=4
        run_num, ok = QInputDialog.getInt(self, "请输入运行次数", "运行次数", 1, 1, 1000)
        if not ok:  # 用户取消了输入
            return
        if yuan==0:
            with open("log.txt","a") as f:
                f.write("获取源：hitokoto.cn\n抓取次数："+str(run_num)+"\n\n")
            for i in range(run_num):
                hitokoto_jx={"hitokoto":"1"}
                hitokoto_get=requests.get("https://v1.hitokoto.cn")
                hitokoto_jx=json.loads(hitokoto_get.text)
                print(hitokoto_jx["hitokoto"])
                with open("log.txt","a") as f:
                    f.write(hitokoto_jx["hitokoto"]+"\n")
                time.sleep(2)
            with open("log.txt","a") as f:
                f.write("\n\n")
            QMessageBox.about(self,"提示软件","抓取成功！")

        elif yuan==1:
            with open("log.txt","a") as f:
                f.write("获取源：光环API\n抓取次数："+str(run_num)+"\n\n")
            for i in range(run_num):
                haloapi_jx={"txt":"1"}
                haloapi_get=requests.get("https://api.haloged.eu.org/")
                print(haloapi_get.text)
                with open("log.txt","a") as f:
                    f.write(haloapi_get.text+"\n")
                time.sleep(2)
            with open("log.txt","a") as f:
                f.write("\n\n")
            QMessageBox.about(self,"提示软件","抓取成功！")

        elif yuan==2:
            with open("log.txt","a") as f:
                f.write("获取源：韩小韩API\n抓取次数："+str(run_num)+"\n\n")
            for i in range(run_num):
                vvhan_get=requests.get("https://api.vvhan.com/api/ian/rand")
                print(vvhan_get.text)
                with open("log.txt","a") as f:
                    f.write(vvhan_get.text+"\n")
                time.sleep(2)
            with open("log.txt","a") as f:
                f.write("\n\n")
            QMessageBox.about(self,"提示软件","抓取成功！")

        elif yuan==3:
            with open("log.txt","a") as f:
                f.write("获取源：ChatGPT\n抓取次数："+str(run_num)+"\n\n")
            gpt_api_token= QInputDialog.getText(window, "请输入你的你的KEY", '请输入你的OPENAI API KEY')
            openai.api_key = os.getenv(gpt_api_token)
            response = openai.Completion.create(model="text-davinci-003", prompt="请生成"+run_num+"个关于励志的句子", temperature=0, max_tokens=1000)
            print(response)
            with open("log.txt","a") as f:
                f.write(response)
            with open("log.txt","a") as f:
                f.write("\n\n")
            QMessageBox.about(self,"提示软件","抓取成功！")

        elif yuan==4:
            with open("log.txt","a") as f:
                f.write("获取源：DeepSeek\n抓取次数："+str(run_num)+"\n\n")
            deepseek_api_token= QInputDialog.getText(window, "请输入你的你的KEY", '请输入你的DeepSeek API KEY')
            openai.api_key = os.getenv(deepseek_api_token)
            client = openai.OpenAI(api_key=os.getenv(deepseek_api_token), base_url="https://api.deepseek.com")
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant"},
                    {"role": "user", "content": "请生成"+run_num+"个关于励志的句子，直接给出"},
                ],
                stream=False
            )
            print(response.choices[0].message.content)
            with open("log.txt","a") as f:
                f.write(response.choices[0].message.content)
            with open("log.txt","a") as f:
                f.write("\n\n")
            QMessageBox.about(self,"提示软件","抓取成功！")
        @test_time
        def run(self):
            m = 0
            while True:
                time.sleep(2)  # 制造阻塞
                m += 1
                self.signal.emit(m)
                print('任务执行中')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())