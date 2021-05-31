def isVowel(sym):
    vowels = ['�','�','�','�','�','�','�','�','�','�']
    if sym in vowels:
        return True
    else:
        return False
    
def main():
    #�������� �������� ���������� ����� �� ������
    try:
        inFile = open('text.txt')
    except:
        print('������ - ���� �� ����������.')
        return 1
    #�������� ��������� ���������� ����� �� ������
    outFile = open('text01.txt','w')
    #��������� ���� ��������� � ������
    text = inFile.readlines()
    #������������ ������ ����� �����������
    for string in text:
        #������� ���������� ������� � ������ ������
        newString = string.lstrip()
        #���� ������ ������ ����� ������ "-", �� ������� �������� ������
        if newString[0] == '-':
            print(string)
        #��������� ������ �� �����, ����� ��������� � ������
        wordsList = string.split()
        #������������ ������ ���� � ������ �����������
        for word in wordsList:
            #���� ������ ������ ����� ������� �����
            if isVowel(word[0]):
                #�� ������ ������ ����� �� ��������� + ���������� ������� �����
                #����� ������������ ������ � �������� ����
                outFile.write(word[0].upper()+word[1:len(word)]+'\n')
    inFile.close()
    outFile.close()
    #�������� ��������� ���������� ����� �� ��������
    outFile = open('text01.txt','a')
    outFile.write('\n��������� ������ ����� ������\n')
    outFile.close()

if __name__ == "__main__":
    main()
