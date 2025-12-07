def cal_sum (file_path):
    sum = 0
    try:
        with open (file_path , "r") as f :
            for line in f :
                line = line.strip()
                if not line:
                    continue 
                try :
                    sum += int(line)
                except:
                    continue
    except:
        print("dont find the file") 
        return
    print(f"total sum = {sum}")

with open("number.txt" ,"w")as f:
    f.write("10\nabc\n12\n")
cal_sum("number.txt")