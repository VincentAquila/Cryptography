#this is a Caesar Cypher cryptographic message encoder. 
#enter a word to encode, e.g. Vince produces ivapr
#enter the encoded word, e.g. ivapr, and the result is Vince

#positions 0-25
alpha = "abcdefghijklmnopqrstuvwxyz"   


def encrypt(cleartext):
    cyphertext = " "
    for char in cleartext:
        if char in alpha:
            #find will look in alpha and return the index number of a character
            newpos = (alpha.find(char) + 13) % 26     
            # the modulus 26 will assist by resetting to zero.
            cyphertext += alpha[newpos]

        else:
            cyphertext += char
    return cyphertext


msg = input("Clear text: ")
cleartext = msg.lower()

print(encrypt(cleartext))



