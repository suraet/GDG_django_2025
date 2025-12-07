old_dict = {"john":"A",
            'sara':'B',
            "musa":"A"}
new = {}
for key , value in old_dict.items():
    new[value] = key 
print(new)

#the dictionary value have to be unique so we only get musa A !!!