import turtle as t # 터틀 모듈을 불러오고 객체를 t라고 설정
t.shape() # 터틀 객체는 없는 것으로 함
i = 1 # 반복 숫자 초기화 여기서는 1로 초기화를 함
for i in range(11): # 10까지 반복
    t.down();t.circle(10*i);t.up() # 반지름을 10배수로 증가시키면서 원을 그림
