def chk_fact(number):
    divisor = number
    dividend = 26
    remainder = dividend % divisor
    while remainder > 0:
        dividend =  divisor
        divisor = remainder
        remainder = dividend % divisor
    if divisor != 1:
        print ('Value of alpha cant be taken')
        quit()
    else:
        pass

def strcheck():
    cont = ''
    while cont != "I":
        str = input('Enter the string to be encrypted: ')
        if str == "":
            print ('String is blank, cannot encrypt')
            cont = ''
            while cont != 'X':
                cont = input('Press Y or N to continue: ')
                if cont.upper() == 'Y':
                    cont = 'X'
                elif cont.upper() == 'N':
                    cont = input('decryption cancelled')
                    quit()
                else:
                    print('Invalid input')
                    continue
        else:
            cont == "I"
            return(str)

def moduloinverse(a_var):
    remainder = 0
    multiple = 0
    while remainder != 1:
        divisor = 26
        dividend = a_var*multiple
        remainder = dividend % divisor
        multiple += 1
    return(multiple-1)

def decrypt(input_str):
    a_var_inverse = moduloinverse(a_var)
    for var in input_str:
                if var in alphabet_list:
                    x = alphabet_list.index(var)
                    newvalue = a_var_inverse*(x - b_var)
                    if newvalue >= 0:
                        newvalue = newvalue%26
                    else:
                        multiple = 1
                        difference = -1
                        while difference <= 0:
                            factor = multiple*26
                            difference = factor + newvalue
                            multiple += 1
                        newvalue = difference % 26
                    decrypt_temp = alphabet_list[newvalue]
                    decrypt_list.append(decrypt_temp)
    decryptmsg=''.join(decrypt_list)
    print('The decrypted message is ', decryptmsg)

alphabet_list= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
decrypt_list = list()
input_str_list = list()
cont = ''
a_var = int(input ('Enter the alpha variable: '))
b_var = int(input ('Enter the beta variable:  '))
if a_var in range(1,26):
    if a_var != 26:
        chk_fact(a_var)
    input_str = strcheck()
    input_str = input_str.lower()
    decrypt(input_str)
else:
    print (' alpha variable should be in the range 1-26')
