#the provided code from the programming assignment unit 7
alphabet = "abcdefghijklmnopqrstuvwxyz"   
test_part1=[alphabet, "aaa", "abc"]
test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 
test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]

def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d

def has_duplicates(s):
    h = histogram(s)
    for i in h :
        if h.get(i,0) > 1:
            return True #return true if there are any repeated characters
    return False #return false if there aren't any repeated characters
        
def listOfString(s):
    for i in s:
        if has_duplicates(i) == True:
            print('{} has duplicates'. format(i))
        else:
            print('{} has no duplicates'. format(i))

def missing_letters(s):
    global alphabet
    missingLetters = ''
    for i in alphabet :
        if histogram(s).get(i,0)==0:
            missingLetters += i
    return missingLetters

def missLetters(s):
    for j in s:
        if missing_letters(j) == "":
            print("{} uses all the letters". format(j))
        else:
            print("{} is missing letters : {}". format(j, missing_letters(j)))

print(has_duplicates("abcd")) #to test whether the has_duplicate function is working correctly or not
print(has_duplicates("abbccd")) #to test whether the has_duplicate function is working correctly or not
print("")
listOfString(test_dups) #the loop that outputs duplicate info for each string in test_dups
print("")
missLetters(test_miss) #the loop that outputs missing letters for each string in test_miss. 
