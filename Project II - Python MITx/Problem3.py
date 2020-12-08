s='zyxwvutsrqponmlkjihgfedcba'
high = s[0]
for i in range(len(s)-1):
    count = 1
    seq = ''
    j = i
    if s[j+1] >= s[j]:
        while j < len(s) - 1:
            if s[j + 1] >= s[j]:
                count += 1
                j += 1
            else:
                break
        seq += s[i:i+count]
    if count > len(high):
            high = seq
print(high)
