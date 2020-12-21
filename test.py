from myaes import MYAES

if __name__ == '__main__':
    aes = MYAES()
    sym_key = aes.newkey()
    #sym_key = int.from_bytes(sym_key, byteorder='big')

    plaintext = input('请输入明文:')
    ciphertext = aes.myaes_encrypt(plaintext, sym_key)
    print('ciphertext = ' + hex(aes._16bytes2num(ciphertext)))

    plaintext = aes.myaes_decrypt(ciphertext, sym_key)
    print('plaintext = ' + plaintext)
