task = [199,200,208,210,200,207,240,269,260,263]
tmp = 00

if __name__ == '__main__':
    for number in task:
        if tmp == 00:
            value = "N/A - no previous measurement"
        else:
            if number > tmp:
                value = "increased"
            elif number < tmp:
                value = "decreased"
            else:
                value = "stays the same"

        print(f'{number} ({value})')
        tmp = number


