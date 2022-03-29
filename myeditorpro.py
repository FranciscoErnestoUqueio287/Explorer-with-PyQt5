from PyQt5.QtWidgets import QWidget ,QFrame, QPushButton,QLabel, QLineEdit,QScrollArea,QProgressBar,QComboBox, QTabWidget, QPlainTextEdit, QGridLayout , QCompleter, QMenu,QFormLayout, QDialogButtonBox, QFileDialog, QScrollBar
from PyQt5.Qt import QApplication, Qt, QAction, QThread, pyqtSignal #MouseButton
from PyQt5.QtCore import QStringListModel, QEvent, QFileInfo
from PyQt5.QtGui import QIcon, QMouseEvent ,QPixmap, QCursor, QImage, QBitmap
from subprocess import Popen
import pyperclip, psutil
from PIL import Image , ImageQt
#from PyQt5.QtCore import QAbstractItemModel
import sys,eyed3, time,os, pyperclip
from random import randint
from threading import Thread 
if "\\" in sys.argv[0]:
    os.chdir("\\".join(sys.argv[0].split("\\")[:-1]))
import sqlite3
if not os.path.exists("img_base/"):
    os.mkdir("img_base/")
class eve(QEvent):
    def __init__(self,event=None):
        super(eve,self).__init__(event)
        print(locals())
    def KeyPress(self,event):
        print(event)
class myTr(QThread):
    si = pyqtSignal(list)
    cur = None
    files_ = {}
    pos = {}
    which_kind = None
    ex = None
    def run(self):
        try:
            l = [1,0]
            for x in os.listdir(self.cur):
                if l[1] in range(0,100000,10):
                    l[0]+= 1
                    l[1] = 0
                y1 = 0
                x1 = 1
                d = self.which_kind(x)
                z = x if len(x) < 12 else x[0:10]+"..."
                n = str(d)+".ico"
                qac = False
                y1,x1 = 1,0
                to_emit = []
                if d == "ico":
                    #self.files_[x] = QPushButton(QIcon(str(self.cur+x)),z)
                    to_emit.append(x)
                    to_emit.append(str(self.cur+x))
                    to_emit.append(z)
                elif d == "image":
                    to_emit.append(x)
                    try:
                        img = Image.open(self.cur+x)
                        img.thumbnail((100,50))
                        img.save("img_base/%s.ico"%x)
                        img.close()
                        to_emit.append(str("img_base/%s"%x))
                    except: to_emit.append("useless/image.ico")
                    #self.files_[x] = QPushButton(QIcon(str("imag.ico")),z)
                    
                    to_emit.append(z)
                elif d == "audio":
                    to_emit.append(x)
                    tag = eyed3.load(self.cur+x)
                    tag_ = tag.tag
                    has_image = False
                    for ipo in tag_.images:
                        has_image = True
                        r = open("image_to_what.jpg","wb")
                        r.write(ipo.image_data)
                        r.close()
                    if has_image == True:
                        try:
                            img = Image.open("image_to_what.jpg")
                            img.thumbnail((100,50))
                            img.save("img_base/%s.ico"%x)
                            img.close()
                            to_emit.append(("img_base/%s.ico"%x))
                        except: to_emit.append("audio.ico")
                    else:
                        to_emit.append(str("audio.ico"))
                    to_emit.append(z)
                else:
                    #self.files_[x] = QPushButton(QIcon(str(n)),z)
                    to_emit.append(x)
                    to_emit.append(str(n))
                    to_emit.append(z)
                to_emit.append(l[0])
                to_emit.append(l[1])
                to_emit.append(qac)
                l[1]+= 1
                if os.path.exists(self.cur+x):
                    if os.path.isdir(self.cur+x):
                        #self.files_[x].setIcon(QIcon("folder.ico"))
                        to_emit[1] = "folder.ico"
                if d == "image":
                    to_emit.append(self.cur+x)
                self.si.emit(to_emit)
        except Exception as e: print(e)
class jan(QWidget):
    def lopert(self,value=None):
        try:
            x = value[0]
            self.files_[x] = QPushButton(QIcon(value[1]),value[2])
            self.files_[x].setToolTip(str(x))
            self.files_[x].setMinimumWidth(30)
            self.files_[x].setMaximumHeight(80)
            self.ex["lay"].addWidget(self.files_[x],value[3],value[4])
            self.myer(e=self.files_[x])
            self.pos[x] = {"x":value[3],"y":value[4],"qac":value[5]}
            self.files_[x].setStyleSheet("QPushButton:hover{background-color:transparent;} QPushButton{background-color:#%2x%2x%2x}"%self.colours)
            #if len(value) == 7:
            #gh = "background-color:#%2x%2x%2x"%(randint(0,255),randint(0,255),randint(0,255))
            #    value[6] = value[6].replace(chr(92),"/")
            #   bn = "QPushButton{width: %s;height: %s; background-image: url('%s');}"%("100%","100%",value[6])
            #   self.files_[x].setStyleSheet(bn)
        except Exception as e: print(e)
    def __init__(self,parent=None):
        QWidget.__init__(self)
        self.colours = [(241, 191, 193),(30, 68, 240),(18, 91, 132),(187, 33, 129),(166, 108, 98),(148, 38, 99),(55, 90, 39),(80, 15, 156),(62, 187, 159),(180, 124, 92),(32, 84, 108)]
        self.colours = self.colours[randint(0,len(self.colours)-1)]
        self.setWindowTitle("Pro place to develop")
        try: self.setWindowIcon(QIcon("Folder-Grey.ico"))
        except: pass
        imgk = os.listdir("img_dir/")
        imgk = imgk[randint(0,len(imgk)-1)]
        css = """QWidget{background-color: #070E27}
QFrame { background-color: #00957b;
	border-radius:15px 15px; background-image: url('img_dir/"""+imgk+"""');}
QAction {background-color: black}
QMenu {background-color: black}
QLabel {background-color:#00957b;
	border-radius: 2;
	color: yellow;
	text-align: center;
	font-family: Comic Sans Ms;}
QCompleter:hover {border: 1 solid yellow;background-color:transparent}
QLabel:hover {border: 1 solid yellow;background-color:transparent}
QLineEdit:hover {border: 1 solid yellow;background-color:transparent}
QLineEdit:selected {color:white;background-color:black}
QPushButton {
font-family: Comic Sans Ms;
border-radius: 6;
background-color:#070E27;
color: yellow;
padding-bottom: 5;
border-style: dotted gray;}
QLineEdit {
font-family: Comic Sans Ms;
border-radius: 6;
background-color:#00957b;
color: yellow;}
QPushButton:hover{ text-decoration: underline;border: 1 solid yellow;background-color:transparent}
QMessageBox{background-color:#00957b;
	border-radius: 6;}
QTabWidget {background-color:#00957b;
	border-radius: 6;}
QTabWidget::addTab:hover {background-color:#00957b;
	border-radius: 6;}"""
        self.setStyleSheet(css)
        img = Image.open("cursor.ico")
        self.file_deitailed = ""
        img.thumbnail((15,15))
        self.setCursor(QCursor(ImageQt.toqpixmap(img)))
        self.lay = QGridLayout()
        self.tab = QTabWidget()
        self.lays = {}
        self.ex = {}
        self.ex["frame"] = QFrame()
        #self.ex["frame"].setMask(QBitmap(QPixmap(imgk)))
        self.ex["la1"] = QGridLayout()
        self.ex["la2"] = QGridLayout()
        self.ex["lay"] = QGridLayout()
        self.ex["la1"].addLayout(self.ex["la2"],0,0)
        self.ex["la1"].addLayout(self.ex["lay"],1,0)
        self.ex["frame"].setLayout(self.ex["la1"])
        self.ex["curdir"] = QLineEdit() #self.ex["frame"]
        self.ex["la2"].addWidget(self.ex["curdir"],0,1,0,1000)
        #self.ex["curdir"].setMinimumWidth(300)
        self.copied = []
        self.ex["curdir"].resize(3000,30)
        self.cur_dirs = {}
        self.st = QStringListModel()
        self.comp = QCompleter()
        self.comp.setModel(self.st)
        self.ex["curdir"].setText(os.getcwd())
        self.ex["curdir"].setCompleter(self.comp)
        self.ex["curdir"].textChanged.connect(self.cur_dir)
        #self.lays["explorer"] = QFrame()
        z = 0
        y = 0
        for x in self.lays.keys():
            self.lay.addLayout(self.lays[x],z,y)
            z+= 1
        self.scr_bar = QPushButton()
        self.scr_bar.setIcon(QIcon("back.ico"))
        self.scr_bar.clicked.connect(self.back_func)
        #self.scr_bar.setWidget(self.ex["frame"])
        self.ex["la2"].addWidget(self.scr_bar,0,0)
        self.tab.addTab(self.ex["frame"],"Explorador de arquivos")
        self.lay.addWidget(self.tab)
        self.setLayout(self.lay)
        self.names = {"audio":["mp3","m4a","ogg"],"executavel":["exe","bat","msi","lnk"],"video":["mp4","mkv","vid","ogg","avi","am4","m4a"],"ico":["ico",],"image":["gif","png","jpg","bmp","webp"],"web":["pdf","html","php","htm"],"doc":["css","xlsx","xls","docx","txt","spec","doc","ini","inf"],"winrar":["rar","gz","tar","zip","whl","CAB", "ARJ", "LZH", "TAR", "GZ", "ACE", "UUE", "BZ2", "JAR",
   "ISO", "XZ", "Z", "7Z"],"py":["py","pyc","pyd"]}
        self.names["dir"] = [x for x in os.listdir() if "folder" in x or "Folder" in x or "generic" in x]
        self.cur_dir()
        self.ex["frame2"] = QFrame()
        self.ex["l2"] = QFormLayout()
        self.ex["frame2"].setLayout(self.ex["l2"])
        self.tab.addTab(self.ex["frame2"],"Detalhes de arquivo")
        self.k_names = ["Arquivo currente","Nome","Tamanho","Localização","Formato","Ultima edição","Ultima vez acessado","Criado em","Executavel","Pode ser escrito","Pode ser lido","Oculto","Shortcut","Proprietario"]
        self.form_l ={}
        for x in self.k_names:
            self.form_l[x] = QLineEdit()
            #self.form_l[x].
            self.ex["l2"].addRow(x+": ",self.form_l[x])
        self.k_buts=[]
        for x in ["Guardar","Desfazer"]:
            y  = QPushButton(QIcon("Menu_dir"+x+".ico"),x)
            y.setToolTip(x)
            y.clicked.connect(self.other_win)
            #self.k_buts.append(y)
            self.ex["l2"].addRow(y)
        r = eve(10)
        self.event(r)
    def other_win(self):
        x = self.sender()
        m = self.file_deitailed
        try: self.info_file(m)
        except Exception as e: print(e)
    def back_func(self):
        try:
            y = str(self.ex["curdir"].text())
            e = self.widir(y)
            k =e
            j = chr(92)
            if "\\" in e:
                k = e.replace("\\",j)
            c = k.split(j)
            if c[-1] == "" or c[-1] == " ":
                c.pop(-1)
                c.pop(-1)
            n = j.join(c)
            self.ex["curdir"].setText(n)
        except Exception as ed: print(e)
    def info_file(self,x):
        j = chr(92)
        k = x
        if "\\" in x:
            k = x.replace("\\",j)
        self.file_deitailed = k
        fil = QFileInfo(k)
        h= {True:"Sim",False:"Não"}
        try:
            self.form_l["Nome"].setText(str(k.split(j)[-1]))
            self.form_l["Arquivo currente"].setText(str(k))
            self.form_l["Tamanho"].setText(str(fil.size()// 1024)+ " K")
            self.form_l["Localização"].setText(j.join(k.split(j)[:-1]))
            f = "Desconhecido"
            #if "." in k:
            #    f = k[::-1].split(".")[0][::-1]
            self.form_l["Formato"].setText(fil.suffix())
            self.form_l["Ultima edição"].setText(fil.lastModified().toString())
            self.form_l["Ultima vez acessado"].setText(fil.lastRead().toString())
            self.form_l["Criado em"].setText(fil.created().toString())
            self.form_l["Executavel"].setText(h[fil.isExecutable()])
            self.form_l["Pode ser escrito"].setText(h[fil.isWritable()])
            self.form_l["Pode ser lido"].setText(h[fil.isReadable()])
            self.form_l["Oculto"].setText(h[fil.isHidden()])
            self.form_l["Shortcut"].setText(h[fil.isShortcut()])
            self.form_l["Proprietario"].setText(fil.owner())
        except Exception as e: print(e)
        self.ex["frame2"].setFocus()
    def which_kind(self,x):
        x = str(x).lower()
        if "." in x:
            f = x[::-1].split(".")[0][::-1]
            for x in self.names.keys():
                if f in self.names[x]:
                    return x
        return "outro"
    def hov(self,x):
        print(self.sender())
    def cl_all(self): #(241, 191, 193),
        self.colours = [(30, 68, 240),(18, 91, 132),(187, 33, 129),(166, 108, 98),(148, 38, 99),(55, 90, 39),(80, 15, 156),(62, 187, 159),(180, 124, 92),(32, 84, 108)]
        self.colours = self.colours[randint(0,len(self.colours)-1)]
        try:
            for x in self.files_:
                try:
                    [self.files_[x].setHidden(True),self.files_[x].destroy(),self.files_[x].close(),self.ex["lay"].removeWidget(self.files_[x])]
                    try: self.thr.quit();self.thr.terminate()
                    except Exception as e: print(e)
                except Exception as e: print(e)
        except: pass
    def dir_see(self):
        m = str(self.ex["curdir"].text())
        self.cl_all()
        self.pos = {}
        self.files_ = {}
        #self.funcs = {}
        self.labels = {}
        self.menus = {}
        self.laysw = {}
        l = [1,0]
        y = str(self.ex["curdir"].text())
        if y.endswith("/") or y.endswith("\\") or y.endswith(chr(92)):
            g = str(self.ex["curdir"].text())
        else:
            g = str(self.ex["curdir"].text())+chr(92)
        '''
        for x in os.listdir(m):
            if l[1] in range(0,100000,10):
                l[0]+= 1
                l[1] = 0
            y1 = 0
            x1 = 1
            #self.funcs[x] = QFrame()
            #self.laysw[x] = QGridLayout()
            #self.funcs[x].setLayout(self.laysw[x])
            #self.files_[x] = QPushButton("")
            d = self.which_kind(x)
            z = x if len(x) < 12 else x[0:10]+"..."
            #self.labels[x] = QLabel(z)
            #img = Image.open(str(d)+".ico")
            #img.thumbnail((45,60))
            #self.files_[x].setPixmap(ImageQt.toqpixmap(img))
            n = str(d)+".ico"
            qac = False
            y1,x1 = 1,0
            if d == "ico":
                    self.files_[x] = QPushButton(QIcon(str(g+x)),z)
            elif d == "image":
                #self.labels[x].setPixmap(ImageQt.toqpixmap(img))
                #self.files_[x].setText(QIcon(n),z)
                self.files_[x] = QPushButton(QIcon(str("imag.ico")),z)
            else:
                #img = Image.open(n)
                #img.thumbnail((20,20))
                #self.labels[x].setPixmap(ImageQt.toqpixmap(img))
                self.files_[x] = QPushButton(QIcon(str(n)),z)
                #self.files_[x].setText(QIcon(n),z)
            self.files_[x].setToolTip(str(x))
            #self.funcs[x].setToolTip(str(x))
            #self.labels[x].setToolTip("<b><font color=red font-style=underline>"+str(x)+"</font></b>")
            #self.files_[x].setText(x)
            self.files_[x].setMinimumWidth(30)
            self.files_[x].setMaximumHeight(80)
            self.ex["lay"].addWidget(self.files_[x],l[0],l[1])
            self.pos[x] = {"x":l[0],"y":l[1],"qac":qac}
            #self.labels[x].setBuddy(self.files_[x])
            #self.laysw[x].addWidget(self.labels[x],x1,0)
            #self.ex["lay"].addWidget(self.files_[x],l[0],l[1])
            #self.files_[x].activeted.connect(self.hov)
            #self.files_[x].show(l[1],l[0])
            #self.files_[x].show()
            l[1]+= 1
            #self.funcs[x].hovered.connect(lambda z=x: self.labn(x=z))
            #self.files_[x].clicked.connect(self.myer)
            #l[0] += 1
            #self.funcs[x] = lambda: self.tir(x=x)
            if os.path.exists(g+x):
                if os.path.isdir(g+x):
                    #self.labels[x].activated.connect(self.labn)
                    #self.labels[x].linkActivated.connect(self.tir)
                    #self.files_[x].clicked.connect(self.tir)
                    #self.files_[x].setIcon(QIcon(self.names["dir"][randint(0,len(self.names["dir"])-1)]))
                    #img = Image.open(self.names["dir"][randint(0,len(self.names["dir"])-1)])
                    #img.thumbnail((20,20))
                    #self.labels[x].setPixmap(ImageQt.toqpixmap(img))
                    #gg = str(self.names["dir"][randint(0,len(self.names["dir"])-1)])
                    self.files_[x].setIcon(QIcon("folder.ico"))'''
        try:
            self.thr = myTr()
            self.thr.cur = g
            self.thr.files_ = self.files_
            self.thr.which_kind  = self.which_kind
            self.thr.ex = self.ex
            self.thr.pos = self.pos
            self.thr.si.connect(self.lopert)
            self.thr.start()
        except Exception as e: print(e)
        #for x in self.files_:
        #    self.myer(e=self.files_[x])
    def widir(self,y):
        if y.endswith("/") or y.endswith("\\") or y.endswith(chr(92)):
            g = y
        else:
            g = y+chr(92)
        return g
    def labn(self,x):
        x = self.sender()
        print(x)
    def cl(self,x):
        if x.text() == "&Yes":
            print("Deleting... ",self.to_delete)
        x.parent().close()
    def ren(self,x):
        if x.text() == "Save":
            try:
                os.rename(self.to_rename,self.to_ren_dir+str(self.ren_val.text()))
                #self.files_[self.to_ren_file].setText(str(self.ren_val.text()))
                #self.labels[self.to_ren_file].setToolTip(str(self.ren_val.text()))
                #self.files_[self.to_ren_file].setToolTip(str(self.ren_val.text()))
                self.ren_val.setHidden(True)
                self.files_[self.to_ren_file].setHidden(False)
            except Exception as e: print(e)
        x.parent().close()
    def ac(self,x,y):
        q = self.last_dir
        g = self.widir(q)
        v = g+x.toolTip()
        v = v.replace("\\",chr(92))
        v = v.replace("/",chr(92))
        if y == "Copy":
            return x
        elif y == "Copy name":
            pyperclip.copy(x.toolTip())
        elif y == "Copy path":
            pyperclip.copy(v)
        elif y=="Rename":
            d = self.which_kind(x)
            self.to_rename = v
            self.to_ren_dir = g
            self.to_ren_file = x.toolTip()
            h = x
            x = x.toolTip()
            self.files_[x].setHidden(True)
            self.ren_val = QLineEdit()
            #lay  = self.funcs[x].layout()
            self.ren_val.setText(x)
            self.ex["lay"].addWidget(self.ren_val,self.pos[x]["x"],self.pos[x]["y"])
            r = QDialogButtonBox(QDialogButtonBox.Save|QDialogButtonBox.Cancel)
            r.clicked.connect(self.ren)
            self.ex["la2"].addWidget(r,0,1)
        elif y=="Delete":
            self.to_delete = v
            r = QDialogButtonBox(QDialogButtonBox.Yes|QDialogButtonBox.Cancel)
            r.clicked.connect(self.cl)
            r.setWindowOpacity(0.1)
            self.ex["la2"].addWidget(r,0,1)            #os.remove(v)
        elif y=="Open with":
            b = QFileDialog()
            t = b.getOpenFileName(filter="*.exe")[0]
            if len(t) > 3:
                k = Popen([t,v])
        elif y == "Run with Python":
            Popen(["python.exe",v])
        elif y == "Watch":
            b = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe" if os.path.exists("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe") else "C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe"
            Popen([b,v])
        elif y == "Listen":
            b = "C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe"
            Popen([b,v])
        elif y == "Cut":
            return x
        elif y == "Paste":
            return x
        elif y == "Details":
            self.info_file(v)
        elif y == "Open":
            Popen(["explorer",v])
        elif y == "Open here":
            self.get_in(v)
        elif y == "cmd":
            Popen("cmd")
        elif y == "Read":
            try:
                r = open(v,"r",encoding="charmap")
                pyperclip.copy(r.read())
                r.close()
            except Exception as e: print(e)
        elif y == "Paste copy on path label":
            self.ex["curdir"].setText(str(pyperclip.paste()))
        elif y.endswith(".exe"):
            v = v.replace("\\",chr(92))
            v = v.replace("/",chr(92))
            try: Popen([y,v])
            except Exception as e: print(e)
    def myer(self,e=None):
        r = e if isinstance(e,QPushButton) else self.sender()
        n = self.ac
        self.fin = {}
        d = ["Open","Open here","Copy","Copy name","Copy path","Paste copy on path label","Rename","Read","Delete","Run with Python","Watch","Listen","Cut","Paste","Details","cmd"]
        try:
            m = QMenu("Menu")
            for x in d:
                self.fin[x] = lambda z=x: self.ac(x=r,y=z)
                m.addAction(QIcon("Menu_dir/"+x+".ico"),x,self.fin[x])
            x = "Open with"
            self.fin[x] = lambda z=x: self.ac(x=r,y=z)
            #ml = QMenu(x)
            #ml.addAction(x,self.fin[x])
            ml = m.addMenu(x)
            for x in ["Explorer.exe","Opera.exe","Notepad.exe","wmplayer.exe","winrar.exe","cmd.exe","Microsoft word.exe"]:
                self.fin[x] = lambda z=x: self.ac(x=r,y=z)
                ml.addAction(QIcon("Menu_dir/"+x+".ico"),x,self.fin[x])
            r.setMenu(m)
        except Exception as e: print(e)
    def get_in(self,x):
        self.ex["curdir"].setText(x)
        self.cur_dir()
    def tir(self,x=None):
        x = self.sender().toolTip()
        y = str(self.ex["curdir"].text())
        if y.endswith("/") or y.endswith("\\") or y.endswith(chr(92)):
            self.ex["curdir"].setText(str(self.ex["curdir"].text())+str(x))
        else:
            self.ex["curdir"].setText(str(self.ex["curdir"].text())+"/"+str(x))
        self.cur_dir()
    def KeyPressEvent(self,event):
        print(event)
    def cur_dir(self):
        try:
            ty = []
            m = str(self.ex["curdir"].text())
            if len(m) <= 1:
                self.cl_all()
                t = psutil.disk_partitions()
                self.files_ = {}
                self.pos = {}
                l = 0
                self.last_dir= ""
                for x in t:
                    us = psutil.disk_usage(x.device)
                    self.files_[x.device] = QPushButton(x.device+f"\nTotal: {us.total//1024} MB\nUsed in percents: {us.percent}%\nUsed: {us.used//1024} MB\nType: {x.fstype}")
                    self.ex["lay"].addWidget(self.files_[x.device],l,0)
                    self.files_[x.device].setToolTip(x.device)
                    self.myer(e=self.files_[x.device])
                    self.files_[x.device].setMinimumWidth(200)
                    jk = x.device+"_prog"
                    self.files_[x.device].setStyleSheet("QPushButton:hover{background-color:transparent;} QPushButton{background-color:#%2x%2x%2x}"%self.colours)
                    self.files_[jk] = QProgressBar()
                    self.files_[jk].setOrientation(Qt.Horizontal)
                    self.files_[jk].setMinimum(0)
                    self.files_[jk].setMaximum(100)
                    self.files_[jk].setValue(us.percent)
                    l+= 1
                    self.ex["lay"].addWidget(self.files_[jk],l,0)
                    l+= 1
            elif os.path.exists(m):
                if os.path.isdir(m):
                    ty = []
                    for x in os.listdir(m):
                        v = str(m)+str(chr(92))+str(x)
                        ty.append(v)
                    self.st.setStringList(ty)
                    self.dir_see()
                    self.last_dir = m
        except Exception as e: print(e)
app = QApplication(sys.argv)
win = jan()
win.show()
app.exec_()
if os.path.exists("img_base/"):
    for x in os.listdir("img_base/"):
        os.remove("img_base/%s"%x)
