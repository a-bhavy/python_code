def hide_card_no(card_no):
    
    hidden_no = "#"*(len(card_no)-4) + str(card_no)[-4:]
    return hidden_no


card_no = input("enter your card no :")
hidden_no = hide_card_no(card_no)
print("last four digits of your card no.is :",hidden_no) 


