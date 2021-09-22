print('長方形を描画します。')
print('2~20までの整数値を入力してください')
g = int(input('行数:'))
r = int(input('列数'))

for i in range(g):
    for j in range(r):
        print('*',end='')
    print()

if g >= 21 or g < 1 or r >= 21 or r < 1:
    print('値が正しくありません')
