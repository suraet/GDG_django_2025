valid_no =[]

with open ("sales.txt" ,"r") as f:
    for a in f:
        try :
            no = int(a)
            valid_no.append(no)
        except:
            continue

total = sum(valid_no)
print(f"the total sales will be {total}")