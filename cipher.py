text = 'Hello World'
shift = 1
alphabet = 'abcdefghijklmnopqrstuvwxyz'
new_char = ''

for char in text.lower():
    index = alphabet.find(char)
    new_index = (index - 5) + shift
    new_char =  new_char + alphabet[new_index]
    print('char:',char,'new char:',new_char);