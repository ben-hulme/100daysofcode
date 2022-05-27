should_end = False

def encrypt_and_decrypt(text, shift):

    global letter_count

    for letter in word_as_list:
        if alphabet.count(letter) > 0:
            if direction == "encode":
                encrypt(letter)
            else:
                decrypt(letter)
        else:
            shifted_loc_list.append(letter)
    for letter in word_as_list:
        if alphabet.count(letter) > 0:
            shifted_word_list.append(alphabet[shifted_loc_list[letter_count]])
            letter_count += 1
        else:
            shifted_word_list.append(shifted_loc_list[letter_count])
            letter_count += 1

    print(f"Your {direction}d text is {''.join(shifted_word_list)}")

def decrypt(letter):
    shifted_loc_list.append(alphabet.index(letter) - shift)
    if shifted_loc_list[-1] < 0:
        shifted_loc_list[-1] = shifted_loc_list[-1] % len(alphabet)

def encrypt(letter):
    shifted_loc_list.append(alphabet.index(letter) + shift)
    if shifted_loc_list[-1] > len(alphabet) - 1:
        shifted_loc_list[-1] = shifted_loc_list[-1] % len(alphabet)

while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    word_as_list = list(text)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    shifted_word_list = []
    shifted_loc_list = []
    letter_count = 0

    encrypt_and_decrypt(text=text, shift=shift)

    restart = input('Type "yes" if you want to go again. Otherwise type "no".\n')
    if restart == "no":
        should_end = True
        print("Goodbye")
