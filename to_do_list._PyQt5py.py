import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QListWidget, QLineEdit, QHBoxLayout, QMainWindow
from PyQt5.QtCore import Qt, QFile
from PyQt5.QtGui import QPalette, QFont

#klasa elementu listy
class TodoListItem(QWidget):
    def __init__(self, text,todo_list, index):
        super().__init__()

        self.todo_list = todo_list #lista do ktorej sie odwoluje
        self.index = index # index elementu

        self.layout = QHBoxLayout() #horizontal layout
        self.layout.setContentsMargins(0, 0, 0, 0) #0 marginesow

        self.del_but = QPushButton("X")
        self.del_but.setStyleSheet("background-color: #2B303A; color: #D64933; border-radius:5px; font:bold")
        self.del_but.setFont(QFont("Comic Sans MS", 12))
        self.del_but.clicked.connect(self.remove) #podlaczenie do funkcji

        self.text_field = QPushButton(text)
        self.text_field.setStyleSheet("background-color: #BAC1B8; color: black; border-radius:5px;")
        self.text_field.setFont(QFont("Comic Sans MS", 12))

        #wymiary
        text_field_size = self.text_field.sizePolicy()
        text_field_size.setHorizontalStretch(4)
        self.text_field.setSizePolicy(text_field_size)

        del_but_size = self.del_but.sizePolicy()
        del_but_size.setHorizontalStretch(1)
        self.del_but.setSizePolicy(del_but_size)

        self.layout.addWidget(self.text_field)
        self.layout.addWidget(self.del_but)

        self.setLayout(self.layout)

    def remove(self):
        self.todo_list.remove_element(self.index)#usuniecie z listy elements i nadpisanie pliku tekstowego z listą (funkcja dalej w kodzie)
        for i in range(self.index,len(self.todo_list.elements)): 
            self.todo_list.elements[i].index -= 1 #zmiejszenie indexow po popie
        self.setParent(None) #usun widget
       


#klasa listy
class ToDoList(QWidget):
  def __init__(self):
    #konstruktor
    super().__init__()
    #GUI
    self.setWindowTitle("To Do List")
    self.setStyleSheet("background-color: #58A4B0;")
    self.setFixedWidth(300) #utrzymanie geometrii

    #lista zadan
    self.elements=[]

    self.layout=QVBoxLayout() #Vertical Box Layout
    #przygotowanie widgetow
    self.input=QLineEdit()  #wprowadzanie zadan
    self.input.setStyleSheet("background-color: white; color: black; border-radius:5px;")
    self.input.setFont(QFont("Comic Sans MS",12))
    self.add_but=QPushButton("DODAJ") #przycisk na wprowadzenie
    self.add_but.setStyleSheet("background-color:#0C7C59; color: #002E2C; border-radius:5px;")
    self.add_but.setFont(QFont("Comic Sans MS",12))

    self.layout.setAlignment(Qt.AlignTop) #umieszcza wszystko u gory
    
    #dodanie widgetów
    self.layout.addWidget(self.input)
    self.layout.addWidget(self.add_but)
  

    self.add_but.clicked.connect(self.add) #przypisanie do przycisku dodawania
    self.input.returnPressed.connect(self.add)# przypisanie przycisku enter do dodania
    self.load_els()  #ładowanie pliku


    self.setLayout(self.layout) # ustawienie układu


  def add(self):
    el=self.input.text() # wyjecie z inputu tekstu
    if el:
      el=TodoListItem(el,self,len(self.elements)) #dodanie kropi
      self.elements.append(el) # dodanie do listy zadan
      self.layout.addWidget(el) #dodanie do listy GUI
      self.input.clear() #wyczyszczenie pola wpisywania po dodatniu
      self.save_els()  #zapis do pliku
  
  def save_els(self):  #zapisanie listy
    with open("elements.txt", "w") as file:
      for el in self.elements:
            file.write(el.text_field.text() + "\n") #wpisanie tekstu z obiektów klasy ToDoListItem w liscie elements do pliku

  def remove_element(self, index): #funkcja wspomniana w funkcji remove w klasie TodoListItem
    self.elements.pop(index)
    self.save_els()

  def load_els(self):
    if QFile.exists("elements.txt"): 
        with open("elements.txt", "r") as file:
            els = file.read().splitlines() # podzial odczytu linii z pliku na liste
            for el in els:
              el = TodoListItem(el,self,len(self.elements)) #nadanie indeksu - aktualna dlugosc listy
              self.elements.append(el) # dodanie do listy zadan
              self.layout.addWidget(el)  # dodanie do listy gui
    else:
        print("NO FILE - LIST EMPTY")

if __name__== "__main__":
  #wywolanie
  application=QApplication(sys.argv) #utworzenie aplikacji z wektorem argv jako argument
  win= ToDoList() #utworzenie okna
  win.show() #pokazanie okna
  sys.exit(application.exec_()) #wyjscie z aplikacji