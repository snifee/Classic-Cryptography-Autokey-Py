try:
    print("Autokey-Enkripsi")
    path = input('Masukan nama gambar:')
    key = input('Masukan Kunci:')

    print('Enkripsi untuk:')
    print('Nama gambar : ', path) #path dari gambar atau nama file gambar
    print('Kunci       : ', key) 
    
    fin = open(path,'rb')
    img = fin.read()
    fin.close()
    img = bytearray(img)

    streamkey = bytearray(key,'utf-16')
    pan = len(img)-len(streamkey)
    streamkey = streamkey+img[:pan]

    result = bytearray(img)
    for i,value in enumerate(streamkey):
        result[i] = (img[i]^value)

    fin = open('cipher.bin','wb')
    fin.write(result)
    fin.close()
    print('done')

except Exception:
    print('Error :', Exception.__name__)
