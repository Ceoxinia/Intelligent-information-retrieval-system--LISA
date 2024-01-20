import sys
import copy
import nltk
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog, QApplication, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, \
    QRadioButton, QVBoxLayout, QWidget, QColumnView, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from Functions import *
from pyqtgraph import PlotWidget

from PyQt5.QtGui import QPixmap, QImage, QStandardItemModel, QStandardItem
import cv2

import warnings



class mainWindow(QDialog):
    def __init__(self):
        super(mainWindow,self).__init__()
        loadUi("main.ui",self)
        self.btn_search.clicked.connect(self.Search)
        self.terms_per_doc.toggled.connect(self.check_terms_per_doc)
        self.docs_per_term.toggled.connect(self.check_docs_per_term)
        self.index_check.stateChanged.connect(self.Index_enable)
        self.index_check.stateChanged.connect(self.dis_radios)
        self.terms_per_doc.setEnabled(False)
        self.docs_per_term.setEnabled(False)

        self.VSM.toggled.connect(self.VSM_enable)

        self.VS_choice.setEnabled(False)
        self.query_dst.setEnabled(False)
        self.VS_choice.addItem("Scalar Product")
        self.VS_choice.addItem("Cosine Measure")
        self.VS_choice.addItem("Jaccard Measure")

        self.BM.toggled.connect(self.check_BM)
        self.boolean_model.toggled.connect(self.check_boolean_model)
        self.DMM.toggled.connect(self.check_DMM)

        self.query_dataset.stateChanged.connect(self.dis_spin)

        self.query_dst.valueChanged.connect(self.spin_query_change)

    def spin_query_change(self,value):

        with open('./Queries/Queries','r') as file:
            lines = file.readlines()
            try:
                text=lines[value-1].replace('\n', '')
                self.entree.setText(text)
            except Exception:
                text=''
                self.entree.setText(text)

    def dis_spin(self, state):
        # Disable the radio button when the checkbox is checked
        self.query_dst.setEnabled(state == 2)

    def check_terms_per_doc(self, checked):
        self.docs_per_term.setChecked(not checked)
    def check_docs_per_term(self,checked):
        self.terms_per_doc.setChecked(not checked)

    def check_BM(self, state):
        if self.BM.isChecked():
            self.VSM.setChecked(not state)
            self.boolean_model.setChecked(not state)
            # self.DMM.setChecked(not state)
            self.index_check.setChecked(not state)
    def check_boolean_model(self, state):
        if self.boolean_model.isChecked():
            self.VSM.setChecked(not state)
            self.BM.setChecked(not state)
            self.DMM.setChecked(not state)
            self.index_check.setChecked(not state)
    def check_DMM(self, state):
        if self.DMM.isChecked():
            self.VSM.setChecked(state)
            self.BM.setChecked(not state)
            self.boolean_model.setChecked(not state)
            self.index_check.setChecked(not state)
    def VSM_enable(self, state):
        if self.VSM.isChecked():
            self.VS_choice.setEnabled(True)

            self.BM.setChecked(not state)
            self.boolean_model.setChecked(not state)
            # self.DMM.setChecked(not state)
            self.index_check.setChecked(not state)

        else :
            self.VS_choice.setEnabled(False)
    def Index_enable(self, state):
        # Disable the radio button when the checkbox is checked
        self.terms_per_doc.setEnabled(state == 2)
        self.docs_per_term.setEnabled(state == 2)

    def dis_radios(self, state):
        # Disable the radio button when the checkbox is checked
        if state==2:
            self.VSM.setChecked(False)
            self.boolean_model.setChecked(False)
            self.DMM.setChecked(False)
            self.BM.setChecked(False)



    def Search(self):
        exp = '(?:[A-Za-z]\.)+|[A-Za-z]+[\-@]\d+(?:\.\d+)?|\d+[A-Za-z]+|\d+(?:[\.\,]\d+)?%?|\w+(?:[\-/]\w+)*'
        if self.index_check.isChecked() and not self.VSM.isChecked() and not self.BM.isChecked() and not self.boolean_model.isChecked() and not self.DMM.isChecked():
            if self.terms_per_doc.isChecked() and not self.docs_per_term.isChecked():
                text = self.entree.text()
                model = QStandardItemModel()
                model.setHorizontalHeaderLabels(['N°doc', 'Terme', 'Freq', 'Poids'])
                if self.tokenization.isChecked() and not self.Porter_stemmer.isChecked():
                    Lancaster = nltk.LancasterStemmer()
                    text = Lancaster.stem(text)
                    with open('./Index/DescripteursTokenLancaster', 'r') as file:
                        lines = file.readlines()
                        for line in lines:
                            if line.split()[0]==text:
                                item0=QStandardItem(str(line.split()[0]))
                                item1=QStandardItem(str(line.split()[1]))
                                item2=QStandardItem(str(line.split()[2]))
                                item3=QStandardItem(str(line.split()[3]))

                                item0.setTextAlignment(Qt.AlignCenter)
                                item1.setTextAlignment(Qt.AlignCenter)
                                item2.setTextAlignment(Qt.AlignCenter)
                                item3.setTextAlignment(Qt.AlignCenter)

                                model.appendRow([item0,item1, item2, item3])
                elif self.tokenization.isChecked() and self.Porter_stemmer.isChecked():
                    Porter = nltk.PorterStemmer()
                    text = Porter.stem(text)
                    with open('./Index/DescripteursTokenPorter', 'r') as file:
                        lines = file.readlines()
                        for line in lines:
                            if line.split()[0]==text:
                                item0=QStandardItem(str(line.split()[0]))
                                item1=QStandardItem(str(line.split()[1]))
                                item2=QStandardItem(str(line.split()[2]))
                                item3=QStandardItem(str(line.split()[3]))

                                item0.setTextAlignment(Qt.AlignCenter)
                                item1.setTextAlignment(Qt.AlignCenter)
                                item2.setTextAlignment(Qt.AlignCenter)
                                item3.setTextAlignment(Qt.AlignCenter)

                                model.appendRow([item0,item1, item2, item3])
                elif not self.tokenization.isChecked() and self.Porter_stemmer.isChecked():
                    Porter = nltk.PorterStemmer()
                    text = Porter.stem(text)
                    with open('./Index/DescripteursSplitPorter', 'r') as file:
                        lines = file.readlines()
                        for line in lines:
                            if line.split()[0]==text:
                                item0=QStandardItem(str(line.split()[0]))
                                item1=QStandardItem(str(line.split()[1]))
                                item2=QStandardItem(str(line.split()[2]))
                                item3=QStandardItem(str(line.split()[3]))

                                item0.setTextAlignment(Qt.AlignCenter)
                                item1.setTextAlignment(Qt.AlignCenter)
                                item2.setTextAlignment(Qt.AlignCenter)
                                item3.setTextAlignment(Qt.AlignCenter)

                                model.appendRow([item0,item1, item2, item3])
                elif not self.tokenization.isChecked() and not self.Porter_stemmer.isChecked():
                    with open('./Index/DescripteursSplitLancaster', 'r') as file:
                        lines = file.readlines()
                        for line in lines:
                            if line.split()[0]==text:
                                item0=QStandardItem(str(line.split()[0]))
                                item1=QStandardItem(str(line.split()[1]))
                                item2=QStandardItem(str(line.split()[2]))
                                item3=QStandardItem(str(line.split()[3]))

                                item0.setTextAlignment(Qt.AlignCenter)
                                item1.setTextAlignment(Qt.AlignCenter)
                                item2.setTextAlignment(Qt.AlignCenter)
                                item3.setTextAlignment(Qt.AlignCenter)

                                model.appendRow([item0,item1, item2, item3])
                self.result.setModel(model)
            elif not self.terms_per_doc.isChecked() and self.docs_per_term.isChecked():
                text = self.entree.text()
                model = QStandardItemModel()
                model.setHorizontalHeaderLabels(['Terme','N°doc', 'Freq', 'Poids'])
                if not self.tokenization.isChecked() and not self.Porter_stemmer.isChecked():
                    Lancaster = nltk.LancasterStemmer()
                    text=Lancaster.stem(text)
                    with open('./Index/InverseSplitLancaster', 'r') as file:
                        lines = file.readlines()
                        for line in lines:
                            if line.split()[0].lower() == text.lower():
                                item0 = QStandardItem(str(line.split()[0]))
                                item1 = QStandardItem(str(line.split()[1]))
                                item2 = QStandardItem(str(line.split()[2]))
                                item3 = QStandardItem(str(line.split()[3]))

                                item0.setTextAlignment(Qt.AlignCenter)
                                item1.setTextAlignment(Qt.AlignCenter)
                                item2.setTextAlignment(Qt.AlignCenter)
                                item3.setTextAlignment(Qt.AlignCenter)

                                model.appendRow([item0, item1, item2, item3])
                if self.tokenization.isChecked() and not self.Porter_stemmer.isChecked():
                    with open('./Index/InverseTokenLancaster', 'r') as file:
                        lines = file.readlines()
                        for line in lines:
                            if line.split()[0].lower() == text.lower():
                                item0 = QStandardItem(str(line.split()[0]))
                                item1 = QStandardItem(str(line.split()[1]))
                                item2 = QStandardItem(str(line.split()[2]))
                                item3 = QStandardItem(str(line.split()[3]))

                                item0.setTextAlignment(Qt.AlignCenter)
                                item1.setTextAlignment(Qt.AlignCenter)
                                item2.setTextAlignment(Qt.AlignCenter)
                                item3.setTextAlignment(Qt.AlignCenter)

                                model.appendRow([item0, item1, item2, item3])
                if not self.tokenization.isChecked() and self.Porter_stemmer.isChecked():
                    with open('./Index/InverseSplitPorter', 'r') as file:
                        lines = file.readlines()
                        for line in lines:
                            if line.split()[0].lower() == text.lower():
                                item0 = QStandardItem(str(line.split()[0]))
                                item1 = QStandardItem(str(line.split()[1]))
                                item2 = QStandardItem(str(line.split()[2]))
                                item3 = QStandardItem(str(line.split()[3]))

                                item0.setTextAlignment(Qt.AlignCenter)
                                item1.setTextAlignment(Qt.AlignCenter)
                                item2.setTextAlignment(Qt.AlignCenter)
                                item3.setTextAlignment(Qt.AlignCenter)

                                model.appendRow([item0, item1, item2, item3])
                if self.tokenization.isChecked() and self.Porter_stemmer.isChecked():
                    with open('./Index/InverseTokenPorter', 'r') as file:
                        lines = file.readlines()
                        for line in lines:
                            if line.split()[0].lower() == text.lower():
                                item0 = QStandardItem(str(line.split()[0]))
                                item1 = QStandardItem(str(line.split()[1]))
                                item2 = QStandardItem(str(line.split()[2]))
                                item3 = QStandardItem(str(line.split()[3]))

                                item0.setTextAlignment(Qt.AlignCenter)
                                item1.setTextAlignment(Qt.AlignCenter)
                                item2.setTextAlignment(Qt.AlignCenter)
                                item3.setTextAlignment(Qt.AlignCenter)

                                model.appendRow([item0, item1, item2, item3])
                self.result.setModel(model)
        elif not self.index_check.isChecked() and self.VSM.isChecked() and not self.BM.isChecked() and not self.boolean_model.isChecked() and not self.DMM.isChecked():
            if self.VS_choice.currentText()=='Scalar Product':
                text = self.entree.text()
                text=text.lower()
                model = QStandardItemModel()
                model.setHorizontalHeaderLabels(['N°doc', 'Relevance'])
                l= {}
                if not self.tokenization.isChecked() and not self.Porter_stemmer.isChecked() :
                    text=sentence_lancaster_stemming(text)
                    l=RSV(text,'./Index/DescripteursSplitLancaster','Scalar Product')
                    for key, value in l.items():
                        item0 = QStandardItem(str(key))
                        item1 = QStandardItem(str(value))

                        item0.setTextAlignment(Qt.AlignCenter)
                        item1.setTextAlignment(Qt.AlignCenter)

                        model.appendRow([item0, item1])
                elif self.tokenization.isChecked() and not self.Porter_stemmer.isChecked() :
                    text = sentece_token(text, exp)
                    text=sentence_lancaster_stemming(text)
                    l = RSV(text, './Index/DescripteursTokenLancaster', 'Scalar Product')
                    for key, value in l.items():
                        item0 = QStandardItem(str(key))
                        item1 = QStandardItem(str(value))

                        item0.setTextAlignment(Qt.AlignCenter)
                        item1.setTextAlignment(Qt.AlignCenter)

                        model.appendRow([item0, item1])
                elif not self.tokenization.isChecked() and self.Porter_stemmer.isChecked():
                    text = sentence_porter_stemming(text)
                    l = RSV(text, './Index/DescripteursSplitPorter', 'Scalar Product')
                    for key, value in l.items():
                        item0 = QStandardItem(str(key))
                        item1 = QStandardItem(str(value))

                        item0.setTextAlignment(Qt.AlignCenter)
                        item1.setTextAlignment(Qt.AlignCenter)

                        model.appendRow([item0, item1])
                elif self.tokenization.isChecked() and self.Porter_stemmer.isChecked():
                    text = sentece_token(text, exp)
                    text = sentence_porter_stemming(text)
                    l=RSV(text, './Index/DescripteursTokenPorter', 'Scalar Product')
                    for key, value in l.items():
                        item0 = QStandardItem(str(key))
                        item1 = QStandardItem(str(value))

                        item0.setTextAlignment(Qt.AlignCenter)
                        item1.setTextAlignment(Qt.AlignCenter)

                        model.appendRow([item0, item1])
                self.result.setModel(model)
            elif self.VS_choice.currentText() == 'Cosine Measure':
                text = self.entree.text()
                text = text.lower()
                model = QStandardItemModel()
                model.setHorizontalHeaderLabels(['N°doc', 'Relevance'])
                l = {}
                if not self.tokenization.isChecked() and not self.Porter_stemmer.isChecked() :
                    text=sentence_lancaster_stemming(text)
                    l=RSV(text,'./Index/DescripteursSplitLancaster','Cosine Measure')
                    for key, value in l.items():
                        item0 = QStandardItem(str(key))
                        item1 = QStandardItem(str(value))

                        item0.setTextAlignment(Qt.AlignCenter)
                        item1.setTextAlignment(Qt.AlignCenter)

                        model.appendRow([item0, item1])
                elif self.tokenization.isChecked() and not self.Porter_stemmer.isChecked() :
                    text = sentece_token(text, exp)
                    text=sentence_lancaster_stemming(text)
                    l=RSV(text,'./Index/DescripteursTokenLancaster','Cosine Measure')

                    for key, value in l.items():
                        item0 = QStandardItem(str(key))
                        item1 = QStandardItem(str(value))

                        item0.setTextAlignment(Qt.AlignCenter)
                        item1.setTextAlignment(Qt.AlignCenter)

                        model.appendRow([item0, item1])
                elif not self.tokenization.isChecked() and  self.Porter_stemmer.isChecked() :
                    text=sentence_porter_stemming(text)
                    l=RSV(text,'./Index/DescripteursSplitPorter','Cosine Measure')
                    for key, value in l.items():
                        item0 = QStandardItem(str(key))
                        item1 = QStandardItem(str(value))

                        item0.setTextAlignment(Qt.AlignCenter)
                        item1.setTextAlignment(Qt.AlignCenter)

                        model.appendRow([item0, item1])
                elif self.tokenization.isChecked() and self.Porter_stemmer.isChecked() :
                    text = sentece_token(text, exp)
                    text=sentence_porter_stemming(text)
                    l=RSV(text,'./Index/DescripteursTokenPorter','Cosine Measure')

                    for key, value in l.items():
                        item0 = QStandardItem(str(key))
                        item1 = QStandardItem(str(value))

                        item0.setTextAlignment(Qt.AlignCenter)
                        item1.setTextAlignment(Qt.AlignCenter)

                        model.appendRow([item0, item1])
                self.result.setModel(model)
            elif self.VS_choice.currentText() == 'Jaccard Measure':
                text = self.entree.text()
                text = text.lower()
                model = QStandardItemModel()
                model.setHorizontalHeaderLabels(['N°doc', 'Relevance'])
                l = {}
                if not self.tokenization.isChecked() and not self.Porter_stemmer.isChecked() :
                    text=sentence_lancaster_stemming(text)
                    l=RSV(text,'./Index/DescripteursSplitLancaster','Jaccard Measure')
                    for key, value in l.items():
                        item0 = QStandardItem(str(key))
                        item1 = QStandardItem(str(value))

                        item0.setTextAlignment(Qt.AlignCenter)
                        item1.setTextAlignment(Qt.AlignCenter)

                        model.appendRow([item0, item1])
                elif self.tokenization.isChecked() and not self.Porter_stemmer.isChecked() :
                    text = sentece_token(text, exp)
                    text=sentence_lancaster_stemming(text)
                    l=RSV(text,'./Index/DescripteursTokenLancaster','Jaccard Measure')

                    for key, value in l.items():
                        item0 = QStandardItem(str(key))
                        item1 = QStandardItem(str(value))

                        item0.setTextAlignment(Qt.AlignCenter)
                        item1.setTextAlignment(Qt.AlignCenter)

                        model.appendRow([item0, item1])
                elif not self.tokenization.isChecked() and  self.Porter_stemmer.isChecked() :
                    text=sentence_porter_stemming(text)
                    l=RSV(text,'./Index/DescripteursSplitPorter','Jaccard Measure')

                    for key, value in l.items():
                        item0 = QStandardItem(str(key))
                        item1 = QStandardItem(str(value))

                        item0.setTextAlignment(Qt.AlignCenter)
                        item1.setTextAlignment(Qt.AlignCenter)

                        model.appendRow([item0, item1])
                elif self.tokenization.isChecked() and self.Porter_stemmer.isChecked() :
                    text = sentece_token(text, exp)
                    text=sentence_porter_stemming(text)
                    l=RSV(text,'./Index/DescripteursTokenPorter','Jaccard Measure')

                    for key, value in l.items():
                        item0 = QStandardItem(str(key))
                        item1 = QStandardItem(str(value))

                        item0.setTextAlignment(Qt.AlignCenter)
                        item1.setTextAlignment(Qt.AlignCenter)

                        model.appendRow([item0, item1])
                self.result.setModel(model)
        elif not self.index_check.isChecked() and not self.VSM.isChecked() and self.BM.isChecked() and not self.boolean_model.isChecked() and not self.DMM.isChecked():
            text = self.entree.text()
            text = text.lower()
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(['N°doc', 'Relevance'])
            l = {}
            K = self.FactK.value()
            B = self.FactB.value()
            if not self.tokenization.isChecked() and not self.Porter_stemmer.isChecked():
                text = sentence_lancaster_stemming(text)
                l= RSV_BM25(text, './Index/DescripteursSplitLancaster',K,B)
                for key, value in l.items():
                    item0 = QStandardItem(str(key))
                    item1 = QStandardItem(str(value))

                    item0.setTextAlignment(Qt.AlignCenter)
                    item1.setTextAlignment(Qt.AlignCenter)

                    model.appendRow([item0, item1])
            elif self.tokenization.isChecked() and not self.Porter_stemmer.isChecked():
                text = sentence_lancaster_stemming(text)
                l= RSV_BM25(text,  './Index/DescripteursTokenLancaster',K,B)
                for key, value in l.items():
                    item0 = QStandardItem(str(key))
                    item1 = QStandardItem(str(value))

                    item0.setTextAlignment(Qt.AlignCenter)
                    item1.setTextAlignment(Qt.AlignCenter)

                    model.appendRow([item0, item1])
            elif not self.tokenization.isChecked() and self.Porter_stemmer.isChecked():

                text = sentence_porter_stemming(text)
                l = RSV_BM25(text,  './Index/DescripteursSplitPorter',K,B)
                for key, value in l.items():
                    item0 = QStandardItem(str(key))
                    item1 = QStandardItem(str(value))

                    item0.setTextAlignment(Qt.AlignCenter)
                    item1.setTextAlignment(Qt.AlignCenter)

                    model.appendRow([item0, item1])
            elif self.tokenization.isChecked() and self.Porter_stemmer.isChecked():
                text = sentence_porter_stemming(text)
                l = RSV_BM25(text, './Index/DescripteursTokenPorter',K,B)
                for key, value in l.items():
                    item0 = QStandardItem(str(key))
                    item1 = QStandardItem(str(value))

                    item0.setTextAlignment(Qt.AlignCenter)
                    item1.setTextAlignment(Qt.AlignCenter)

                    model.appendRow([item0, item1])
            self.result.setModel(model)
        elif not self.index_check.isChecked() and not self.VSM.isChecked() and not self.BM.isChecked() and self.boolean_model.isChecked() and not self.DMM.isChecked():
            text = self.entree.text()
            text = text.lower()
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(['N°doc', 'Relevance'])
            l = {}
            if not self.tokenization.isChecked() and not self.Porter_stemmer.isChecked():
                text = sentence_lancaster_stemming(text)

                l=RSV_Bool(text, './Index/DescripteursSplitLancaster')
                l = dict(sorted(l.items(), key=lambda item: item[1], reverse=True))
                l = {key: 'YES' if value == 1 else value for key, value in l.items()}
                l = {key: 'NO' if value == 0 else value for key, value in l.items()}
                l = {key: 'Error Syntaxe' if value == 2 else value for key, value in l.items()}
                for key, value in l.items():
                    item0 = QStandardItem(str(key))
                    item1 = QStandardItem(str(value))

                    item0.setTextAlignment(Qt.AlignCenter)
                    item1.setTextAlignment(Qt.AlignCenter)

                    model.appendRow([item0, item1])
            elif self.tokenization.isChecked() and not self.Porter_stemmer.isChecked():
                text = sentence_lancaster_stemming(text)

                l=RSV_Bool(text, './Index/DescripteursTokenLancaster')
                l = dict(sorted(l.items(), key=lambda item: item[1], reverse=True))
                l = {key: 'YES' if value == 1 else value for key, value in l.items()}
                l = {key: 'NO' if value == 0 else value for key, value in l.items()}
                l = {key: 'Error Syntaxe' if value == 2 else value for key, value in l.items()}
                for key, value in l.items():
                    item0 = QStandardItem(str(key))
                    item1 = QStandardItem(str(value))

                    item0.setTextAlignment(Qt.AlignCenter)
                    item1.setTextAlignment(Qt.AlignCenter)

                    model.appendRow([item0, item1])
            elif not self.tokenization.isChecked() and self.Porter_stemmer.isChecked():
                text = sentence_porter_stemming(text)
                l= RSV_Bool(text, './Index/DescripteursSplitPorter')
                l = dict(sorted(l.items(), key=lambda item: item[1], reverse=True))
                l = {key: 'YES' if value == 1 else value for key, value in l.items()}
                l = {key: 'NO' if value == 0 else value for key, value in l.items()}
                l = {key: 'Error Syntaxe' if value == 2 else value for key, value in l.items()}
                for key, value in l.items():
                    item0 = QStandardItem(str(key))
                    item1 = QStandardItem(str(value))

                    item0.setTextAlignment(Qt.AlignCenter)
                    item1.setTextAlignment(Qt.AlignCenter)

                    model.appendRow([item0, item1])
            elif self.tokenization.isChecked() and self.Porter_stemmer.isChecked():
                text = sentence_porter_stemming(text)
                l= RSV_Bool(text,  './Index/DescripteursTokenPorter')
                l = dict(sorted(l.items(), key=lambda item: item[1], reverse=True))
                l = {key: 'YES' if value == 1 else value for key, value in l.items()}
                l = {key: 'NO' if value == 0 else value for key, value in l.items()}
                l = {key: 'Error Syntaxe' if value == 2 else value for key, value in l.items()}
                for key, value in l.items():
                    item0 = QStandardItem(str(key))
                    item1 = QStandardItem(str(value))

                    item0.setTextAlignment(Qt.AlignCenter)
                    item1.setTextAlignment(Qt.AlignCenter)

                    model.appendRow([item0, item1])
            self.result.setModel(model)
        elif not self.index_check.isChecked() and not self.boolean_model.isChecked() and self.DMM.isChecked():
            if self.VSM.isChecked() and not self.BM.isChecked():
                RSV_list={}
                if self.VS_choice.currentText() == 'Scalar Product':
                    text = self.entree.text()
                    text = text.lower()
                    model = QStandardItemModel()
                    model.setHorizontalHeaderLabels(['N°doc', 'Relevance'])
                    l = {}
                    if not self.tokenization.isChecked() and not self.Porter_stemmer.isChecked():
                        text = sentence_lancaster_stemming(text)
                        l = RSV(text, './Index/DescripteursSplitLancaster', 'Scalar Product')
                        RSV_list=l
                        for key, value in l.items():
                            item0 = QStandardItem(str(key))
                            item1 = QStandardItem(str(value))

                            item0.setTextAlignment(Qt.AlignCenter)
                            item1.setTextAlignment(Qt.AlignCenter)

                            model.appendRow([item0, item1])
                    elif self.tokenization.isChecked() and not self.Porter_stemmer.isChecked():
                        text = sentece_token(text, exp)
                        text = sentence_lancaster_stemming(text)
                        l = RSV(text, './Index/DescripteursTokenLancaster', 'Scalar Product')
                        RSV_list=l
                        for key, value in l.items():
                            item0 = QStandardItem(str(key))
                            item1 = QStandardItem(str(value))

                            item0.setTextAlignment(Qt.AlignCenter)
                            item1.setTextAlignment(Qt.AlignCenter)

                            model.appendRow([item0, item1])
                    elif not self.tokenization.isChecked() and self.Porter_stemmer.isChecked():
                        text = sentence_porter_stemming(text)
                        l = RSV(text, './Index/DescripteursSplitPorter', 'Scalar Product')
                        RSV_list=l
                        for key, value in l.items():
                            item0 = QStandardItem(str(key))
                            item1 = QStandardItem(str(value))

                            item0.setTextAlignment(Qt.AlignCenter)
                            item1.setTextAlignment(Qt.AlignCenter)

                            model.appendRow([item0, item1])
                    elif self.tokenization.isChecked() and self.Porter_stemmer.isChecked():
                        text = sentece_token(text, exp)
                        text = sentence_porter_stemming(text)
                        l = RSV(text, './Index/DescripteursTokenPorter', 'Scalar Product')
                        RSV_list = l
                        for key, value in l.items():
                            item0 = QStandardItem(str(key))
                            item1 = QStandardItem(str(value))

                            item0.setTextAlignment(Qt.AlignCenter)
                            item1.setTextAlignment(Qt.AlignCenter)

                            model.appendRow([item0, item1])
                    self.result.setModel(model)
                elif self.VS_choice.currentText() == 'Cosine Measure':
                    text = self.entree.text()
                    text = text.lower()
                    model = QStandardItemModel()
                    model.setHorizontalHeaderLabels(['N°doc', 'Relevance'])
                    l = {}
                    if not self.tokenization.isChecked() and not self.Porter_stemmer.isChecked():
                        text = sentence_lancaster_stemming(text)
                        l = RSV(text, './Index/DescripteursSplitLancaster', 'Cosine Measure')
                        RSV_list = l
                        for key, value in l.items():
                            item0 = QStandardItem(str(key))
                            item1 = QStandardItem(str(value))

                            item0.setTextAlignment(Qt.AlignCenter)
                            item1.setTextAlignment(Qt.AlignCenter)

                            model.appendRow([item0, item1])
                    elif self.tokenization.isChecked() and not self.Porter_stemmer.isChecked():
                        text = sentece_token(text, exp)
                        text = sentence_lancaster_stemming(text)
                        l = RSV(text, './Index/DescripteursTokenLancaster', 'Cosine Measure')
                        RSV_list = l
                        for key, value in l.items():
                            item0 = QStandardItem(str(key))
                            item1 = QStandardItem(str(value))

                            item0.setTextAlignment(Qt.AlignCenter)
                            item1.setTextAlignment(Qt.AlignCenter)

                            model.appendRow([item0, item1])
                    elif not self.tokenization.isChecked() and self.Porter_stemmer.isChecked():
                        text = sentence_porter_stemming(text)
                        l = RSV(text, './Index/DescripteursSplitPorter', 'Cosine Measure')
                        RSV_list = l
                        for key, value in l.items():
                            item0 = QStandardItem(str(key))
                            item1 = QStandardItem(str(value))

                            item0.setTextAlignment(Qt.AlignCenter)
                            item1.setTextAlignment(Qt.AlignCenter)

                            model.appendRow([item0, item1])
                    elif self.tokenization.isChecked() and self.Porter_stemmer.isChecked():
                        text = sentece_token(text, exp)
                        text = sentence_porter_stemming(text)
                        l = RSV(text, './Index/DescripteursTokenPorter', 'Cosine Measure')
                        RSV_list = l
                        for key, value in l.items():
                            item0 = QStandardItem(str(key))
                            item1 = QStandardItem(str(value))

                            item0.setTextAlignment(Qt.AlignCenter)
                            item1.setTextAlignment(Qt.AlignCenter)

                            model.appendRow([item0, item1])
                    self.result.setModel(model)
                elif self.VS_choice.currentText() == 'Jaccard Measure':
                    text = self.entree.text()
                    text = text.lower()
                    model = QStandardItemModel()
                    model.setHorizontalHeaderLabels(['N°doc', 'Relevance'])
                    l = {}
                    if not self.tokenization.isChecked() and not self.Porter_stemmer.isChecked():
                        text = sentence_lancaster_stemming(text)
                        l = RSV(text, './Index/DescripteursSplitLancaster', 'Jaccard Measure')
                        RSV_list = l
                        for key, value in l.items():
                            item0 = QStandardItem(str(key))
                            item1 = QStandardItem(str(value))

                            item0.setTextAlignment(Qt.AlignCenter)
                            item1.setTextAlignment(Qt.AlignCenter)

                            model.appendRow([item0, item1])
                    elif self.tokenization.isChecked() and not self.Porter_stemmer.isChecked():
                        text = sentece_token(text, exp)
                        text = sentence_lancaster_stemming(text)
                        l = RSV(text, './Index/DescripteursTokenLancaster', 'Jaccard Measure')
                        RSV_list = l
                        for key, value in l.items():
                            item0 = QStandardItem(str(key))
                            item1 = QStandardItem(str(value))

                            item0.setTextAlignment(Qt.AlignCenter)
                            item1.setTextAlignment(Qt.AlignCenter)

                            model.appendRow([item0, item1])
                    elif not self.tokenization.isChecked() and self.Porter_stemmer.isChecked():
                        text = sentence_porter_stemming(text)
                        l = RSV(text, './Index/DescripteursSplitPorter', 'Jaccard Measure')
                        RSV_list = l
                        for key, value in l.items():
                            item0 = QStandardItem(str(key))
                            item1 = QStandardItem(str(value))

                            item0.setTextAlignment(Qt.AlignCenter)
                            item1.setTextAlignment(Qt.AlignCenter)

                            model.appendRow([item0, item1])
                    elif self.tokenization.isChecked() and self.Porter_stemmer.isChecked():
                        text = sentece_token(text, exp)
                        text = sentence_porter_stemming(text)
                        l = RSV(text, './Index/DescripteursTokenPorter', 'Jaccard Measure')
                        RSV_list = l
                        for key, value in l.items():
                            item0 = QStandardItem(str(key))
                            item1 = QStandardItem(str(value))

                            item0.setTextAlignment(Qt.AlignCenter)
                            item1.setTextAlignment(Qt.AlignCenter)

                            model.appendRow([item0, item1])
                    self.result.setModel(model)
                judg_load=judgments_load('./Judgements/Judgements')

                MPrecision(judg_load[str(self.query_dst.value())], RSV_list, self.p5, self.p10, self.precision, self.recall, self.fscore,self.plot_widget)


if __name__ == '__main__':
    path = "./Collection"
    path_out = "./Index"
    #exp = '(?:[A-Z]\.)+|\d+(?:\.\d+)?DA?|\w+|\.{3}'
    exp = '(?:[A-Za-z]\.)+|[A-Za-z]+[\-@]\d+(?:\.\d+)?|\d+[A-Za-z]+|\d+(?:[\.\,]\d+)?%?|\w+(?:[\-/]\w+)*'

    # Descripteur(path, path_out, 'split', 'Lanaster', '')
    # Descripteur(path, path_out, 'Token', 'Lanaster', exp)
    # Descripteur(path, path_out, 'split', 'Porter', '')
    # Descripteur(path, path_out, 'Token', 'Porter', exp)
    #
    # Inverse(path, path_out, 'split', 'Lanaster', '')
    # Inverse(path, path_out, 'Token', 'Lanaster', exp)
    # Inverse(path, path_out, 'split', 'Porter', '')
    # Inverse(path, path_out, 'Token', 'Porter', exp)
    #
    # update_poids_descripteur("./Index/DescripteursSplitPorter")
    # update_poids_descripteur("./Index/DescripteursTokenPorter")
    # update_poids_descripteur("./Index/DescripteursSplitLancaster")
    # update_poids_descripteur("./Index/DescripteursTokenLancaster")
    #
    # update_poids_inverse("./Index/InverseSplitPorter")
    # update_poids_inverse("./Index/InverseTokenPorter")
    # update_poids_inverse("./Index/InverseSplitLancaster")
    # update_poids_inverse("./Index/InverseTokenLancaster")

    app=QApplication(sys.argv)
    mainWindow=mainWindow()
    mainWindow.show()
    sys.exit(app.exec_())