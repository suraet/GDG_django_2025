try :
  with open("test.txt","r") as f:
       p = f.read()
       print(p)
except:
    with open("test.txt","w") as m:
        m.write("Guest")
    with open("test.txt", "r") as m:
        file = m.read()
        print(file)

    