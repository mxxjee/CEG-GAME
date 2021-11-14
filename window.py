import pygame as pg
import time
import sys
import random

#초기화
pg.init()

BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)
YELLOW = (0,255,255)
BABYPINK = (225, 226, 243)
GRAY = (102, 102, 102)

set_color = (255, 255, 255)
size = [1040,800]

#화면 사이즈
screen = pg.display.set_mode(size)

#창의 캡션
pg.display.set_caption("CEG GAME!!!!")

diceNum = 0
diceCnt = 0
chanceTile = [7, 22, 36]
communityTile = [2, 17, 33]
thanksFee = [4, 38]
freeParking = 20
freeTravel = [12, 28]
spaceCraft = [5, 15, 25, 35]
fuel = 20
resource = 20

# Flags
resourceButtonBlock = False
printMode = 0
spaceBlock = False


#배경음악
background_sound = pg.mixer.Sound("./bgm/bgm.wav")
background_sound.play(-1)

in_game_music = pg.mixer.Sound("./bgm/in_game_music.wav")

#버튼 클릭음
buttonClick = pg.mixer.Sound("./bgm/button_click.wav")


clock = pg.time.Clock()
titleImg = pg.image.load("./img/startimg.png")
board = pg.image.load("./img/board.png")
board = pg.transform.scale(board, (800, 800))

startImg = pg.image.load("./img/starticon.png")
clickStartImg = pg.image.load("./img/clickedStartIcon.png")

quitImg = pg.image.load("./img/quiticon.png")
clickQuitImg = pg.image.load("./img/clickedQuitIcon.png")

diceImg = pg.image.load("./img/dice.png")
diceImg = pg.transform.scale(diceImg, (150, 150))
sideImg = pg.image.load("./img/side.png")

yesImg = pg.image.load("./img/Yes.png")
yesImg = pg.transform.scale(yesImg, (470, 200))

clickYesImg = pg.image.load("./img/clickYes.png")
clickYesImg = pg.transform.scale(clickYesImg, (470, 200))

noImg = pg.image.load("./img/No.png")
noImg = pg.transform.scale(noImg, (470, 200))

clickNoImg = pg.image.load("./img/clickNo.png")
clickNoImg = pg.transform.scale(clickNoImg, (470, 200))

winImg = pg.image.load("./img/win.png")

gameoverImg = pg.image.load("./img/gameover.png")

restartImg = pg.image.load("./img/restart.png")
restartImg = pg.transform.scale(restartImg, (180, 180))


clickRestartImg = pg.image.load("./img/clickedrestart.png")
clickRestartImg = pg.transform.scale(clickRestartImg, (180, 180))

# screen.blit(restartImg, (500, 500))

# playerImg = pg.image.load("./img/player_001.png")
# playerImg = pg.transform.scale(playerImg, (70, 70))
player_x_pos = 710
player_y_pos = 710


selectText = pg.image.load("./img/select.png")

cr1 = pg.image.load("./img/c1.png")
cr1 = pg.transform.scale(cr1, (170, 170))

clickedcr1Img = pg.image.load("./img/click1.png")
clickedcr1Img = pg.transform.scale(clickedcr1Img, (170, 170))

cr2 = pg.image.load("./img/c2.png")
cr2 = pg.transform.scale(cr2, (170, 170))

clickedcr2Img = pg.image.load("./img/click2.png")
clickedcr2Img = pg.transform.scale(clickedcr2Img, (170, 170))

#땅 , 좌표
playerTile = {
    0: (720, 720),
    1: (620, 720),
    2: (560, 720),
    3: (495, 720),
    4: (430, 720),
    5: (370, 720),
    6: (300, 720),
    7: (235, 720),
    8: (170, 720),
    9: (105, 720),
    10: (20, 710),
    11: (10, 620),
    12: (10, 560),
    13: (10, 490),
    14: (10, 425),
    15: (10, 360),
    16: (10, 290),
    17: (10, 230),
    18: (10, 160),
    19: (10, 100),
    20: (10, 10),
    21: (100, 10),
    22: (170, 10),
    23: (235, 10),
    24: (300, 10),
    25: (365, 10),
    26: (430, 10),
    27: (495, 10),
    28: (560, 10),
    29: (625, 10),
    30: (720, 10),
    31: (720, 90),
    32: (720, 165),
    33: (720, 230),
    34: (720, 290),
    35: (720, 360),
    36: (720, 420),
    37: (720, 490),
    38: (720, 560),
    39: (720, 610),
    40: (720, 720)
}

# 찬스카드 종류 (위치 or 잃거나 얻는 연료나 자원, 출력텍스트)
chanceCards = {
	0: (10, "Go to Blackholl!"),
	1: (0, "Go to Earth!"),
	2: (random.randrange(0,41), "Go to Random!"),
	3: (20, "Go to Free Parking"),
	4: (3, "Get 3 fuel!"),
	5: (5, "Get 5 fuel!"),
	6: (50, "Get 50 resource!"),
	7: (100, "Get 100 resource!"),
	8: (-1, "Lose 1 fuel"),
	9: (-50, "Lose 50 resource")
}

# 커뮤니티 카드 종류 (잃거나 얻는 연료 or 자원, 출력텍스트)
communityCards = {
    0:(5,"Get 5 fuel!"),
    1:(7,"Get 7 fuel!"),
    2:(100,"Get 100 resource!"),
    3:(150,"Get 150 fuel!"),
    4:(-2,"Lose 2 fuel!"),
    5:(-3,"Lose 3 fuel!"),
    6:(-100,"Lose 100 resource!"),
    7:(150,"Lose 150 resource!"),

}

# 땅 정보 (연료소비, 자원획득) 
boardTile = {
    1: ("화성", -1, 15),
    3: ("세레스", -1, 20),
    6: ("목성", -1,40),
    8: ("토성", -1,60),
    9: ("천왕성", -1,50),
    11: ("해왕성", -2,90),
    13: ("명왕성", -2,80),
    14: ("하우메아", -2,100),
    16: ("마케마케", -2,110),
    18: ("에리스", -2,85),
    19: ("이오", -2,95),
    21: ("큰곰자리", -3,100),
    23: ("판도라", -3,110),
    24: ("오베론", -3,95),
    26: ("아리엘", -3,105),
    27: ("히페리온", -3,103),
    29: ("프로메테우스", -3,107),
    31: ("말머리성운", -4,120),
    32: ("태양", -4,125),
    34: ("수성", -4,130),
    37: ("금성", -4,134),
    39: ("달", -4,137)
}



def getResource(fuelToSpend, resourceToEarn):
    global fuel, resource

    fuel += fuelToSpend
    resource += resourceToEarn

def movePlayer(x, y):
    global player_x_pos, player_y_pos
    global playerTile

class mainMenuButton:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action=None) -> None:
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            screen.blit(img_act, (x_act, y_act))
            if click[0] and action != None:
                buttonClick.play()
                time.sleep(0.3)
                action()
        else:
            screen.blit(img_in, (x, y))

#말 선택 버튼 
class SelectButton:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action=None):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            screen.blit(img_act, (x_act, y_act))
            if click[0] and action != None:
                buttonClick.play()
                time.sleep(0.3)
                action(img_act)
        else:
            screen.blit(img_in, (x, y))


def renderResourceButton(img_in, x, y, width, height, img_act, x_act, y_act, fuel, resource):
    global resourceButtonBlock
    global printMode
    global spaceBlock

    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        screen.blit(img_act, (x_act, y_act))
        if click[0]:
            buttonClick.play()
            time.sleep(0.3)

            if fuel != None and resource != None:
                getResource(fuel, resource)

            resourceButtonBlock = True
            printMode = 0
            spaceBlock = False

    else:
        screen.blit(img_in, (x, y))

#주사위 버튼
class DiceButton:
    def __init__(self, x, y, width, height):
        self.x = x              # x 좌표
        self.y = y              # y 좌표
        self.width = width      # 너비
        self.height = height    # 높이
        self.txt = ""           # 출력 텍스트
        self.end_time = pg.time.get_ticks() # 문자 출력 끝나는 시간
    
    # Dice 문자를 출력하는 함수
    def printDice(self):
        printText(str(self.txt), "BLACK", 65, (460, 420))

    # Dice를 굴리는 함수
    def rollDice(self):
        global diceNum
        global spaceBlock

        diceNum = random.randrange(1, 13)

        self.txt = str(diceNum)

        dice_sound = pg.mixer.Sound("./bgm/Rolls_Dice.wav")
        dice_sound.play()

        spaceBlock = True
            
    
    # 문자 출력 끝나는 시간 설정하는 함수 (단위 ms)
    def timer(self, times):
        self.end_time = pg.time.get_ticks() + times

class Background:
    def __init__(self, bg_img, bg_x, bg_y) -> None:
        self.bg_x = bg_x
        self.bg_y = bg_y
        screen.blit(bg_img, (bg_x, bg_y))


def printText(msg, color, size, pos=(600, 600)):
    font = pg.font.SysFont("consolas", size)
    # font = pg.font.SysFont("malgungothic", size)
    textSurface = font.render(msg, True, pg.Color(color))
    textRect = textSurface.get_rect()
    textRect.topleft = pos
    screen.blit(textSurface, textRect)

#찬스카드 출력 폰트
def printText2(msg, color, size, pos=(600, 600)):
    font = pg.font.SysFont("Jalan.ttf", size)
    textSurface = font.render(msg, True, pg.Color(color))
    textRect = textSurface.get_rect()
    textRect.topleft = pos
    screen.blit(textSurface, textRect)

def printKorean(msg, color, size, pos=(600, 600)):
    # font = pg.font.SysFont("hangul", size)
    font = pg.font.Font("BMHANNAPro.ttf", size)
    textSurface = font.render(msg, True, pg.Color(color))
    textRect = textSurface.get_rect()
    textRect.topleft = pos
    screen.blit(textSurface, textRect)

def printSpace(msg, color, size, pos=(600, 600)):
    # font = pg.font.SysFont("hangul", size)
    font = pg.font.Font("aAbstractGroovy.ttf", size)
    textSurface = font.render(msg, True, pg.Color(color))
    textRect = textSurface.get_rect()
    textRect.topleft = pos
    screen.blit(textSurface, textRect)

def quitGame():
    pg.quit()
    sys.exit()

def textTimer(times):
    end_time = pg.time.get_ticks() + times
    return end_time


    
    

def mainMenu():
    menu = False
    
    while not menu:
        clock.tick(10)
        screen.fill(set_color)


        for event in pg.event.get():
            if event.type == pg.QUIT:
                menu = True
                quitGame()
        titleText = screen.blit(titleImg, (0,0))
        gamestartButton = mainMenuButton(startImg, 320, 500, 70, 40, clickStartImg, 320, 500, selectScreen)
        quitButton = mainMenuButton(quitImg, 610, 500, 70, 40, clickQuitImg, 610, 500, quitGame)

        pg.display.update()
    

# 선택 화면
def selectScreen():
    global fuel, resource
    global in_game_music
    global diceCnt
    global player_x_pos 
    global player_y_pos

    in_game_music.stop()

    select = True

    fuel = 20
    resource = 20
    diceCnt = 0
    player_x_pos = playerTile[0][0]
    player_y_pos = playerTile[0][1]

    while select:
        for event in pg.event.get():
            if event.type == pg.QUIT:
               quitGame()



        screen.fill(WHITE)
        #선택화면 배경사진
        screen.blit(selectText,(0,0))
        #첫번째 말 클릭
        cr1Select = SelectButton(cr1, 290, 355, 120, 130, clickedcr1Img,290,355,gameScreen)
        #두번째 말 클릭
        cr22select = SelectButton(cr2, 590, 360, 130, 140, clickedcr2Img, 590, 360,gameScreen)

        pg.display.update()
        clock.tick(15)


def gameScreen(img_act):
    
    global player_x_pos, player_y_pos
    global resourceButtonBlock
    global diceNum
    global diceCnt
    global fuel
    global resource
    global printMode
    global spaceBlock
 
    endTime = 0
    turnCnt = 0
    timerWait = None

    gameexit = False
    # Dice문자 출력용 객체
    clickDice = DiceButton(360, 270, 150, 150)
    #보드게임음악 플레이
    in_game_music.play(-1)

    #카드뽑기음악
    card_music = pg.mixer.Sound("./bgm/card.wav")

    #블랙홀음악
    jail_sound = pg.mixer.Sound("./bgm/jail.wav")

    #패배음악
    gameover_sound = pg.mixer.Sound("./bgm/gameover.wav")
    win_sound = pg.mixer.Sound("./bgm/winmusic.wav")
    
    img_act = pg.transform.scale(img_act, (70, 70))

    isBlocked = False                   # 특정부분의 코드가 프레임마다 실행되는 것을 방지하기 위한 플래그
    msgChance = ''                      # 찬스 내용
    msgCommunity = ''                   # 커뮤니티 내용
    blackhollFuelBlock = False          # 특정부분의 코드가 프레임마다 실행되는 것을 방지하기 위한 플래그
    musicBlock = False
    pressSpaceBlock = False

    while not gameexit:
        background_sound.stop()
        clock.tick(30)
        screen.fill(set_color)
        bg = Background(board, 0, 0)
        screen.blit(diceImg, (340, 310))
        screen.blit(sideImg, (800,0))
        screen.blit(img_act, (player_x_pos, player_y_pos))


        if pressSpaceBlock == False:
            pg.draw.rect(screen, BABYPINK, (59, 314, 700, 160), 0, 30)
            printSpace("Press the space Key", BLACK, 50, (110, 370))
            pg.draw.rect(screen, BLACK, (55, 310, 705, 165), 5, 30)


        #폰트
        turn = pg.font.Font('hangul.ttf',60)
        korean = pg.font.Font('hangul.ttf',40)
        sideNum = pg.font.Font('hangul.ttf',50)

        #폰트출력
        font1=turn.render('Turn',True,BLACK)
        font2=korean.render('목표자원',True,BLACK)
        font3=korean.render('현재 자원',True,BLACK)
        font4=korean.render('현재 원료',True,BLACK)
        font5 = sideNum.render(str(resource), True, BLACK)
        font6 = sideNum.render(str(fuel), True, BLACK)
        font7 = sideNum.render('3000', True, BLACK)
        font8 = sideNum.render(str(30 - turnCnt), True, BLACK)


        screen.blit(font1,(860,90))
        screen.blit(font8,(890,155))
        screen.blit(font2,(850,240))
        screen.blit(font7,(860,305))
        screen.blit(font3,(840,450))
        screen.blit(font4,(840,630))
        screen.blit(font5,(895,510))
        screen.blit(font6,(895,690))


        # 만약 현재 시간이 Dice 객체 안에 end_time보다 적을경우 clickDice 출력
        if pg.time.get_ticks() <= clickDice.end_time:
            clickDice.printDice()
            printMode = 1
        else:
            printMode = 2

        if pg.time.get_ticks() <= endTime and msgChance != '':    
            printText2(msgChance, "YELLOW", 50, (370, 150))
        else:
            msgChance = '' 
          
        if pg.time.get_ticks() <= endTime and msgCommunity != '':    
            printText2(msgCommunity, "GREEN", 50, (370, 200))
        else:
            msgCommunity = '' 
   
        # 찬스칸에 도착했을 경우
        if diceCnt in chanceTile:
            chanceNum = random.randrange(0, 10)

            if timerWait == None and timerAssignBlock == False:
                timerWait = pg.time.get_ticks() + 1000
                timerAssignBlock = True

            elif timerWait != None and pg.time.get_ticks() > timerWait:

                if isBlocked == False:
                    card_music.play()
                    msgChance = chanceCards[chanceNum][1]

                    if chanceNum == 0:
                        player_x_pos = playerTile[10][0]
                        player_y_pos = playerTile[10][1]
                        diceCnt = 10
                    elif chanceNum == 1:
                        player_x_pos = playerTile[0][0]
                        player_y_pos = playerTile[0][1]
                        diceCnt = 0
                    elif chanceNum == 2:
                        randomMove = random.randrange(0, 41)
                        player_x_pos = playerTile[randomMove][0]
                        player_y_pos = playerTile[randomMove][1]
                        diceCnt = randomMove
                    elif chanceNum == 3:
                        player_x_pos = playerTile[20][0]
                        player_y_pos = playerTile[20][1]
                        diceCnt = 20
                    elif chanceNum == 4:
                        fuel += 3
                    elif chanceNum == 5:
                        fuel += 5
                    elif chanceNum == 6:
                        resource += 50
                    elif chanceNum == 7:
                        resource += 100
                    elif chanceNum == 8:
                        fuel -= 1
                    elif chanceNum == 9:
                        resource -= 50
            
                    isBlocked = True
                    timerWait = None
                    spaceBlock = False
        #우주선 발전기금칸에 도착했을 경우
        elif diceCnt in communityTile:
            communityNum = random.randrange(0,8)

            if timerWait == None and timerAssignBlock == False:
                timerWait = pg.time.get_ticks() + 1000
                timerAssignBlock = True

            elif timerWait != None and pg.time.get_ticks() > timerWait:

                if isBlocked == False:
                    card_music.play()
                    msgCommunity = communityCards[communityNum][1]

                    if communityNum == 0:
                        fuel += 5
                    elif communityNum == 1:
                        fuel +=7
                    elif communityNum == 2:
                        resource +=100
                    elif communityNum == 3:
                        resource +=150
                    elif communityNum == 4:
                        fuel -= 2
                    elif communityNum == 5:
                        resource -=3
                    elif communityNum == 6:
                        resource -=100
                    elif communityNum == 7:
                        resource -150

                    isBlocked = True
                    timerWait = None
                    spaceBlock = False      
        #이용 감사료칸에 도착했을 경우
        elif diceCnt in thanksFee:
            if timerWait == None and timerAssignBlock == False:
                timerWait = pg.time.get_ticks() + 900
                timerAssignBlock = True

            elif timerWait != None and pg.time.get_ticks() > timerWait:
                resource -= 200
                timerWait = None
                spaceBlock = False      

        #행성에 도착했을 경우
        elif diceCnt in boardTile:
            if resourceButtonBlock == False and printMode == 2:
                pg.draw.rect(screen, BABYPINK, [20, 80, 760, 650], 0, 30)
                printKorean(boardTile[diceCnt][0] + "에 도착하였습니다.", BLACK, 50, (50, 180))
                printKorean("자원을 획득하시겠습니까?", BLACK, 70, (50, 280))
                printKorean("연료: " + str(boardTile[diceCnt][1]) + "         획득 자원: " + str(boardTile[diceCnt][2]), GRAY, 40, (50, 400))


                renderResourceButton(yesImg, -20, 500, 300, 150, clickYesImg, -20, 500, boardTile[diceCnt][1], boardTile[diceCnt][2])
                renderResourceButton(noImg, 390, 500, 300, 150, clickNoImg, 390, 500, None, None)

        #무료 우주여행칸에 도착할경우    
        elif diceCnt in freeTravel:
            if timerWait == None and timerAssignBlock == False:
                timerWait = pg.time.get_ticks() + 1200
                timerAssignBlock = True

            elif timerWait != None and pg.time.get_ticks() > timerWait:
                random_sound = pg.mixer.Sound("./bgm/random.wav")
                random_sound.play() 
                rand_tile=random.randrange(0,40)
                player_x_pos = playerTile[rand_tile][0]
                player_y_pos = playerTile[rand_tile][1]
                diceCnt = rand_tile
                timerWait = None
                spaceBlock = False
        #우주비행선 칸에 도착했을경우
        elif diceCnt in spaceCraft:
            if timerWait == None and timerAssignBlock == False:
                timerWait = pg.time.get_ticks() + 900
                timerAssignBlock = True

            elif timerWait != None and pg.time.get_ticks() > timerWait:
                fuel += 3
                timerWait = None
                spaceBlock = False
        # 파킹칸에 도착했을경우
        elif diceCnt == freeParking:
            if timerWait == None and timerAssignBlock == False:
                timerWait = pg.time.get_ticks() + 1000
                timerAssignBlock = True

            elif timerWait != None and pg.time.get_ticks() > timerWait:
                resource += 100
                timerWait = None
                spaceBlock = False

        #블랙홀로 이동   
        if player_x_pos == playerTile[30][0] and player_y_pos == playerTile[30][1] and blackhollFuelBlock == False:

            if timerWait == None and timerAssignBlock == False:
                timerWait = pg.time.get_ticks() + 1000
                timerAssignBlock = True

            elif timerWait != None and pg.time.get_ticks() > timerWait:
                # 일정 시간이 지나면
                jail_sound.play()
                player_x_pos = playerTile[10][0]
                player_y_pos = playerTile[10][1]
                diceCnt = 10
                turnCnt += 1
                fuel -= 5

                blackhollFuelBlock = True
                timerWait = None
                spaceBlock = False

        #주사위를 굴려 블랙홀 칸에 도착한 경우
        if diceCnt == 10 and blackhollFuelBlock == False:
            if timerWait == None and timerAssignBlock == False:
                timerWait = pg.time.get_ticks() + 1000
                timerAssignBlock = True

            elif timerWait != None and pg.time.get_ticks() > timerWait:
                jail_sound.play()
                fuel -=5
                blackhollFuelBlock = True
                timerWait = None
                spaceBlock = False

            
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameexit = True
                quitGame()
            if event.type == pg.KEYDOWN and event.key== pg.K_SPACE and spaceBlock == False:
                clickDice.rollDice()    # Dice객체 안 숫자를 랜덤하게 바꾸는 함수
                pressSpaceBlock = True
                clickDice.timer(1300)   # Dice객체 안 end_time을 설정하는 함수 (단위 ms)
                endTime = textTimer(2000)

                diceCnt += diceNum
                isBlocked = False
                blackhollFuelBlock = False
                resourceButtonBlock = False
                musicBlock = False
                timerAssignBlock = False

                if diceCnt >= 40:
                    diceCnt -= 40
                    turnCnt += 1
                    fuel += 10
                
                player_x_pos = playerTile[diceCnt][0]
                player_y_pos = playerTile[diceCnt][1] 


                
        if turnCnt == 30 or fuel <= 0:
            if resource < 3000:
                pressSpaceBlock = False
                resourceButtonBlock = True
                pg.draw.rect(screen, BABYPINK, [20, 80, 760, 650], 0, 30)
                screen.blit(gameoverImg, (-140, -40))
                regamestartButton = mainMenuButton(restartImg, 150, 470, 130, 130, clickRestartImg, 150, 470, selectScreen)
                quitButton = mainMenuButton(quitImg, 500, 535, 70, 40, clickQuitImg, 500, 535, quitGame)
                if musicBlock == False:
                    gameover_sound.play()
                    musicBlock = True

            
            else:
                pressSpaceBlock = False
                resourceButtonBlock = True
                pg.draw.rect(screen, BABYPINK, [20, 80, 760, 650], 0, 30)
                screen.blit(winImg, (-100, -40))
                regamestartButton = mainMenuButton(restartImg, 150, 470, 100, 100, clickRestartImg, 150, 470, selectScreen)
                quitButton = mainMenuButton(quitImg, 500, 535, 70, 40, clickQuitImg, 500, 535, quitGame)
                if musicBlock == False:
                    win_sound.play()
                    musicBlock = True


        

        pg.display.update()

mainMenu()
selectScreen()
gameScreen()