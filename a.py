#Jeffery Zhao 349162321

def encryptor(word,key):
    
    alphabet="abcdefghijklmnopqrstuvwxyz"
    result=word
    
    result=list(result)
    value=list(word)
    
    for i in range(0,len(word)):
        value[i]=int(alphabet.rindex(word[i]))
        value[i]=value[i]+key
        
        if value[i]>25:
            value[i]=value[i]-26
            
        result[i]=alphabet[value[i]]
        
        endResult=''.join(result)
    
    return endResult


word = input("What is the word you would like to encypt?\n")
key = int(input("What is the key?\n"))
print(encryptor(word,key))
print("Another victory for JeffJeffGames")
