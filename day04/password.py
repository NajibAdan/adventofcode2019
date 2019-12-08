def correct(password):
    if len(str(password)) != 6:
        return False
    else:
        password = str(password)
        adj, iso = False, False
        for x in range(len(password)-1):
            if password[x] <= password[x+1]:
                continue
            else:
                return False
        for y in range(10):
            if str(y) * 2 in password:
                adj = True
                if str(y) * 3 not in password:
                    iso = True
        if adj and iso:
            return True

count = 0
for password in range(235741,706949):
    if correct(password) is True: count+= 1

print(count)