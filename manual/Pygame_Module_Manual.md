# pygame 모듈

## pygame 기본 구조

1. pygame 선언 (`import pygame`)

2. pygame 초기화 (`pygame.init()`)

3. pygame에서 사용할 전역변수 선언
    - size : (창 크기 x와 y, array 배열로 저장) `[int x, int y]`
    - screen : pygame 창 크기 설정 `pygame.display.set_mode(size)`
    - clock : 초당 화면에 보여줄 프레임 설정 `pygame.time.Clock()`

4. pygame 메인 루프 (while 문)
    - pygame Event 설정
    - pygame 화면 설정
    - 사용자 행위



ex)

```python
import pygame # pygame 모듈 불러오기

pygame.init() # pygame 모듈 초기화

# 여기서부터 전역 변수
# 자주 사용하는 색깔 전역 변수
BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
RED   = ( 255,   0,   0)
GREEN = (   0, 255,   0)
BLUE  = (   0,   0, 255)

# 게임 스크린 사이즈 설정
screen_size = [400, 300]	# 스크린 크기, [x, y]
screen = pygame.display.set_mode(size) # 스크린 크기 설정

pygame.display.set_caption("Game Title") # 게임 타이틀 _ 위에 바에 뜨는 이름

#루프 설정 변수
playing_program = True	# 프로그램 실행되고 있는 것 체크용
clock = pygame.time.Clock() # 프레임 설정용

while playing_program:
    clock.tick(30)	# 초당 보여줄 프레임 수, (10, 30, 60 중 하나로 할 것)
    
    for event in pygame.event.get():	# 플레이어가 행동을 할 시,
        if event.type == pygame.QUIT:	# 그 행동이 창을 닫는 행동일 시,
            playing_program = False		# 프로그램 실행 X, while문 탈출
	
    # ~코드~
    
pygame.quit() # 게임 종료
```



## 이미지 불러오기

```python
test_image = pygame.image.load("img/test.png") # 이미지 불러와 test_image에 저장
test_image = pygame.transform.scale(test_image, (50, 100)) # 이미지 사이즈 지정

screen.blit(test_image, (x_pos, y_pos)) # x_pos, y_pos에 test_image를 띄운다
pygame.display.update() # 화면 업데이트해서 보여준다. (while문 맨 마지막에 넣을것)
```

## pygame event 목록

| 이벤트 이름            | 이벤트 속성        | 설명                                                         |
| ---------------------- | ------------------ | ------------------------------------------------------------ |
| pygame.QUIT            | none               | 창 닫기 버튼 클릭 시 발생함                                  |
| pygame.ACTIVEEVENT     | gain, state        | 화면(GUI)에 마우스가 들어가거나 나가면 발생. <br/>혹은 화면이 활성화 상태이면 발생함 |
| pygame.KEYDOWN         | unicode, key, mode | 키보드를 누를때 발생                                         |
| pygame.KEYUP           | key, mode          | 키보드를 누를 때 발생함                                      |
| pygame.MOUSEMOTION     | pos, rel, buttons  | 마우스가 움직일 때 발생함                                    |
| pygame.MOUSEBUTTONUP   | pos, button        | 마우스 버튼을 누른 후 뗄 때 발생함                           |
| pygame.MOUSEBUTTONDOWN | pos, button        | 마우스 버튼을 눌렀을 때 발생함                               |
| pygame.USEREVENT       | code               | 사용자가 임의로 설정하는 이벤트                              |

```python
for event in pygame.event.get(): 	# 플레이어가 행동을 할 시,
    if event.type == pygame.QUIT:		# 플레이어가 창을 닫을 시
        # ~code~
    if event.type == pygame.KEYDOWN:	# 플레이어가 키보드를 누를 시
        if event.key == pygame.K_UP:	# 누른 키보드가 화살표 UP 일 시
            # ~code~
        if event.key == pygame.K_1:		# 누른 키보드가 1일 시
        	# ~code~
    
    if event.type == pygame.MOUSEBUTTONDOWN:	# 마우스 버튼을 누를 시
        if event.button == 1:	# 1:좌클릭, 2:휠클릭, 3:우클릭
            # ~code~
```
