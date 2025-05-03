#input array, length and n
def rotation(a, n, a_size):
    for i in range(n):
        rotate(a, a_size)
        
#rotate the array to the left by one space
def rotate(a, a_size):
    temp= a[0]
    for i in range(a_size-1):
        a[i]= a[i+1]
        a[a_size-1]= temp
        
        
def printarray(a, a_size):
    for i in range(a_size):
        print("%d"%a[i], end= " ")
    print("\n")
    
a= [12, 1, 13, 23, 45, 66, 78, 89, 55, 343, 5678]
printarray(a, len(a))
rotation(a, 2, len(a))
printarray(a, len(a))