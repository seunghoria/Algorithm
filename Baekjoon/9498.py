X = int(input())

if 90 <= X <= 100:
    print('A')
elif 80 <= X < 90:
    print('B')
elif 70 <= X < 80:
    print('C')
elif 60 <= X < 70:
    print('D')
else:
    print('F')


# 정확한 답
score = int(input())
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

