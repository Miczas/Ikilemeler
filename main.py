def find_double_words(input_file: str, output_file: str) -> None:
    """
    Reads the input_file line by line and writes lines containing
    Turkish double words (ikileme) to the output_file.
    """
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            words = line.strip().split()
            if words and words.count(words[0]) > 1:
                outfile.write(line)

if __name__ == '__main__':
    find_double_words('words.txt', 'FirstIkilemeDictionary.txt')