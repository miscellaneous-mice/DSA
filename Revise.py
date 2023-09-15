print("Execise 1")
def missing_number(arr, n):
    total_sum = n*(n+1)/2

    sum_arr = sum(arr)

    missing = total_sum - sum_arr

    return missing

my_list = [1, 2, 3, 4, 6]
print(missing_number(my_list, 6))

print("\nExecise 2")

def sum_num(arr, n):
    size = len(arr)
    for i in range(size):
        for j in range(i+1 ,size):
            if (arr[i]+arr[j]) == n:
                return i,j
                break
            else:
                continue

list_num = [2, 7 ,11, 15]
print(sum_num(list_num, 9))

list_num = [3, 2, 4]
print(sum_num(list_num, 6))

print("\nExecise 3")
def max_pdt(arr):
    arr[::-1].sort()
    return arr[0]*arr[1]

arr = [1, 7, 3, 4 ,9, 5]
print(max_pdt(arr))

print("\nExecise 4")
def middle(arr):
    return arr[1:-1]

myList = [1, 2, 3, 4]
print(middle(myList))

print("\nExecise 5")
def diagonal_sum(matrix):
    total=0
    for i in range(len(matrix)):
        total += matrix[i][i]   
    return total 

print("\nExecise 5")
def first_second(arr):
    arr.sort(reverse=True)
    return arr 

print(first_second([84,85,86,87,85,90,85,83,23,45,84,1,2,0]))

print("\nExercise 6")
def remove_duplicates(arr):
    return list(set(arr))

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))

def remove_duplicates(arr):
    new_arr = [arr[0]]
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            continue
        else:
            new_arr.append(arr[i])
            continue
    return new_arr

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))