import turtle as t
from random import randint

t.shape("turtle") # 그래픽 객체는 turtle

s = t.textinput("", "이름을 입력하시오:") # 본인의 이름을 입력할 수 있는 창 생성
 
t.write("안녕하세요?" + s + "씨, 터틀 인사 드립니다.") # 본인의 이름 및 레이블이 생성

t.color("orange");t.speed(8);t.up();t.goto(-200, 200) # 오렌지 객체 이동
for step in range(20): # 터틀 경주를 할 경주선 그리기
    t.rt(90);t.down();t.fd(130);t.up();t.bk(130);t.lt(90);t.fd(25)

t.goto(0, -55) # 오렌지 객체 이동
t.down()
t.fd(50);t.lt(90);t.fd(20);t.lt(90);t.fd(100);t.lt(90);t.fd(20);t.lt(90);t.fd(50)
# 주황색 거북이가 사각형을 그리고 가운데 위치에 올 수 있도록 설정

t1 = t.Turtle() # 레드 객체 생성 및 위치 이동
t1.color('red');t1.shape('turtle');t1.penup();t1.goto(-220,170);t1.pendown()

t2 = t.Turtle() # 노랑 객체 생성 및 위치 이동
t2.color('yellow');t2.shape('turtle');t2.penup();t2.goto(-220, 140);t2.pendown()

t3 = t.Turtle() # 블루 객체 생성 및 위치 이동
t3.color('blue');t3.shape('turtle');t3.penup();t3.goto(-220,110);t3.pendown()

t4 = t.Turtle() # 그린 객체 생성 및 위치 이동
t4.color('green');t4.shape('turtle');t4.penup();t4.goto(-220, 80);t4.pendown()

ad1 = 0 # 1번 거북이가 이동한 거리
ad2 = 0 # 2번 거북이가 이동한 거리
ad3 = 0 # 3번 거북이가 이동한 거리
ad4 = 0 # 4번 거북이가 이동한 거리

for turn in range(180): # 179까지 1~5정도의 이동 수를 바탕으로 거북이들이 이동
    r1 = randint(1, 5) # 랜덤 모듈의 randint 메서드 사용 1 ~ 5까지의 난수 범위 설정
    r2 = randint(1, 5)
    r3 = randint(1, 5)
    r4 = randint(1, 5)
    t1.fd(r1) # 랜덤값 만큼 
    t2.fd(r2)
    t3.fd(r3)
    t4.fd(r4)
    ad1 += r1
    ad2 += r2
    ad3 += r3
    ad4 += r4
    
    if ad1 >= 500: # 1번 거북이 500 이상 이동
        t1.write("1번 거북이 우승!")
        break
    elif ad2 >= 500: # 2번 거북이 500 이상 이동
        t2.write("2번 거북이 우승!")
        break
    elif ad3 >= 500: # 3번 거북이 500 이상 이동
        t3.write("3번 거북이 우승!")
        break
    elif ad4 >= 500: # 4번 거북이 500 이상 이동
        t4.write("4번 거북이 우승!")
        break
    


