"""
    BS implementation 
    Created by 
    Modified by 
    Date 

"""


def binary_serach(l,key):
    """
    
    BS fun input takes list and key 
    return true if elemnt present else False
    """
    if len(l) == 0:
        return False
    else:
        mid = len(l) // 2 

        if key == l[mid]:
            return True
        elif key < l[mid]:
            return binary_serach(l[0:mid],key)
        else:
            return binary_serach(l[mid+1:],key)


if __name__ == "__main__":
    l = [10,20,30,40,50,60,70,80]
    key = 100
    print(binary_serach(l,key))


