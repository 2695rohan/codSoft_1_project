# /Password Generator

import string
import random

if __name__ == "__main__":

    s1 = string.ascii_lowercase                        #to get  lowercase values of alphabet

    s2 = string.ascii_uppercase                        #for get uppercase values of alphabet
    
    s3 = string.digits                                 #to get  numbers
    
    s4 = string.punctuation                            #to take special char
   
    passLen= int(input("Enter password length\n: "))   #Todo1: Handle Gibberish

    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
   
    random.shuffle(s)                                #to print random values of list s.
    
    print("Your password is: ")
    print("". join(random.sample(s, passLen)))       #to give 4 sample for create a password according to its length

    # print("".join(s[0:passLen]))                   #to add all values of s in a password length.



