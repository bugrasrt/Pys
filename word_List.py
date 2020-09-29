from itertools import permutations

# Enter several word or letter then it will create unique words then sort it.
while True:
    words = input('Enter the words(For exit, enter 0): ')
    if words == '0':
        break
    else:
        char_List = [char if char != ' ' else '' for char in words]

    word = ''
    word_List = set()

    for xs in permutations(char_List):
        word += ''.join(xs)
        word_List.add(word)
        word = ''

    def order(input_List):
        sorted_List = list(input_List)
        sorted_List.sort()
        for word in sorted_List:
          print(word)

    order(word_List)
    
    exit = input('For exit enter 0, otherwise press any key: ')
    if exit == '0':
        break
    else:
        pass
