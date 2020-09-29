import itertools

char_List= []
while True:
  char_input = input('(For stop, enter 0!) Char: ')
  if char_input == '0':
    print(f'Char List: {char_List}')
    break
  else:
    for i in char_input:
      char_List.append(i)

n = len(char_List)
word = ''
word_List = set()

for xs in itertools.permutations(char_List):
    word += ''.join(xs)
    word_List.add(word)
    word = ''

def order(liste):
    liste = list(liste)
    liste.sort()
    for i in liste:
      print(i)

order(word_List)
cikis = input('For exit press a button...')
