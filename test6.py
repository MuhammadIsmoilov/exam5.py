file_name = 'counter.txt'
cnt = 0
cnt2 = 0
cnt3 = 0

with open(file_name, 'r') as file:
        for i in file:
            if (i.isalpha()):
                cnt += 1
            elif (i.isdigit()):
                cnt2 += 1
            else:
                cnt3 += 1

print(f"Words: {cnt}\n Numbers: {cnt2}\n Symbols: {cnt3}")
