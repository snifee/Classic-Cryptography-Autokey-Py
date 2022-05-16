try:   
    print("Autokey-Dekripsi")
    # path = input('Masukan nama cipher:')
    key = input('Masukan Kunci:')

    print('Dekripsi untuk:')
    # print('Nama gambar : ', path)
    print('Kunci       : ', key) 

    # fin = open(path,'rb')
    # cipher = fin.read()
    # fin.close()

    streamkey = bytearray(key,'utf-32')
    print(streamkey,' ',ord('h'))

    result = bytearray(cipher)
    for i in range(len(cipher)):
        result[i]=(cipher[i]^streamkey[i])
        streamkey.append(result[i])

    fin = open('result1.png','wb')
    fin.write(result)
    fin.close()

except Exception:
    print('Error: ',Exception.__name__)