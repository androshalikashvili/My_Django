total_sum = 0

while True:
    x = input('enter number or "sum" for end : ')

    if x.isdigit():
        num = int(x)
        if num > 0:
            total_sum += num
        else:
            continue
    elif x == "sum":
        break
    else:
        continue

print(total_sum)
