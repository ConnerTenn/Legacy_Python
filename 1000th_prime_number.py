i = 0
count = 0
while count <= 999:
    i = i + 1
    if i % 3 == 1:
        count = count + 1
        if count == 1000:
            ans = i
print (ans , "=", i)


