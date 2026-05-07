wr=9.68
running_time= input("what is your running time ?")
running_timme=float(running_time)6
dq_status=input("did you run out of your track(yes/no)?")

disqualified= False
if dq_status=="yes":
 disqualified=True

won=False
if running_time < wr and answer=="no":
 won=True

print(won)