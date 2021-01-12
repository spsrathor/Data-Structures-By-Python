# Your task is to complete all
# three functions

# if the element is found in the list
# function  must return true or else
# return false
def searchEle(a, x):
    # Code here
    if x in a:
        return 1
    else:
        return 0

# fucntion must return true if 
# insertion is successful or else
# return false
def insertEle(a, y, yi):
    # Code here
    a.insert(yi,y)
    return 1

# fucntion must return true if 
# deletion is successful or else
# return false
def deleteEle(a, z):
    # Code here
    try:
        a.remove(z)
        return 1
    except:
        return 1
