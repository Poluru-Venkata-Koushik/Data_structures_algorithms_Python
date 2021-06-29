def binary_search(input_list, query):
    low=0
    high=len(input_list)-1
    while True:
        if input_list[low]==query:
            return low
        elif input_list[high]==query:
            return high
        mid=(low+high)//2
        if(low==mid or high==mid):
            return -1
        if(mid)==0:
            return -1
        if(input_list[mid]==query):
            return mid
        if input_list[mid]>query:
            high=mid
        elif input_list[mid]<query:
            low=mid


input_list = [1, 25, 8, 65, 54, 4, 6, 4, 1, 4, 6, 4, 5, 6, 4, 9, 2, 8, 5, 98, 9, 48, 84, 5, 48, 48, 4, 64, 984, 85, 4,
              84, 8, 48, 489, 4, 96, 9, 6, 4, 48, 548, 5, 7854, 85, 45, 24, 6]
input_list.sort(reverse=False)  # to sort in ascending order reverse=False. to sort in ascending order reverse=True
query = int(input("Enter query:"))
print(binary_search(input_list, query))