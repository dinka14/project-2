inp_list = [int(s) for s in input().split()]

for i in range(1, len(inp_list)):
    if (inp_list[i-1] < 0 and inp_list[i] < 0) or (inp_list[i-1] > 0 and inp_list[i] > 0):
        print(inp_list[i-1], inp_list[i])
        break
