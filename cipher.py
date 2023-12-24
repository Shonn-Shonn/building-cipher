text = 'Hello World boby weight'
characters = 'abcdefghijklmnopqurstuvwxyz'
shift = 3
encrypted_text = ' '
for char in text.lower():
    if char == ' ':
        encrypted_text += ' '
    index = characters.find(char)
    new_index = (index + shift) % 26
    encrypted_text += characters[new_index]
    print(encrypted_text)