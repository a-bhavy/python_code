def x_equal_o(string):
    countX=0
    countO=0
    for i in string.lower():
        if i =="x" :
            countX+=1
        elif i == "o":
            countO+=1

    if countX==countO:
        return True
    else :
        return False    
 

string = input("enter string:")

ans = x_equal_o(string)
print (ans)

