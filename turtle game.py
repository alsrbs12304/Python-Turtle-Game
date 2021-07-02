import turtle
import random

t_score = 0
o_score = 0

# 볼 생성
f = turtle.Turtle()
f.shape("circle")
f.color("blue")
f.penup()
f.speed(10)
f_xpos = random.randint(-390,390)    
f_ypos = random.randint(-390,390)
f.goto(f_xpos,f_ypos)

# AWAY 터틀 생성
o = turtle.Turtle()
o.shape("turtle")
o.speed(10)
o.penup()
o.color("red")
o.goto(300,300)


# HOME 터틀 생성
t = turtle.Turtle()
t.shape("turtle")
t.speed(10)
t.penup()
t.color("black")
t.goto(-300, 300)

# 점수 바뀔 때 마다 터틀을 이동 시킬 수 없어서 새 객체로 생성
# HOME 점수 표시
ts = turtle.Turtle()
ts.penup()
ts.pendown()
ts.hideturtle()

# AWAY 점수 표시
os = turtle.Turtle()
os.penup()
os.pendown()
os.hideturtle()

# 게임 종료후 메세지 표시할 객체
m = turtle.Turtle()
m.goto(0,0)
m.hideturtle()

# HOME 점수 초기화 함수
def t_setScore(score): 
    ts.clear()
    ts.penup()
    ts.hideturtle()
    ts.setposition(-400, 350)
    ts.write("HOME 점수 : %s" % score, font=("Arial", 20, "normal"))

# AWAY 점수 초기화 함수
def o_setScore(score): 
    os.clear()
    os.penup()
    os.hideturtle()
    os.setposition(250, 350)
    os.write("AWAY 점수 : %s" % score, font=("Arial", 20, "normal"))

# HOME 터틀 움직임 함수
def t_turn_right():
    t.setheading(0)
    t.forward(20)
def t_turn_up():
    t.setheading(90)
    t.forward(20)
def t_turn_left():
    t.setheading(180)
    t.forward(20)
def t_turn_down():
    t.setheading(270)
    t.forward(20)

# AWAY 터틀 움직임 함수
def o_turn_right():
    o.setheading(0)
    o.forward(20)
def o_turn_up():
    o.setheading(90)
    o.forward(20)
def o_turn_left():
    o.setheading(180)
    o.forward(20)
def o_turn_down():
    o.setheading(270)
    o.forward(20)

# HOME 터틀 키 입력
turtle.listen()
turtle.onkeypress(t_turn_right,"Right")
turtle.onkeypress(t_turn_up,"Up")
turtle.onkeypress(t_turn_left,"Left")
turtle.onkeypress(t_turn_down,"Down")

# AWAY 터틀 키 입력
turtle.onkeypress(o_turn_right,"d")
turtle.onkeypress(o_turn_up,"w")
turtle.onkeypress(o_turn_left,"a")
turtle.onkeypress(o_turn_down,"s")

# 게임 시작 함수
def play():
    global t_score
    global o_score    
    global state
    state = True
    global winner

    # t(HOME)와 f(볼)의 거리가 18 이하이면 볼 잡기 성공
    # 잡은 후 HOME의 점수를 1 증가 후
    # 볼을 랜덤한 위치로 이동
    if t.distance(f) < 18:
        print("볼 잡기 성공")
        t_score = t_score + 1
        print(t_score,"점")
        t_setScore(t_score)
        f_xpos = random.randint(-390,390)    
        f_ypos = random.randint(-390,390)
        f.goto(f_xpos,f_ypos)

    # t(HOME)와 o(AWAY)의 거리가 18이하이면 터틀 잡기 성공
    # 잡은 후 AWAY의 점수를 1 증가 후
    # AWAY 터틀을 랜덤한 위치로 이동
    if t.distance(o) < 18:
        print("잡았다")
        o_score = o_score + 1
        print(o_score,"점")
        o_setScore(o_score)
        o_xpos = random.randint(-390,390)    
        o_ypos = random.randint(-390,390)
        o.goto(o_xpos,o_ypos)

    # HOME과 AWAY 의 점수중 하나라도 5점 이 되면
    # 게임 종료
    if t_score == 5 or o_score == 5:
        if t_score == 5:
            winner = "HOME"
        else:
            winner = "AWAY"
        print("게임 종료")
        state = False
        end()

    # state가 True이면 게임 계속 실행
    if state == True:
        turtle.ontimer(play,100)

play()
t_setScore(t_score)
o_setScore(o_score)

# 게임 종료 함수
def end():
    o.hideturtle()
    t.hideturtle()
    f.hideturtle()
    endMessage = "Game Over Winner : %s" % winner
    m.write(endMessage,align="center", font=("Arial", 30, "normal"))
