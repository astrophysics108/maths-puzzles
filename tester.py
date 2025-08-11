x = "3816547290"

for i in range(1,10):
    if not int(x[:i]) % len(x[:i]) == 0:
        print("oh no")




