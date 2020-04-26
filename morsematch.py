morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

words = ["gin", "zen", "gig", "msg"]


word_trans = []

for item in words:
    item_trans = ""
    for c in list(item):
        c_index = alpha.index(c)
        item_trans += morse[c_index]
    word_trans.append(item_trans)

print(len(set(word_trans)))



