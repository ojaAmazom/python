def add(num1, num2):
    result = num1 + num2
    return result

def sub(num1, num2):
    result = num1 - num2
    return result

def mul(num1, num2):
    result = num1 * num2
    return result

def div(num1, num2):
    if num2 == 0:
        result = 0
    else:
        result = num1 / num2

    return result

def rem(num1, num2):
    if num2 == 0:
        result = num1
    else:
        result = num1 % num2

    return result

#メイン処理
input_num1 = int(input('１つ目の整数:'))
input_num2 = int(input('２つ目の整数:'))

#足し算
add_result = add(input_num1, input_num2)
print(input_num1,'+',input_num2,'=',add_result,sep='')

#引き算
sub_result = sub(input_num1, input_num2)
print(input_num1,'-',input_num2,'=',sub_result,sep='')

#掛け算
mul_result = mul(input_num1, input_num2)
print(input_num1,'*',input_num2,'=',mul_result,sep='')

#割り算
div_result = div(input_num1, input_num2)
print(input_num1,'/',input_num2,'=',div_result,sep='')

#剰余算
rem_result = rem(input_num1, input_num2)
print(input_num1,'%',input_num2,'=',rem_result,sep='')