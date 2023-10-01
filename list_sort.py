def index_of_min(mylist):
    min_index=0
    for i in range(1,len(mylist)):
        if mylist[i]<= mylist[min_index]:
            min_index=i
    return min_index        

def sort_asc_list(mylist):

    sorted_list = []
    for i in range(0,len(mylist)):
        # print (mylist)
        # print(i)
        index_to_move = index_of_min(mylist)
        sorted_list.append(mylist[index_to_move])
        del mylist[index_to_move]
    return sorted_list

def index_of_max(mylist):
    max_index=0
    for i in range(1,len(mylist)):
        if mylist[i]>= mylist[max_index]:
            max_index=i
    return max_index     

def sort_desc_list(mylist):

    sorted_list = []
    for i in range(0,len(mylist)):
        index_to_move = index_of_max(mylist)
        sorted_list.append(mylist[index_to_move])
        del mylist[index_to_move]
    return sorted_list
    
        
    
        
    


def list_sort(mylist, order=None):
    if order=="asc":
        return sort_asc_list(mylist)
    if order=="desc":
        return sort_desc_list(mylist)
    if order==None:
        return mylist
       

list1 = [4,9,9,5,3,2,55,6]
#print(sort_a_list(list1))   
# print(list_sort(list1,"asc"))
print(list_sort(list1,"desc"))
