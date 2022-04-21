from time import sleep # time sleep 모듈 불러옴
i = 1 # 반복 변수 초기화 --> 1
while i<=10: # 10보다 작거나 같을 때까지 반복
    print("숫자 " , str(i), end=' ') # 숫자 1 숫자 2 숫자 3 ... 숫자 10 (end = ' ' --> 한 줄로 출력하도록 함)
    sleep(1) # 1초 동안 대기 
    i+=1 # 값 1씩 증가
