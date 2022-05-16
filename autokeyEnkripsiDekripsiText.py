def autoKeyEnkripsi(plain,key):
    plain = plain.upper().split()
    plain = ''.join(plain)
    key = key.upper()

    length = len(plain)-len(key)#panjang plain text yang dipotong
    streamkey = key + plain[:length]
    result =''
    for i in range(len(streamkey)):
        p = ord(plain[i])
        k = ord(streamkey[i])
        c =(p+k)%26
        result = result+chr(c+65)
    return result

def autoKeyDekripsi(cipher,key):
    cipher = cipher.upper()
    key = key.upper()
    streamkey = key 
    result =''
    
    for i in range(len(cipher)):
        c = ord(cipher[i])
        k = ord(streamkey[i])
        p =(c-k)%26
        result = result + chr(p+65)
        streamkey = streamkey + chr(p+65)
    return result

#######################################################

print('Program Enkripsi/Dekripsi Autokey Cipher')
pilihan = int(input('1. Enkripsi\n2. Dekripsi\n Pilihan:'))

text=input('Masukkan text  : ')
key=input('Masukkan kunci :')

if pilihan==1:
    cipher = autoKeyEnkripsi(text,key)
    print('Plaintext    :',text)
    print('Kunci        :',key)
    print('Hasil Enkripsi: ',cipher)
elif pilihan==2:
    plain = autoKeyDekripsi(text,key)
    print('Ciphertext   :',text)
    print('Kunci        :',key)
    print('Hasil Dekripsi: ',plain)
