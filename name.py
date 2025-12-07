while True:
 try :
   a=input("enter the name ")
   with open("userdata.txt", "a") as m:
        m.write(f"\n{a}")
   with open("userdata.txt","r") as f:
       p = f.read()
       print(p)

 except Exception:
     with open("userdata.txt","w") as m:
        m.write("Guest")
