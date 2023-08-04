from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QTextEdit, QLineEdit
import json

app = QApplication([])
window = QWidget()

list_countries = QListWidget()
text_countries = QTextEdit()
name_countries = QLineEdit()
name_countries.setPlaceholderText('Введите страну...')
add_country_button = QPushButton('добавить страну')
del_country_button = QPushButton('удалить страну')
edit_country_button = QPushButton('изменить страну')

buttons_layout = QHBoxLayout()
right_layout = QVBoxLayout()
left_layout = QVBoxLayout()
main_layout = QHBoxLayout()

buttons_layout.addWidget(add_country_button)
buttons_layout.addWidget(del_country_button)
buttons_layout.addWidget(edit_country_button)

right_layout.addWidget(add_country_button)
right_layout.addWidget(name_countries)
right_layout.addWidget(del_country_button)


main_layout.addLayout(left_layout, 3)
main_layout.addLayout(right_layout, 7)
window.setLayout(main_layout)

window.resize(1000, 700)
window.setWindowTitle("Путеводитель")
window.setStyleSheet("background color: grey")
list_countries.setStyleSheet("border: 4px solid black; font-size: 24px; color: white; font-style: italic")
text_countries.setStyleSheet("border: 4px solid black; font-size: 24px; color: white; font-style: italic;")
name_countries.setStyleSheet("border: 4px solid black; font-size: 18px; colors white; font-style; italic;")
add_country_button.setStyleSheet("border: 4px solid black; font-size: 18px; colors: white; font-style: italic")
del_country_button.setStyleSheet("border: 4px solid black; font-size: 18px; color: white; font-style: italic")
edit_country_button.setStyleSheet("border: 4px solid black; font-size: 18px; color: white; font-style: italic")

def fill_countries():
    list_countries.clear()
    with open('countries.json', 'r', encoding = 'utf-8') as file:
        countries = json.load(file)
        for country in countries:
            list_countries.addItem(country)

def add_country():
    list_countries.text()
    with open('countries.json', 'r', encoding = 'utf-8') as file:
        countries = json.load(file)
    if not(country in countries):
        countries[country] = ''
    with open('countries.json', 'w', encoding = 'utf-8') as file:
        json.dump(file)
    fill_countries()

def del_country():
    if list_countries.selectedItem():
        country = list_countries.selectedItem()[0].text()
        with open('countries.json', 'r', encoding = 'utf-8') as file:
            countries = json.load(file)
        del countries[country]
        with open('countries.json', 'w', encoding = 'utf-8') as file:
            json.dump(countries , file)
        fill_countries()

def edit_country():
    if list_countries.selectedItem():
        country = list_countries.selectedItem()[0].text()
        text_country = text_countries.toPlainText()
        with open('countries.json', 'r', encoding = 'utf-8') as file:
            countries = json.load(file)
        countries[country] = text_country
        with open('countries.json', 'w', encoding = 'utf-8') as file:
            json.dump(countries , file)
def info_country():
    country = list_countries.selectedItem()[0].text()
    with open('countries.json', 'w', encoding = 'utf-8') as file:
        json.dump(countries , file)
    text_countries.setText(countries[country])

fill_countries()

add_country_button.clicked.connect(add_country)
del_country_button.clicked.connect(del_country)
edit_country_button.clicked.connect(edit_country)
list_countries.itemClicked.connect(info_country)


window.show()
app.exec()



