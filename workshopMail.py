# İSTENİLEN MAİLE METİN GÖNDERME
import smtplib
from email.mime.multipart import MIMEMultipart # MESAJ GÖVDEMİZİ YANİ MAİL YAPIMIZI OLUŞTURACAK 
from email.mime.text import MIMEText
import os
import sys
from PyQt5.QtWidgets  import QWidget,QApplication,QTextEdit,QLabel,QCheckBox,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout,QRadioButton
from PyQt5.QtWidgets import QAction,qApp,QMainWindow
class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.baglan = Mail()
      
    def init_ui(self):
        
        self.gonder = QPushButton("GÖNDER")
        self.temizle =QPushButton("TEMİZLE")
        self.kaydet = QPushButton("KAYDET")
        self.text = QTextEdit("")
        self.mail = QLabel("HANGİ MAİL HESABINA GÖNDERMEK İSTERSİNİZ")
        self.eren = QRadioButton("eerkesikbas0@gmail.com")
        self.tala = QRadioButton("talhaergy@gmail.com")
        self.yunus = QRadioButton("yunusemreyee64@gmail.com")
        h_box = QHBoxLayout()
        h_box.addWidget(self.gonder)
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.kaydet)
        h_box.addStretch()
    
        v_box =QVBoxLayout()
        v_box.addWidget(self.mail)
        v_box.addWidget(self.text)
        v_box.addWidget(self.eren)
        v_box.addWidget(self.tala)
        v_box.addWidget(self.yunus)
        v_box.addLayout(h_box)
        self.setLayout(v_box)
        self.temizle.clicked.connect(self.sil)
        self.kaydet.clicked.connect(self.kayit)
        self.gonder.clicked.connect(lambda : self.click(self.eren.isChecked(),self.tala.isChecked(),self.yunus.isChecked(),self.text))

    def click(self,eren,tala,yunus,text):
        if eren :
            
            self.baglan.sendMail("eerkesikbas0@gmail.com",(self.text.toPlainText()))
            self.text.setText("MAİL GÖNDERİLDİ...")
        if tala :
            self.baglan.sendMail("talhaergy@gmail.com",(self.text.toPlainText()))
            self.text.setText("MAİL GÖNDERİLDİ...")
        if yunus :

            self.baglan.sendMail("yunusemreyee64@gmail.com",(self.text.toPlainText()))
            self.text.setText("MAİL GÖNDERİLDİ...")

    def sil(self):
        self.text.clear()
    def kayit(self):
        dosya_ismi = QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))
        with open(dosya_ismi[0],"w") as file:
            file.write(self.text.toPlainText())
        self.text.setText("KAYIT İŞLEMİ BAŞARIYLA GERÇEKLEŞTİ.")
    def dosya_ac(self):
        dosya_ismi = QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME")) # hazır kod getenv ile kaydedilecek yer yazılır home yerine desktop da yasılabilir
        with open(dosya_ismi[0],"r") as file: # dosya isminin 0.indisi ile istediğimiz dosyaya gireriz 
            self.text.setText(file.read()) # dosyayı okuruz

class Mail():
    def __init__(self):
        self.mesaj = MIMEMultipart()
    def sendMail(self,email,text):
        self.mesaj = MIMEMultipart()
        self.mesaj["From"] = "yunusemreyee64@gmail.com"
        self.mesaj["To"] = email
        self.mesaj["Subject"] = "PyQt5 ile MAİL GÖNDERME İŞLEMLERİ"
        self.yazi = text
        self.mesaj_govdesi = MIMEText(self.yazi,"plain")
        self.mesaj.attach(self.mesaj_govdesi)
        try:
            self.mail = smtplib.SMTP("smtp.gmail.com",587)  
            self.mail.ehlo() 
            self.mail.starttls() 
            self.mail.login("yunusemreyee64@gmail.com","") # "" olan yeri mailinizin şifresini girerek oluşturabilirsiniz   
            self.mail.sendmail(self.mesaj["From"],self.mesaj["To"],self.mesaj.as_string()) 
            print("Mail Başarıyla Gönderildi....")
            self.mail.close() 
        except:
            sys.stderr.write("Bir sorun oluştu!")
            sys.stderr.flush(),
    
class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pencere = Pencere()
        self.setCentralWidget(self.pencere)
        self.menu_olustur()
        self.baglan = Mail()

    def menu_olustur(self):
        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")
        dosya_kaydet = QAction("Dosya Kayıt",self)
        dosya_kaydet.setShortcut("Ctrl + S")
        cikis = QAction("Çıkış Yap",self)
        cikis.setShortcut("Ctrl + Q")
        dosya_ac = QAction("Dosya Aç",self)
        dosya_ac.setShortcut("Ctrl + O ")
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)
        dosya.addAction(dosya_ac)
        dosya.triggered.connect(self.response)
        self.setWindowTitle("MAİL GÖNDERME İŞLEMLERİ")
        self.show()

    def response(self,action):
        if action.text() == "Dosya Kayıt" :
            self.pencere.kayit()
        elif action.text() == "Çıkış Yap":
            qApp.quit()
        elif action.text() == "Dosya Aç":
            self.pencere.dosya_ac()

app = QApplication(sys.argv)
mail = MainMenu()
sys.exit(app.exec_())