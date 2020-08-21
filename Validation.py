import re

def validateemail(email):
    if re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email):
        return False
    else:
        return True

def validatetemobile(mobile):
    if re.match(re.compile(r'\d{10,12}'), str(mobile)):
        return True
    else:
        return False

