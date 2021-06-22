class Main:
    def __init__(self,file):
        self.File = file

    def prefix(self):
        count = 0
        for i in range(len(self.File)):
            if (i != 0):
                if words[i - 1] == 'to':
                    count += 1
        print(count)

    def endsWith(self):
        count2 = 0
        for i in range(len(self.File)):
            if words[i].endswith("ing"):
                count2 += 1
        print(count2)

    def Maximum(self):
        word = []
        index = []
        index2 = []
        new_list = []
        for i in range(len(self.File)):
            val = self.File.count(self.File[i])
            word.append(self.File[i])
            index.append(val)

        max1 = max(index)
        for i in range(len(index)):
            if (index[i] == max1):
                index2.append(i)

        for i in range(len(index2)):
            new_list.append(word[index2[i]])
        set1 = set(new_list)
        new_list = list(set1)
        print(new_list)

    def Palindrome(self):
         palindrome = 0
         for i in range(len(self.File)):
             if (self.File[i][::-1] == self.File[i]):
                 print(self.File[i])
                 palindrome += 1
             if (i == len(self.File) - 1 and palindrome == 0):
                 print("No Palindrome")

    def Unique(self):
        set1 = set(self.File)
        list2 = list(set1)
        print(list2)
    def Dict(self):
        Word = dict()

        for line in lines:

            line = line.strip()

            line = line.lower()

            words = line.split(" ")

            for word in self.File:
                print(word)
                if word in Word:

                    Word[word] = Word[word] + 1

                else:

                    Word[word] = 1

        for key in list(Word.keys()):
            print(key, ":", Word[key])

try:
    with open("py.txt", 'r') as f:
        lines = f.readlines()
        words = []

        for line in lines:
            arr = [str for str in line.split()]
            words.extend(arr)
    result = Main(words)
    while (True):
        print("1.Prefix To")
        print("2.Ending with ing")
        print("3.Maximum Elements")
        print("4.Palindrome")
        print("5.Unique List")
        print("6.Dict")
        print("7.Stop")

        num = int(input("Enter the number "))
        if (num == 1):
            result.prefix()
        elif (num == 2):
            result.endsWith()
        elif (num == 3):
            result.Maximum()
        elif (num == 4):
            result.Palindrome()
        elif (num == 5):
            result.Unique()
        elif (num == 6):
            result.Dict()
        elif (num == 7):
            break

except:
    print("File Not Found")
