try:
    with open("py.txt", 'r') as f:
        lines = f.readlines()

        words = []

        for line in lines:
            arr = [str for str in line.split()]
            words.extend(arr)


        while(True):
            print("1.Prefix To")
            print("2.Ending with ing")
            print("3.Maximum Elements")
            print("4.Palindrome")
            print("5.Unique List")
            print("6.Dict")
            print("7.Stop")

            num = int(input("Enter the number "))

            if(num == 1):
                count = 0
                for i in range(len(words)):
                    if (i != 0):
                        if words[i - 1] == 'to':
                            count += 1
                print(count)

            elif(num == 2):
                count2 = 0
                for i in range(len(words)):
                    if words[i].endswith("ing"):
                        count2 += 1
                print(count2)

            elif(num == 3):
                word = []
                index = []
                index2 = []
                count3 = 0
                for i in range(len(words)):
                    val = words.count(words[i])
                    word.append(words[i])
                    index.append(val)

                max1 = max(index)
                for i in range(len(index)):
                    if (index[i] == max1):
                        index2.append(i)

                for i in range(len(index2)):
                    print(word[index2[i]])

            elif(num == 4):
                palindrome = 0
                for i in range(len(words)):
                    if (words[i][::-1] == words[i]):
                        print(words[i])
                        palindrome += 1
                    if (i == len(words) - 1 and palindrome == 0):
                        print("No Palindrome")


            elif(num == 5):
                set1 = set(words)
                list2 = list(set1)
                print(list2)

            elif(num == 6):
                Word = dict()

                for line in lines:

                    line = line.strip()

                    line = line.lower()

                    words = line.split(" ")

                    for word in words:
                        print(word)
                        if word in Word:

                            Word[word] = Word[word] + 1

                        else:

                            Word[word] = 1

                for key in list(Word.keys()):
                    print(key, ":", Word[key])

            elif(num == 7):
                break

except:
    print("File Not Found")