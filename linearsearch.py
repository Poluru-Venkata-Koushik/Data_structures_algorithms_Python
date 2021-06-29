def locate(numbers,query):
    position=0
    while True:
        if numbers[position]==query:
            return position
        position+=1
        if position==len(numbers):
            return -1
test=[3,5,7,59,65,12,64]
inp=int(input("Number Query:"))
print(locate(test,inp))
