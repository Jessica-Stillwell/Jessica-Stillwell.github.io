import string
import re
def encrypt(filename):
    text = ""
    alphabet = list(string.ascii_lowercase)+list('a') + list(string.ascii_uppercase)+list('A')
    file = open(filename, 'r') 
    lines = file.readlines()
    for line in lines: 
        for element in list(line.strip()):
            text = text + chr(ord(element)-2)
    wr = open(filename, 'w') 
    wr.write(text)
    

def decrypt(filename):
    dtext = ""
    alphabet = list(string.ascii_lowercase)+list('a') + list(string.ascii_uppercase)+list('A')
    file = open(filename, 'r') 
    lines = file.readlines()
    for line in lines:
        for element in list(line.strip()):
            dtext = dtext + chr(ord(element)+2)
    wr = open(filename, 'w') 
    wr.write(dtext)
    
encrypt('MobyDick.txt')
decrypt('MobyDick.txt')