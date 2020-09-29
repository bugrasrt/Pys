from itertools import permutations

# Enter several word or letter then it will create unique words then sort it.
# You can write it to your txt file

def word_create():
    words = input('Enter the words(Exit 0): ')
    if words == '0':
        exit(1)
    else:
        char_List = [char if char != ' ' else '' for char in words]

    word = ''
    word_List = set()

    for xs in permutations(char_List):
        word += ''.join(xs)
        word_List.add(word)
        word = ''
        
    return word_List

def list_order(input_List):
    sorted_List = list(input_List)
    sorted_List.sort()
    for word in sorted_List:
        print(word)
            
    return sorted_List

def file_create(input_List):
    file = open(r'C:/Users/Bugra/Desktop/my_word_List.txt', 'a+')
    file.write('####New List####\n')
    for word in input_List:
          file.write(f'{word}\n')
    file.write('\n')
    file.close()


while True:
    words = word_create()
    sorted_List = list_order(words)
    
    choose = input('Exit(0) or Write_to_File(1), otherwise press any key: ')
    if choose == '0':
        break
    elif choose == '1':
        file_create(sorted_List)
    else:
        pass
