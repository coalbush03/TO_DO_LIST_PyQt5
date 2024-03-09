import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QListWidget, QLineEdit, QHBoxLayout, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QFont

#klasa
class ToDoList(QWidget):
  def __init__(self):
    #konstruktor
    super().__init__()
    #GUI
    self.setWindowTitle("To Do List")
    self.setStyleSheet("background-color: #3F3F37;")
    self.setGeometry(100,100,300,300)

    #lista zadan
    self.elements=[]

    self.layout=QVBoxLayout() #Vertical Box Layout
    #przygotowanie widgetow
    self.input=QLineEdit()  #wprowadzanie zadan
    self.input.setStyleSheet("background-color: white; color: black; border-radius:5px;")
    self.input.setFont(QFont("Comic Sans MS",12))
    self.add_but=QPushButton("DODAJ") #przycisk na wprowadzenie
    self.add_but.setStyleSheet("background-color:#A2A77F; color: #002E2C; border-radius:5px;")
    self.add_but.setFont(QFont("Comic Sans MS",12))
    self.el_list=QListWidget() # widget na liste
    self.el_list.setStyleSheet("background-color: #D6D6B1; color: black; border-radius:5px;")
    self.el_list.setFont(QFont("Comic Sans MS",12))

    #dodanie widgetów
    self.layout.addWidget(self.input)
    self.layout.addWidget(self.add_but)
    self.layout.addWidget(self.el_list)

    self.add_but.clicked.connect(self.add) #przypisanie do przycisku dodawania
    self.input.returnPressed.connect(self.add)# przypisanie przycisku enter do dodania
    self.setLayout(self.layout) # ustawienie układu


  def add(self):
    el=self.input.text() # wyjecie z inputu tekstu
    if el:
      self.elements.append(el) # dodanie do listy zadan
      el = '\u2022 ' + el #dodanie kropki
      self.el_list.addItem(el) #dodanie do listy GUI
      self.input.clear() #wyczyszczenie pola po dodatniu

if __name__== "__main__":
  application=QApplication(sys.argv)
  win= ToDoList() #wywolanie
  win.show()
  sys.exit(application.exec_())


