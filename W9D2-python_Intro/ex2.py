def donuts(count):
    
    if count < 10:
        return "number of donuts :"+str(count)
    else :
        return "number of donuts is many"

def both_ends(s):
    begining= s[0:1]
    end= s[-2:]
    if len(s) < 2:
        return " "
    else: 
        return begining + end