from time import sleep
print("369 game start~")
for i in range(1, 101): # 1 ~ 100까지 숫자가 반복되도록 함
    if(i % 3 == 0 or i % 10 == 3): # i가 3의 배수이거나 끝자리가 3으로 끝난다면
        print("박수 짝~")
        sleep(0.5) # 0.5초 동안 대기하다가 다음 숫자 출력
    else:
        print(i) # 박수 짝 ~ 을 제외한 나머지 숫자 출력
        sleep(0.5)
