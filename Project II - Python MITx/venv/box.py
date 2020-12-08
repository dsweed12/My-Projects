def bob(s):
    n = 0
    k=0
    f=s.find('bob')
    while f != -1:
        n += 1
        if f-k+2>len(s)-1:
            x=len(s)-1
        else:
            x=f-k+2
        while s[f:f+5] == "bobob":
            k += 1
            s = s.replace(s[f-k:x], "", 1)
            if f - k + 2 > len(s) - 1:
                x = len(s) - 1
            else:
                x = f -k +2
            f = s.find("bob")
        s = s.replace('bob', "", 1)
        f = s.find("bob")
    print("Number of times bob occurs is: " + str(n+k))
bob('spongebobandbobbywenttobobtobobbybobob')