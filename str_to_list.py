# convert string to a list like this?
# ['My', 'name', 'is', 'mohan,', 'i', 'am', '27', 'years']

data = "My name is mohan, i am 27 years old"
list = []
str = ""

for i in data:
    # print(i, end="")
    if i != " ":
        str = str + i
    else:
        list.append(str)
        str = ""

list.append(str)  # Append the last word after the loop ends

print(list)
