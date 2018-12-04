import random as r

#losujemy tablice
arr = []
for i in range(0,50):
    n = r.randint(0,2000)
    arr.append(n)
arr1=arr
arr2=arr
print("Tablica przed sortowaniem:\n",arr1,"\n")

# definiujemy quicksort
def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot-1)
        quicksort(arr, pivot+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    if arr[high] > arr[i+1]:
        arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1

# definiujemy bubblesort dla porownania, chociaz dla takich malych tablic nie ma to znaczenia
def bubblesort(arr):
    swaps = 1

    while swaps:
        swaps = 0

        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps += 1


#testujemy sortowanie naszym quicksortem
print("Tablcia po naszym quicksorcie:")
length=len(arr1)
quicksort(arr1,0,length-1)
print(arr1,"\n")

#testujemy bubblesort
print("Tablica po naszym bubblesorcie:")
bubblesort(arr2)
print(arr2,"\n")

#sortowanie funkcja wbudowana sort
print("Tablica po wbudowanym sorcie:")
arr.sort(reverse=True)
print(arr,"\n")