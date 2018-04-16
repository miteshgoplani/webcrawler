import sys
from PyQt5 import QtWidgets
from bs4 import BeautifulSoup
import requests
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit,QInputDialog
import re
import os
import sqlite3
import csv


##sqlite_file = 'C:/Users/dell/Desktop/my_database.sqlite'
##conn = sqlite3.connect(sqlite_file)
##c = conn.cursor()
##if os.path.isfile(sqlite_file)==False:
##    c.execute('CREATE TABLE crawler (id INTEGER,links text)')
##    print('created')


class Main(QtWidgets.QWidget):
    
    def __init__(self):
        sqlite_file = 'C:/Users/dell/Desktop/my_database.sqlite'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        if os.path.isfile(sqlite_file)==False:
            c.execute('CREATE TABLE crawler (l_id INTEGER PRIMARY KEY,website text,links text)')
            print('created')
        QtWidgets.QWidget.__init__(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('VES Web Crawler')
        self.lineHeader=QtWidgets.QLabel("Top 10 crawled Links:",self)
        self.lineHeader.setStyleSheet("color:blue;")
        self.lineHeader.move(0, 35)
        self.lineHeader.resize(100, 25)

        self.lineLastPost1 = QtWidgets.QLineEdit(self)
        self.lineLastPost1.move(0, 65)
        self.lineLastPost1.setReadOnly(True)
        self.lineLastPost1.resize(1300, 25)

        self.lineLastPost2 = QtWidgets.QLineEdit(self)
        self.lineLastPost2.move(0, 95)
        self.lineLastPost2.setReadOnly(True)
        self.lineLastPost2.resize(1300, 25)

        self.lineLastPost3 = QtWidgets.QLineEdit(self)
        self.lineLastPost3.move(0, 125)
        self.lineLastPost3.setReadOnly(True)
        self.lineLastPost3.resize(1300, 25)

        self.lineLastPost4 = QtWidgets.QLineEdit(self)
        self.lineLastPost4.move(0, 155)
        self.lineLastPost4.setReadOnly(True)
        self.lineLastPost4.resize(1300, 25)

        self.lineLastPost5 = QtWidgets.QLineEdit(self)
        self.lineLastPost5.move(0, 185)
        self.lineLastPost5.setReadOnly(True)
        self.lineLastPost5.resize(1300, 25)

        self.lineLastPost6 = QtWidgets.QLineEdit(self)
        self.lineLastPost6.move(0, 215)
        self.lineLastPost6.setReadOnly(True)
        self.lineLastPost6.resize(1300, 25)

        self.lineLastPost7 = QtWidgets.QLineEdit(self)
        self.lineLastPost7.move(0, 245)
        self.lineLastPost7.setReadOnly(True)
        self.lineLastPost7.resize(1300, 25)

        self.lineLastPost8 = QtWidgets.QLineEdit(self)
        self.lineLastPost8.move(0, 275)
        self.lineLastPost8.setReadOnly(True)
        self.lineLastPost8.resize(1300, 25)

        self.lineLastPost9 = QtWidgets.QLineEdit(self)
        self.lineLastPost9.move(0, 305)
        self.lineLastPost9.setReadOnly(True)
        self.lineLastPost9.resize(1300, 25)

        self.lineLastPost10 = QtWidgets.QLineEdit(self)
        self.lineLastPost10.move(0, 335)
        self.lineLastPost10.setReadOnly(True)
        self.lineLastPost10.resize(1300, 25)

        getInfo = QtWidgets.QPushButton("Crawl Website", self)
        getInfo.move(455, 5)
        getInfo.resize(295, 25)
        getInfo.clicked.connect(self.getText)

        getInfo = QtWidgets.QPushButton("Add to Database", self)
        getInfo.move(50, 400)
        getInfo.resize(295, 55)
        getInfo.clicked.connect(self.database)

        getInfo = QtWidgets.QPushButton("Save content in text file", self)
        getInfo.move(885, 400)
        getInfo.resize(295, 55)
        getInfo.clicked.connect(self.save)



    def getText(self):
        text, OKPressed = QInputDialog.getText(self, "Enter URL", "Website URL:", QLineEdit.Normal, "")
        if OKPressed and text != '':
            r  = requests.get("http://" +text)
            data = r.text
            soup = BeautifulSoup(data,"lxml")
            Data=[]
            sqlite_file = 'C:/Users/dell/Desktop/my_database.sqlite'
            conn = sqlite3.connect(sqlite_file)
            c = conn.cursor()
            for link in soup.find_all('a'):
                print(link.get('href'))
                Data.append(str(link.get('href')))
                data = [(text,str(link.get('href')))]
                print(data)
                c.executemany('INSERT INTO crawler(website,links) VALUES(?,?)', data)
            self.lineLastPost1.setText(Data[0])
            self.lineLastPost2.setText(Data[1])
            self.lineLastPost3.setText(Data[2])
            self.lineLastPost4.setText(Data[3])
            self.lineLastPost5.setText(Data[4])
            self.lineLastPost6.setText(Data[5])
            self.lineLastPost7.setText(Data[6])
            self.lineLastPost8.setText(Data[7])
            self.lineLastPost9.setText(Data[8])
            self.lineLastPost10.setText(Data[9])
        conn.commit()

    def save(self):
        f1=open("C:/Users/Dell/Desktop/output.txt","a")
        f1.write("=====================================New Entry==================================\n")
        f1.write(self.lineLastPost1.text())
        f1.write("\n")
        f1.write(self.lineLastPost2.text())
        f1.write("\n")
        f1.write(self.lineLastPost3.text())
        f1.write("\n")
        f1.write(self.lineLastPost4.text())
        f1.write("\n")
        f1.write(self.lineLastPost5.text())
        f1.write("\n")
        f1.write(self.lineLastPost6.text())
        f1.write("\n")
        f1.write(self.lineLastPost7.text())
        f1.write("\n")
        f1.write(self.lineLastPost8.text())
        f1.write("\n")
        f1.write(self.lineLastPost9.text())
        f1.write("\n")
        f1.write(self.lineLastPost10.text())
        f1.write("\n")
        f1.close()
        os.startfile("C:/Users/Dell/Desktop/output.txt")


    def database(self):
        print('Printing from database:')
        sqlite_file = 'C:/Users/dell/Desktop/my_database.sqlite'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        for row in c.execute('SELECT * FROM crawler'):
            print(row)
        with open("C:/Users/Dell/Desktop/crawler_database.txt", "a") as f:
            writer = csv.writer(f, delimiter='\t')
            cursor = c.execute("SELECT * FROM crawler")
            writer.writerow([i[0] for i in cursor.description])
            writer.writerows(cursor.fetchall())
        f.close()
        os.startfile("C:/Users/Dell/Desktop/crawler_database.txt")
        



def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

conn.close()
