def chk_fact(number):
    divisor = number
    dividend = 26
    remainder = dividend % divisor
    while remainder > 0:
        dividend =  divisor
        divisor = remainder
        remainder = dividend % divisor
    if divisor != 1:
        print ('value of alpha cant be taken')
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
                    cont = input('encryption cancelled')
                    quit()
                else:
                    print('Invalid input')
                    continue
        else:
            cont == "I"
            return(str)

def encrypt(input_str):
    for var in input_str:
                if var in alphabet_list:
                    x = alphabet_list.index(var)
                    newvalue = a_var*x + b_var
                    newvalue = newvalue%26
                    encrypt_temp = alphabet_list[newvalue]
                    encrypt_temp = encrypt_temp.upper()
                    encrypt_list.append(encrypt_temp)
    encryptmsg=''.join(encrypt_list)
    print('The encrypted message is ', encryptmsg)

alphabet_list= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
encrypt_list = list()
input_str_list = list()
cont = ''
a_var = int(input ('Enter the alpha variable: '))
b_var = int(input ('Enter the beta variable:  '))
if a_var in range(1,26):
    if a_var != 26:
        chk_fact(a_var)
    input_str = strcheck()
    input_str = input_str.lower()
    encrypt(input_str)
else:
    print (' alpha variable should be in the range 1-26')
