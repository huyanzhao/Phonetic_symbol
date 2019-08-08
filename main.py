# -*- coding: utf-8 -*-
# !/usr/bin/python3
import os
import copy
import sys
import time
from urllib import request, parse
import json
from PyQt4.QtGui import *
import widget


class MainWindow(QWidget, widget.Ui_Form):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.file = None
        self.path = None
        self.file_name = None
        self.content = None
        self.log_file = None
        self.result_file = None

        self.connect_solt()

    def connect_solt(self):
        self.pushButton_import.clicked.connect(self.on_pushButton_import_click)
        self.pushButton_start.clicked.connect(self.on_pushButton_start_click)
        self.pushButton_log.clicked.connect(self.on_pushButton_log_click)

    def on_pushButton_import_click(self):
        self.file = QFileDialog().getOpenFileName(self, 'Open file', 'd:/Art/')
        self.path, self.file_name = os.path.split(self.file)
        with open(self.file, 'r') as fp:
            self.content = fp.read()
        self.textBrowser_detail.append("当前路径：%s, 当前文件：%s，文件大小：%d" % (self.path, self.file_name, len(self.content)))

    def on_pushButton_start_click(self):
        start = time.time()
        if self.file is None:
            return
        file_name, tail = os.path.splitext(self.file_name)
        self.log_file = 'log/' + file_name + '.log'
        with open(self.log_file, 'w', encoding='utf-8') as fp:
            fp.write(self.file_name)
        self.result_file = os.path.join(self.path, file_name + '_phonetic' + tail)
        with open('dictionary.json', 'r') as fp:
            dictionary = json.load(fp)

        seq_list = ['\n', '.', '!', '?']
        sentence_list = [self.content]
        for seq in seq_list:
            self.log("分割符：%s" % seq)
            result_list = []
            for sentence in sentence_list:
                sentence_list_temp = sentence.split(seq)
                self.progressBar.setMaximum(len(sentence_list))
                i = 0
                for item in sentence_list_temp:
                    item = item.strip(' ')
                    item = item.strip('\'')
                    item = item.strip('"')
                    i += 1
                    self.progressBar.setValue(i)
                    if item != '':
                        result_list.append(item.strip())
                        self.log("得到语句：%s" % item)
                        self.textBrowser.append(item)
            sentence_list = copy.deepcopy(result_list)
            self.log("共得到%d句文本" % len(sentence_list))
            result_list.clear()
            self.textBrowser.clear()

        base_url = "http://fy.iciba.com/ajax.php?a=fy"
        header = {
            "User-Agent": " Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        query = {
            "f": "auto",
            "t": "auto",
        }
        phoneticed_text = ""
        while sentence_list:
            sentence = sentence_list.pop(0)
            phonetic = ''
            self.textBrowser.setText(phoneticed_text + sentence)
            self.log("开始解析语句：%s" % sentence)
            clause_list = sentence.split(',')
            self.log("使用逗号分割后得到%d个分句：%s" % (len(clause_list), str(clause_list)))
            for clause in clause_list:
                word_list = clause.strip().strip('\'').split(' ')
                phonetic += '['
                self.textBrowser.setText(phoneticed_text + phonetic + '\r\n' + sentence)
                self.log("使用空格分割得到%d个单词：%s" % (len(word_list), str(word_list)))
                self.progressBar.setMaximum(len(word_list))
                i = 0
                for word in word_list:
                    if word.strip('\'') == "":
                        continue
                    if word not in dictionary.keys():
                        word = word.strip(':')
                        self.log("开始翻译%s" % word)
                        query['w'] = word
                        data = parse.urlencode(query)
                        response = request.Request(url=base_url, headers=header, data=bytes(data, encoding="utf-8"))
                        time.sleep(0.1)
                        req = request.urlopen(response).read().decode("utf-8")
                        obj = json.loads(req)
                        self.log("%s的翻译结果：%s" % (word, obj['content']))
                        if 'ph_en' not in obj['content'].keys():
                            print(word, obj['content'])
                            continue
                        ph_en = obj['content']['ph_en']
                        ph_en = ph_en.replace('(', '').replace(')', '')
                        if ph_en != '':
                            dictionary[word] = ph_en
                    else:
                        ph_en = dictionary[word]
                    phonetic += ' ' + ph_en + ' '
                    self.textBrowser.setText(phoneticed_text + phonetic + '\r\n' + sentence)
                    i += 1
                    self.progressBar.setValue(i)
                phonetic += ']'
                self.textBrowser.setText(phoneticed_text + phonetic + '\r\n' + sentence)
            phoneticed_text += phonetic + '\r\n' + sentence + '\r\n'
            with open(self.result_file, 'w', encoding="utf-8") as fp:
                fp.write(phoneticed_text)
        with open('dictionary.json', 'w') as fp:
            json.dump(dictionary, fp)
        self.log("标注音标完毕！耗时：%f秒" % (time.time()-start))

    def on_pushButton_log_click(self):
        os.startfile(self.path + '/' + self.log_file)

    def log(self, message):
        with open(self.log_file, 'a', encoding='utf-8') as fp:
            fp.write(message + '\r\n')
        self.textBrowser_detail.append(message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
