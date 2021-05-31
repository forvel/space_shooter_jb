def isVowel(sym):
    vowels = ['а','я','ы','у','э','е','ё','и','о','ю']
    if sym in vowels:
        return True
    else:
        return False
    
def main():
    #открытие входного текстового файла на чтения
    try:
        inFile = open('text.txt')
    except:
        print('Ошибка - файл не существует.')
        return 1
    #открытие выходного текстового файла на запись
    outFile = open('text01.txt','w')
    #считываем файл построчно в список
    text = inFile.readlines()
    #обрабатываем список строк поэлементно
    for string in text:
        #удаляем пробельные символы в начале строки
        newString = string.lstrip()
        #если первый символ новой строки "-", то выводим исходную строку
        if newString[0] == '-':
            print(string)
        #разбиваем строку на слова, слова сохраняем в список
        wordsList = string.split()
        #обрабатываем список слов в строке поэлементно
        for word in wordsList:
            #если первый символ слова гласная буква
            if isVowel(word[0]):
                #то меняем первую букву на прописную + дописываем остаток слова
                #пишем получившуюся строку в выходной файл
                outFile.write(word[0].upper()+word[1:len(word)]+'\n')
    inFile.close()
    outFile.close()
    #открытие выходного текстового файла на дозапись
    outFile = open('text01.txt','a')
    outFile.write('\nПрограмму создал Некто Нектов\n')
    outFile.close()

if __name__ == "__main__":
    main()
