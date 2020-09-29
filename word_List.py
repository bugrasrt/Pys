from itertools import permutations

while True:
    words = input('Enter the words(For exit, enter 0): ')
    if words == '0':
        exit(1)
    else:
        char_List = [char for char in words]

    word = ''
    word_List = set()

    for xs in permutations(char_List):
        word += ''.join(xs)
        word_List.add(word)
        word = ''

    def order(liste):
        liste = list(liste)
        liste.sort()
        for i in liste:
          print(i)

    order(word_List)
    cikis = input('For exit enter 0, otherwise press any key: ')
    if cikis == '0':
        exit(1)
    else:
        pass
