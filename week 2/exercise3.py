a = input ( "enter the log data ")
def log():
    try :
      with open("log.txt","a") as f:
       p =  f.write(a +"\n")
       print(p)
      with open("log.txt","r") as f:
       p =  f.read()
       print(p)
    except:
     with open("log.txt","w") as m:
        m.write(a)
     with open("logtxt","r") as f:
       p =  f.read()
       print(p)
log()
# with open("log.txt","w") as m:
#         m.write(a)
# with open("log.txt","r") as f:
#        p =  f.read()
#        print(p)


