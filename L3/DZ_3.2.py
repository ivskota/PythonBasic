#list = [12, 3, 4, 10] # [10, 12, 3, 4]
#list = [1] # [1]
#list =[] #[]
list =[12, 3, 4, 10, 8] # [8, 12, 3, 4, 10]

if len(list) > 1:
    last = list.pop()
    list.insert(0, last)

print(list)