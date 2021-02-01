def compressioin(file):
    with open(file, 'r') as inputfile:
        text = inputfile.readlines()
    text.remove('\n')
    text = ''.join([line.lstrip() for line in text if line != '\n'])
    newfile = '{}Output{}'.format(file[:-4], file[-4:])
    with open(newfile, 'w') as outputfile:
        outputfile.write(text)


compressioin('Test.txt')