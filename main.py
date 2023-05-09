from PyQt5.QtWidgets import QMainWindow, QApplication, QMenuBar, QLabel, QPushButton, QMenu, QAction, QSizePolicy, QFrame
from PyQt5.QtGui import QFont, QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import sys
import random
import chardet

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个新的 QFrame 对象
        frame = QFrame(self)

        # 设置 QFrame 的属性
        frame.setStyleSheet("background-color: #EDEDED; border-radius: 10px;")
        frame.setFrameShape(QFrame.Panel)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setGeometry(50, 50, 200, 200)

class TitleBar(QMenuBar):
    def __init__(self, parent=None, maxAction=None, minAction=None, closeAction=None):
        super().__init__(parent)
        self.maximizeAction = None
        self.maximizeButton = QPushButton("口")
        self.minimizeButton = QPushButton("一")
        self.closeButton = QPushButton("X")
        self.maximizeAction = maxAction
        self.minimizeAction = minAction
        self.closeAction = closeAction

    def initUI(self):
        self.setGeometry(0, 0, 400, 30)
        self.setStyleSheet("""
            QMenuBar {
                background-color: #2F4F4F;
                color: #F5F5F5;
                font-size: 14px;
            }

            QMenuBar::item {
                spacing: 3px;
                padding: 1px 4px;
                background-color: transparent;
            }

            QMenuBar::item:selected {
                background-color: #1E90FF;
            }

            QMenu {
                background-color: #F5F5F5;
                color: #333;
            }

            QMenu::item:selected {
                background-color: #1E90FF;
                color: #F5F5F5;
            }

            QMenu::separator {
                height: 1px;
                background-color: #ccc;
            }
        """)


        # create menus for the buttons
        self.minMenu = QMenu(self)
        self.maxMenu = QMenu(self)
        self.closeMenu = QMenu(self)

        # add the buttons to the menus
        self.minMenu.addAction(self.minimizeAction)
        self.maxMenu.addAction(self.maximizeAction)
        self.closeMenu.addAction(self.closeAction)

        # add the menus to the menu bar
        self.addMenu(self.minMenu)
        self.addMenu(self.maxMenu)
        self.addMenu(self.closeMenu)

    def toggleMaximized(self):
        if self.parent.isMaximized():
            self.parent.showNormal()
        else:
            self.parent.showMaximized()



class RoundedWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建最大化、最小化和关闭按钮
        self.maximizeAction = QAction("口", self)
        self.minimizeAction = QAction("一", self)
        self.closeAction = QAction("X", self)

        self.setGeometry(100, 100, 400, 200)
        self.setMinimumSize(300, 150)
        self.setMaximumSize(600, 300)

        # 初始化TitleBar实例
        self.titleBar = TitleBar(self, self.maximizeAction, self.minimizeAction, self.closeAction)
        self.setMenuBar(self.titleBar)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F5F5F5;
            }
        """)

        # 设置最大化、最小化和关闭按钮的样式
        self.titleBar.maximizeButton.setObjectName("MaxButton")
        self.titleBar.minimizeButton.setObjectName("MinButton")
        self.titleBar.closeButton.setObjectName("CloseButton")
        self.titleBar.maximizeButton.setStyleSheet("#MaxButton{background-color:#2F4F4F;color:#F5F5F5}")
        self.titleBar.minimizeButton.setStyleSheet("#MinButton{background-color:#2F4F4F;color:#F5F5F5}")
        self.titleBar.closeButton.setStyleSheet("#CloseButton{background-color:#2F4F4F;color:#F5F5F5}")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        brush = QBrush(Qt.white)
        painter.setBrush(brush)

        pen = QPen(Qt.white)
        pen.setWidth(2)
        painter.setPen(pen)

        rect = self.rect().adjusted(1, 1, -1, -1)
        painter.drawRoundedRect(rect, 10, 10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('style.qss', 'rb') as f:
        result = chardet.detect(f.read())
    with open('style.qss', 'r', encoding=result['encoding']) as f:
        app.setStyleSheet(f.read())

    window = MyMainWindow()

    menu = ["鱼香肉丝", "宫保鸡丁", "红烧排骨", "麻婆豆腐", "水煮肉片", "土豆丝", "西红柿炒蛋", "青椒肉丝", "酸辣汤", "蛋炒饭"]

    window = RoundedWindow()
    label = QLabel("今天中午吃什么？", window)
    label.setFont(QFont("Arial", 16))
    label.setAlignment(Qt.AlignCenter)
    label.setWordWrap(True)
    label.setGeometry(20, 30, 360, 80)
    label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    button = QPushButton("点我选菜", window)
    button.move(150, 120)
    button.setObjectName("myButton")
    button.clicked.connect(lambda: label.setText("今天中午吃：" + random.choice(menu)))

    window.show()
    sys.exit(app.exec_())





