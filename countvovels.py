def countvovels(text):
    count = 0
    vovels = ["A","a","E","e","I","i","O","o","U","u"]
    
    for char in text:
        if (char in vovels):
            count+=1
    return (count)

text = input("text:")
count = countvovels(text)
print ("count:",count)