score = {"john":85,
         "sara":92,
         "fraol":78}
try :
    print(f"u sore {score[str(input("write name to see ur grade "))]}")
except:
    print("u dont have registered")