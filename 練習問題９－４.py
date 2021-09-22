def triple(num):
    return num*3

input_num = int(input('整数を入力してください'))

triple_num = triple(input_num)
ninetimes_num = triple(triple_num)

print(input_num, 'の9倍は', ninetimes_num, 'です。', sep='')