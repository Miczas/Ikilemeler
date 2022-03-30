


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file2 = open("FirstIkilemeDictionary.txt", "w", encoding='utf-8')
    file1 = open('words.txt', 'r', encoding='utf-8')
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        words = line.split()
        if (words.count(words[0])>1):
            file2.write(line)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
