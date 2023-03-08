

#defining a function

#input in function definion is called parameter
# def sayHello(fname,lname):
#     print("Hello",fname+" ",lname)


# #calling a function

# #argument -> the input given during function calling called argument
# sayHello(lname="Kumar",fname="Sumit")


# #return keyword

# def addition(num1,num2):
#     return num1+num2

# add = addition(10,15)
# print(add)

# name = "Sumit"

# #global scope
# def format_name(fname,lname):
#     global name
#     name = "Amit"
#     print(name)
#     #local scope
#     print("Hi "+fname+ " "+lname)
#     # return "Hi "+fname +" "+lname
# print("n",name)

# formatted_name = format_name("Sumit","Kumar")
# print(formatted_name)



try:
    # print(1+"")
    print(1/0)
except ZeroDivisionError as ze:
    print("Zero devision err ",ze)
except TypeError as e:
    print("Error ",e)







