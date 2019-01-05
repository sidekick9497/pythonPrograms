def generate(n):
    output_list = []
    for i in range(0,2*n+1):
        output_list.append(i)
    counter_negative = n-1
    counter_positive = n+1
    print("  ",n)
    while(counter_negative > 0):
        print(output_list[counter_negative],end="    ")
        print(output_list[counter_positive],end="    ")
        print("")
        counter_negative -= 1
        counter_positive += 1

number = int(input("enter the number  :"))
generate(number)