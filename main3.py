import re
import random
import string
try:
    with open('py.txt','r') as f:
        lines = f.readlines()

        words = []

        words2 = []
        list5 = []
        list4 = []
        str1 = ''
        str3 = ''

        for line in lines:
            arr = [str for str in line.split()]
            words.extend(arr)
            words2.extend(arr)

        for i in range(len(words2)):
            word1 = words2[i]
            result = re.split('a|e|i|o|u', word1)
            list5.append(result)
        print(list5)

        for i in range(len(words)):
            words[i] = words[i].lower()
            for j in range(len(words[i])):
                if j == 2:
                    str1 += chr(ord(words[i][j]) - 32)
                else:
                    str1 += words[i][j]
                    if j == len(words[i]) - 1:
                        str1 += ' '
        print(str1)

        lenght = 5
        name = ''.join([random.choice(string.ascii_letters) for _ in range(lenght)])

        str4 = ''
        for i in range(len(list5)):
            for j in range(len(list5[i])):
                str4 += list5[i][j]
                if j == len(list5[i])-1:
                    str4 += ' '

        for i in range(len(words)):
            if i % 5 == 4:
                words[i] = words[i].upper()
        print(words)

        str2 = ' '.join(words2)

        for i in range(len(str2)):
            if str2[i] == ' ':
                str3 += '-'
            else:
                str3 += str2[i]
        print(str3)

        for i in range(len(lines)):
            if (len(lines) > 1):
                if i != len(lines) - 1:
                    list4.append(lines[i] + ";")
                else:
                    list4.append(lines[i])
            else:
                list4.append(lines[i])
        print(list4)

        with open(name+".txt","w") as f:
            for word in str4:
                f.write(word)
            f.write("\n")

            for word in str1:
                f.write(word)
            f.write("\n")

            for word in words:
                f.write(word+" ")
            f.write("\n")

            for word in str3:
                f.write(word)
            f.write("\n")

            for word in list4:
                f.write(word+" ")
            f.write("\n")




except:
    print('No File')
