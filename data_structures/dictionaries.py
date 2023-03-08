
user = {"name":"Sumit","age":25,"mobile":"7406644532","roll":"roll number"}

print(user["name"])
print(user["age"])
print(user.get("roll","2146255sb8"))


user_keys = user.keys()
print(user_keys)
user_values = user.values()
print(user_values)

#user for loop on dictionary

for u in user.keys():
    print(user[u])

for key in user.keys():
    print(key)

for val in user.values():
    print(val)


for item in user.items():
    print(item)

if "roll" in user.keys():
    print("exist")
else:
    print("not exist")