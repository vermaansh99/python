
friends = ["Sameer","Surya","Sumit","Saif","Hemanth"] #string type list
scores = [22,23,35] # num list
salaries = [33000.15,23000.0] #float list
my_list = ["Apple",12,True,3.5] #mixed type list

# change value by index
friends[0] = "Surya"
friends[1] = "Sameer"

try:
    print(friends[5]) # access element by index
except IndexError as ie:
    print(ie)


# slicing

first_two_friends = friends[0:4:2]
print(first_two_friends)

# negative indexing

print(friends[-1])

# getting length of list

print(len(friends))

# methods on the list

# append

friends.append("Rohit")
print(friends)

#pop
last_popped_out = friends.pop()

print(last_popped_out)

print(friends)

# copy

a = friends.copy()
print(a)

#extend

a = [1,2,3]
b = [1,5,6]

a.extend(b)
print(a)


# list concatenation
c = a+b
print(c)

print(a)

# list replication
print(["a","b"]*10)

del friends[0]

print(friends)


# using for loops on list


for friend in friends:
    print(friend)

# using range 

for i in range(0,len(friends)):
    print(friends[i])

# enum

for i,friend in enumerate(friends):
    print(i,friend)


for friend in friends:
    if "Sumit" not in friends:
        print("yes")


a,b,c = [10,20,30]
print(a,b,c)

num = 20
num *= 2
print(num)

num = [1,2,3]

num.insert(0,5)

print(num)

num.sort(reverse=True)
print(num)


str=("ansh  verma")
print(str.strip().replace("  "," ").count(" ")+1)



