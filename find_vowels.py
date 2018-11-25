def find_vowels(str1):
    str1=str1.lower()
    vowels=[ 'a', 'e', 'i','o', 'u']
    counter=0
    for symbol in str1:
        if symbol in vowels:
            counter+=1
    return counter