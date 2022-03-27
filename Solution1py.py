"Function get alphabet"
def get_alphabet():
    chn=''
    for i in range(97,122):
        chn=chn+chr(i)
    return chn
chaine=get_alphabet()
print(chaine) 

"Function is_pangramme"
def is_pangramme(str):
    alphabets=get_alphabet()
    for alp in alphabets:
        if alp not in str:
            return false
            break
        return True
"Test"
sentence='the quick brown fox jumps over the lazy dog'
if (is_pangramme(sentence)==True):
    print("Yes, this sentence is a pangram")
else:
    print("No, this sentence is not a pangram")
