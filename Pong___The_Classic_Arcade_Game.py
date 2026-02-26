# ==================================================
# 🎰 Pong - The Classic Arcade Game 🎰
# Built with Python Turtle Graphics
# Player A: W/S keys | Player B: Up/Down arrows
# First to score wins! 🎉
# ==================================================

import turtle

# =============================================
# 🖥️ Window / Screen Setup
# =============================================
win = turtle.Screen()
win.title("🎰 Pong - The Classic Arcade Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)  # ⚡ Turn off auto-update for smooth animation

# =============================================
# 🔵 Paddle A (Left - Player 1)
# =============================================
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("#00e5ff")  # 💧 Cyan
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# =============================================
# 🔴 Paddle B (Right - Player 2)
# =============================================
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#ff4081")  # 💜 Pink
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# =============================================
# ⚡ Ball Setup
# =============================================
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("#ffd700")  # 🟡 Gold
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx =  0.15  # 🟢 Ball X speed
ball.dy = -0.15  # 🟢 Ball Y speed

# =============================================
# 📊 Score Setup
# =============================================
score_a = 0
score_b = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("🔵 0  |  0 🔴", align="center", font=("Courier", 24, "bold"))

# =============================================
# 📝 Score Update Helper
# =============================================
def update_score():
    """Clears and redraws the current score on screen."""
    score_display.clear()
    score_display.write(
        f"🔵 {score_a}  |  {score_b} 🔴",
        align="center",
        font=("Courier", 24, "bold")
    )

# =============================================
# 🎮 Paddle A Controls (W / S)
# =============================================
def paddle_a_up():
    """Move Paddle A up."""
    y = paddle_a.ycor()
    if y < 250:
        paddle_a.sety(y + 20)

def paddle_a_down():
    """Move Paddle A down."""
    y = paddle_a.ycor()
    if y > -250:
        paddle_a.sety(y - 20)

# =============================================
# 🎮 Paddle B Controls (Up / Down)
# =============================================
def paddle_b_up():
    """Move Paddle B up."""
    y = paddle_b.ycor()
    if y < 250:
        paddle_b.sety(y + 20)

def paddle_b_down():
    """Move Paddle B down."""
    y = paddle_b.ycor()
    if y > -250:
        paddle_b.sety(y - 20)

# =============================================
# ⌨️ Keyboard Bindings
# =============================================
win.listen()
win.onkeypress(paddle_a_up,   "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up,   "Up")
win.onkeypress(paddle_b_down, "Down")

# =============================================
# 🔄 Main Game Loop
# =============================================
while True:
    win.update()  # 🖥️ Refresh screen

    # ➡️ Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # 🌅 Top & Bottom Wall Bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # 🌟 Right Wall - Player A scores
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        update_score()

    # 🌟 Left Wall - Player B scores
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        update_score()

    # 🔴 Ball hits Paddle B (right)
    if (340 < ball.xcor() < 360) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    # 🔵 Ball hits Paddle A (left)
    if (-360 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
