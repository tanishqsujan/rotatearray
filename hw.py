def rotate(a, a_size):
    temp = a[0]
    for i in range(a_size - 1):
        a[i] = a[i + 1]
    a[a_size - 1] = temp

def rotation(a, n, a_size):
    for i in range(n):
        rotate(a, a_size)

def printarray(a, a_size):
    for i in range(a_size):
        print("%d" % a[i], end=" ")
    print("\n")

a_size = int(input("Enter the size of the array: "))
a = []

print("Enter the elements of the array:")
for i in range(a_size):
    element = int(input(f"Element {i + 1}: "))
    a.append(element)

n = int(input("Enter number of positions to rotate the array to the left: "))

print("\nOriginal array:")
printarray(a, a_size)

rotation(a, n, a_size)

print("Rotated array:")
printarray(a, a_size)
