#python 3.7.1
#python 3.7.1
#AES
#Equipo
#Adolfo Armando Villegas Jimenez
#Alan Ignacio Delgado Alarcon

import csv
import random
import string
#El funcionamiento codigo es de la siguiente manera:
#Para el envio de texto y la llave se tiene que tener exactas
#Un texto de 16 bytes y una llave de 16,24 o 32 bytes
#Al ingresar las llaves con esa cantidad de bytes exacta se identifica NK, Nb y Nk
#El cuál se les almacenara su valor.

sbox = [
    ['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
    ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
    ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
    ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
    ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
    ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
    ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
    ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
    ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
    ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
    ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
    ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
    ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
    ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
    ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
    ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']
]

Rcon = [
  ["00","00","00","00"],
  ["01","00","00","00"],
  ["02","00","00","00"],
  ["04","00","00","00"],
  ["08","00","00","00"],
  ["10","00","00","00"],
  ["20","00","00","00"],
  ["40","00","00","00"],
  ["80","00","00","00"],
  ["1b","00","00","00"],
  ["36","00","00","00"]
]



Mul_2 = [
  ["00", "02", "04", "06","08","0a","0c","0e","10","12","14","16","18","1a","1c","1e"],
  ["20", "22", "24", "26","28","2a","2c","2e","30","32","34","36","38","3a","3c","3e"],
  ["40", "42", "44", "46","48","4a","4c","4e","50","52","54","56","58","5a","5c","5e"],
  ["60", "62", "64", "66","68","6a","6c","6e","70","72","74","76","78","7a","7c","7e"],
  ["80", "82", "84", "86","88","8a","8c","8e","90","92","94","96","98","9a","9c","9e"],
  ["a0", "a2", "a4", "a6","a8","aa","ac","ae","b0","b2","b4","b6","b8","ba","bc","be"],
  ["c0", "c2", "c4", "c6","c8","ca","cc","ce","d0","d2","d4","d6","d8","da","dc","de"],
  ["e0", "e2", "e4", "e6","e8","ea","ec","ee","f0","f2","f4","f6","f8","fa","fc","fe"],
  ["1b", "19", "1f", "1d","13","11","17","15","0b","09","0f","0d","03","01","07","05"],
  ["3b", "39", "3f", "3d","33","31","37","35","2b","29","2f","2d","23","21","27","25"],
  ["5b", "59", "5f", "5d","53","51","57","55","4b","49","4f","4d","43","41","47","45"],
  ["7b", "79", "7f", "7d","73","71","77","75","6b","69","6f","6d","63","61","67","65"],
  ["9b", "99", "9f", "9d","93","91","97","95","8b","89","8f","8d","83","81","87","85"],
  ["bb", "b9", "bf", "bd","b3","b1","b7","b5","ab","a9","af","ad","a3","a1","a7","a5"],
  ["db", "d9", "df", "dd","d3","d1","d7","d5","cb","c9","cf","cd","c3","c1","c7","c5"],
  ["fb", "f9", "ff", "fd","f3","f1","f7","f5","eb","e9","ef","ed","e3","e1","e7","e5"] 
]

Mul_3 = [
        ["00","03","06","05","0c","0f","0a","09","18","1b","1e","1d","14","17","12","11"],
        ["30","33","36","35","3c","3f","3a","39","28","2b","2e","2d","24","27","22","21"],
        ["60","63","66","65","6c","6f","6a","69","78","7b","7e","7d","74","77","72","71"],
        ["50","53","56","55","5c","5f","5a","59","48","4b","4e","4d","44","47","42","41"],
        ["c0","c3","c6","c5","cc","cf","ca","c9","d8","db","de","dd","d4","d7","d2","d1"],
        ["f0","f3","f6","f5","fc","ff","fa","f9","e8","eb","ee","ed","e4","e7","e2","e1"],
        ["a0","a3","a6","a5","ac","af","aa","a9","b8","bb","be","bd","b4","b7","b2","b1"],
        ["90","93","96","95","9c","9f","9a","99","88","8b","8e","8d","84","87","82","81"],
        ["9b","98","9d","9e","97","94","91","92","83","80","85","86","8f","8c","89","8a"],
        ["ab","a8","ad","ae","a7","a4","a1","a2","b3","b0","b5","b6","bf","bc","b9","ba"],
        ["fb","f8","fd","fe","f7","f4","f1","f2","e3","e0","e5","e6","ef","ec","e9","ea"],
        ["cb","c8","cd","ce","c7","c4","c1","c2","d3","d0","d5","d6","df","dc","d9","da"],
        ["5b","58","5d","5e","57","54","51","52","43","40","45","46","4f","4c","49","4a"],
        ["6b","68","6d","6e","67","64","61","62","73","70","75","76","7f","7c","79","7a"],
        ["3b","38","3d","3e","37","34","31","32","23","20","25","26","2f","2c","29","2a"],
        ["0b","08","0d","0e","07","04","01","02","13","10","15","16","1f","1c","19","1a"]
]


mtx = [
  [2, 3, 1, 1],
  [1, 2, 3, 1],
  [1, 1, 2, 3],
  [3, 1, 1, 2]
]

def convert_char_to_hex(char):  #Conviertir el caracter a su valor hexadecimal
    return format(ord(char), "x")

def subByte(s):
    for i in range(4):
        for j in range(4):
            s[i][j] = sbox[int(s[i][j][0],16)][int(s[i][j][1],16)]
        
    return s

def shiftRows(s):
    s[1] = s[1][1:] + s[1][:1]
    s[2] = s[2][2:] + s[2][:2]
    s[3] = s[3][3:] + s[3][:3]
    
    return s

def subWord(s):
    for i in range(4):
        s[i] = sbox[int(s[i][0],16)][int(s[i][1],16)]
    return s
  

def rotWord(s):
    s = s[1:] + s[:1]
    return s

def xor_Operation(v1,v2):
  #hex(dec).split('x')[-1
  #hex(int(v1[i],16) ^ int(v2[i],16)).split('x')[-1
  #format(aux, '02x')
    result =[]
    for i in range(4):
        aux = int(v1[i],16) ^ int(v2[i],16)
        result.append(format(aux, '02x'))
    return result


def keyExpansion(ky,Nb,Nr,Nk):
    temp = []
    word =[[] for x in range(Nb *(Nr+1))]
    i=0
  
    while i<Nk:
        word[i].append(format(ord(ky[4*i]), "x"))
        word[i].append(format(ord(ky[(4*i)+1]), "x"))
        word[i].append(format(ord(ky[(4*i)+2]), "x"))
        word[i].append(format(ord(ky[(4*i)+3]), "x"))
        i = i+1
    
    i = Nk
                 
    while i < (Nb * (Nr+1)):
        temp = word[i-1]
        
        if (i%Nk) == 0:
            temp = xor_Operation(subWord(rotWord(temp)),Rcon[i//Nk])
        elif (Nk>6) and (i%Nk == 4):
            temp = subWord(temp)
        word[i] =xor_Operation(word[i-Nk],temp)
        i = i+1
    return word

def addRoundKey(s,word):  
    for i in range(4):
        for j in range(4):
            aux = int(s[j][i],16) ^ int(word[i][j],16)
            s[j][i] = format(aux, '02x')
    return s

def product(num, opt):
    #aux=0
    if opt == 1:
        return int(num,16)
    elif opt == 2:
        return int(Mul_2[int(num[0],16)][int(num[1],16)],16)
    elif opt == 3:
        return int(Mul_3[int(num[0],16)][int(num[1],16)],16)

def mixColumns(s):
    aux = 0
    result = [[],[],[],[]]
    for i in range(4):
        for j in range(4):
            aux = product(s[0][i],mtx[j][0]) ^ product(s[1][i],mtx[j][1]) ^ product(s[2][i],mtx[j][2]) ^ product(s[3][i],mtx[j][3])
            result[j].append(format(aux, '02x'))
    return result

def encrypt(msg,w,Nb,Nr,Nk):
  
    state = [[],[],[],[]]
    k=0
    for i in range(4): #Pasa el caracter del arreglo (o string) a una matriz.
        for j in range(4):
            state[j].append(convert_char_to_hex(msg[k]))  #
            k=k+1
    state = addRoundKey(state,w[0:Nb])
  
    for rnd in range(1,Nr):
        state = subByte(state)
        state = shiftRows(state)
        state = mixColumns(state)
        state = addRoundKey(state,w[rnd*Nb:(rnd+1)*Nb])
    state = subByte(state)
    state = shiftRows(state)
    state = addRoundKey(state,w[Nr*Nb:(Nr+1)*Nb])
    
    return state




def AES(mes,k,Nk,Nb,Nr):
    w = keyExpansion(k,Nb,Nr,Nk)
    
    #if opt == 1:
    return encrypt(mes,w,Nb,Nr,Nk)
    #elif opt == 2:
    #  return encrypt_hex(mes,w,Nb,Nr,Nk)


if __name__ == "__main__":
  
    message = input("Mensaje a encriptar: ")
    key = input("Llave: ")
    if(len(key) == 16):
        nk = 4
        nr = 10
        nb = 4
    elif(len(key)== 24):
        nk = 6
        nr = 12
        nb = 4
    elif(len(key)== 32):
        nk = 8
        nr = 14
        nb = 4
    save = AES(message,key,nk,nb,nr)
  
    print(save)
    sentence = ""
    sen_hex=""
    k=0
    for i in range(4):
        for j in range(4):
            sen_hex = sen_hex + save[j][i]
            sentence = sentence + chr(int(save[j][i],16))
            print(chr(int(save[j][i],16)))
    
    
    print(sen_hex)
    print(type(sen_hex))
    print(sentence)
    print(len(sentence))
    print(type(sentence))




    f = open("archivo_aes.csv","a",newline="")
    


    tupl = [message,sen_hex,key]
    print(tupl)
    writer = csv.writer(f)
    writer.writerow(tupl)
    f.close()

