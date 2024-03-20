from random import random
import os
from data import event, time, n_time

def alert(word):
    if word == '상':
        print("""난이도 '어려움'을 선택하셨습니다
'어려움'난이도는 년, 월, 일까지 입력해야 정답으로 처리됩니다

주의사항
- 입력 형식은 년 월 일 입니다. ex) 1863 12 8
- 공백에 주의하세요 !!""")
    elif word == '하':
        print("난이도 '쉬움'을 선택하셨습니다\n'쉬움'난이도는 년 월을 정확하게 입력하면 정답으로 처리됩니다\n")
    else:
        input("제대로 입력해 주세요. 아무 키나 눌러 종료하세요")

def inf():
    os.system('cls')
    print("\n무한 모드입니다\n그만하고 싶으시다면 X를 입력해 주세요\n")
    while True:
        x = int(random()*len(event))
        print(event[x])
        y = input("언제 일어났나요? : ")
        if y == time[x]:
            print("\n정답!\n")
        elif y == 'X':
            break
        else:
            print("\n다시 외우세요!")
            print("정답은", time[x]+'입니다\n\n\n\n')
    play = input("\n\n테스트 모드를 진행할까요? (O/X) : ")
    if play == "O":
        test()
    else:
        input("프로그램을 종료합니다. 아무 키나 눌러 종료하세요")

def test():
    os.system('cls')
    print("\n시험 모드입니다")
    diff = input("난이도를 설정해 주세요 (상/하) : ")
    
    n = int(input("시험 볼 문제 개수를 입력해 주세요 : "))
    total = 0
    print('\n')
    alert(diff)
    print('\n')
    for i in range(1, n+1):
        q = int(random()*len(event))
        print('[',i, "번째 문제]\n", event[q], sep='')
        a = input("언제 일어났나요? : ")
        if diff == "상":
            answer = time[q]
        else:
            answer = n_time[q]
        if a == answer:
            print("\n정답입니다!\n\n\n")
            total += 1
        else:
            print("\n틀렸습니다..")
            print("정답 :", answer+'\n\n\n')
    percentage = total/n*100
    print("총 문제 수 :", n, "\n맞은 문제 수 :", total, "\n정답률 :", str(percentage)+"%")

    if total/int(a)*100 >= 80:
        print("중간 화이팅 !!")
        input("아무 키나 눌러 종료하세요")
    else:
        print("노력이 필요합니다 ..\n")
        cont = input("무한모드를 진행할까요? (O/X) : ")
        if cont == 'O':
            inf()
        else:
            input("프로그램을 종료합니다. 아무 키나 눌러 종료하세요")

print('''[역사 연표 외우기]
김중근T 1학년 2학기 중간고사 범위 연표
''')

mode = input("<모드선택>\n1. 무한모드\n2. 테스트\n\n어떤 모드로 하시겠습니까? (1 / 2) : ")

if mode == '1':
    inf()

elif mode == '2':
    test()

# Easter Egg ...

else:
    print('제대로 입력해 주세요. 프로그램을 종료합니다')