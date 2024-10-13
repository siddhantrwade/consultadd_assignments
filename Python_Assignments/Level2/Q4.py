
def reverser(iterable, start, end):

    while start < end: 

        iterable[start], iterable[end] = iterable[end], iterable[start]
        start +=1 
        end -= 1

def rotator(lst, d):

    n = len(lst)

    d = d % n # adjusts d in case its d > n

    reverser(lst, 0, n-1)

    reverser(lst, 0, d-1)

    reverser(lst, d, n-1)

list_sample = [1,2,3,4,5,6,8]
d = 2 

rotator(list_sample, d)

print("Rotated list", list_sample)

