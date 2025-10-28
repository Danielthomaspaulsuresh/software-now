# def decrypt by text, key value
def decrypt(text, key=15):
    decrypted_text = ""
# use the for loop
    for char in text:
# isalpha takes only alphabetic charater
        if char.isalpha():  
            shifted = ord(char) - key
#this helps to check the lower character
            if char.islower():
# no of alphabets
                if shifted < ord('a'):
                    shifted += 26  
            elif char.isupper(): # helps to handle upper case character
                if shifted < ord('A'):
                    shifted += 26  
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char 
    return decrypted_text
