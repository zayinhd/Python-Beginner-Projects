# Search for a target in a list of numbers 
# and the steps it takes

def binary_search(my_list, elem):
    start = 0
    middle = 0
    end = len(my_list)
    steps = 0

    while(start <= end):
        print("Step", steps, ":", str(my_list[start:end+1]))

        steps = steps + 1

        middle = (start + end) // 2

        if elem == my_list[middle]:
            return middle
        if elem < my_list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1

my_list = [0,1,2,3,4,5,6,7,8,9]

target = int(input("Please enter your target number: "))

# call binary function
binary_search(my_list, target)
