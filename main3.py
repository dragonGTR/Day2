import re
import random
import string

class Main:
    def __init__(self, file):
        self.File = file

    def splitVowels(self,words):
        str4 = ''
        for i in range(len(words2)):
            word1 = self.File[i]
            result = re.split('a|e|i|o|u', word1)
            list5.append(result)
        for i in range(len(list5)):
            for j in range(len(list5[i])):
                str4 += list5[i][j]
                if j == len(list5[i])-1:
                    str4 += ' '
        return str4

    def Capital(self, words):
        str1 = ''
        for i in range(len(words)):
            words[i] = words[i].lower()
            for j in range(len(words[i])):
                if j == 2:
                    str1 += chr(ord(words[i][j]) - 32)
                else:
                    str1 += words[i][j]
                    if j == len(words[i]) - 1:
                        str1 += ' '
        return str1

    def Capital2(self,words):
        for i in range(len(words)):
            if i % 5 == 4:
                words[i] = words[i].upper()
        str2 = ' '.join(words)
        return str2

    def new_Line(self,words2):
        str2 = ' '.join(words2)
        str3 = ''
        for i in range(len(str2)):
            if str2[i] == ' ':
                str3 += '-'
            else:
                str3 += str2[i]
        return str3

    def semiColon(self,lines):
        for i in range(len(lines)):
            if (len(lines) > 1):
                if i != len(lines) - 1:
                    list4.append(lines[i] + ";")
                else:
                    list4.append(lines[i])
            else:
                list4.append(lines[i])
        print(list4)

try:
    with open("py.txt", 'r') as f:
        lines = f.readlines()

        words = []
        str4 = ''
        words2 = []
        list5 = []
        list4 = []
        str1 = ''
        str3 = ''
        str2 = ''

        for line in lines:
            arr = [str for str in line.split()]
            words.extend(arr)
            words2.extend(arr)
    result = Main(words)
    str4 = result.splitVowels(words2)
    str1 = result.Capital(words)
    str2 = result.Capital2(words)
    str3 = result.new_Line(words2)
    result.semiColon(lines)

    lenght = 5
    name = ''.join([random.choice(string.ascii_letters) for _ in range(lenght)])

    with open(name + ".txt", "w") as f:
        for word in str4:
            f.write(word)
        f.write("\n")

        for word in str1:
            f.write(word)
        f.write("\n")

        for word in words:
            f.write(word + " ")
        f.write("\n")

        for word in str3:
            f.write(word)
        f.write("\n")

        for word in list4:
            f.write(word + " ")
        f.write("\n")




except:
    print("File Not Found")

