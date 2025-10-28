
def decrypt(text, key=13):
    decrypted_text = ""  # declare an empty string to the Decrypted text
    for char in text:
        if char.isalpha(): # shows the alphabetic charcters
            shifted = ord(char) - key
            if char.islower():  #helps to handle the lower case
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper(): # handles the upper case
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text   # return the decrypted text

plain_text = "global"
decrypted_text = decrypt(plain_text, key=13) # decrpt the plain_text into key value of 13
print(f"Decrypted text: {decrypted_text}") # print the decrypted which helps to find the encrypted text

# key value is 13