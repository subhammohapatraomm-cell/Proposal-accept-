import turtle
import random

# =========================
# SCREEN
# =========================

screen = turtle.Screen()
screen.setup(900, 700)
screen.bgcolor("#080018")
screen.title("A Special Message ❤️")
screen.tracer(0)

HER_NAME = "YOUR LOVE"   # Apni girlfriend ka naam


# =========================
# TURTLES
# =========================

heart = turtle.Turtle()
heart.hideturtle()
heart.speed(0)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

stars = turtle.Turtle()
stars.hideturtle()
stars.speed(0)

buttons = turtle.Turtle()
buttons.hideturtle()
buttons.speed(0)


# =========================
# STARS
# =========================

star_positions = []

for i in range(45):
    x = random.randint(-430, 430)
    y = random.randint(-320, 320)

    if abs(x) < 250 and abs(y) < 180:
        continue

    star_positions.append((x, y))


def draw_stars():
    stars.clear()

    for x, y in star_positions:
        stars.penup()
        stars.goto(x, y)
        stars.color("white")
        stars.write(
            "✦",
            align="center",
            font=("Arial", random.randint(10, 18), "bold")
        )


# =========================
# HEART
# =========================

def draw_heart(size):

    heart.clear()
    heart.showturtle()

    heart.penup()
    heart.goto(0, -70)
    heart.setheading(140)

    heart.color("red")
    heart.fillcolor("red")

    heart.begin_fill()

    heart.forward(size)
    heart.circle(-size * 0.55, 200)

    heart.left(120)
    heart.circle(-size * 0.55, 200)

    heart.forward(size)

    heart.end_fill()


# =========================
# MAIN MESSAGE
# =========================

def main_message():

    writer.clear()

    writer.goto(0, 250)
    writer.color("#ff69b4")
    writer.write(
        "❤️ A SPECIAL MESSAGE FOR ❤️",
        align="center",
        font=("Arial", 24, "bold")
    )

    writer.goto(0, 195)
    writer.color("white")
    writer.write(
        HER_NAME,
        align="center",
        font=("Arial", 32, "bold")
    )

    writer.goto(0, -200)
    writer.color("#ffb6c1")
    writer.write(
        "Will You Be Mine? 💕",
        align="center",
        font=("Arial", 28, "bold")
    )


# =========================
# BUTTON
# =========================

def rectangle(x, y, width, height, color, label):

    buttons.penup()
    buttons.goto(x, y)

    buttons.color(color)
    buttons.fillcolor(color)

    buttons.begin_fill()

    for _ in range(2):
        buttons.forward(width)
        buttons.left(90)
        buttons.forward(height)
        buttons.left(90)

    buttons.end_fill()

    buttons.goto(x + width / 2, y + 15)
    buttons.color("white")

    buttons.write(
        label,
        align="center",
        font=("Arial", 18, "bold")
    )


def draw_buttons():

    buttons.clear()

    rectangle(-180, -310, 140, 60, "green", "YES ❤️")
    rectangle(40, -310, 140, 60, "#555555", "NO 😭")


# =========================
# YES
# =========================

def yes_clicked():

    # 🔴 सबसे पहले animation रोकने के लिए
    global animation_running
    animation_running = False

    # 🔴 Heart पूरी तरह हटाओ
    heart.clear()
    heart.hideturtle()

    # 🔴 पुराने buttons हटाओ
    buttons.clear()

    # 🔴 पुराना text हटाओ
    writer.clear()

    # =====================
    # NEW MESSAGE
    # =====================

    writer.goto(0, 130)
    writer.color("#ff69b4")

    writer.write(
        "SHE SAID YES! ❤️",
        align="center",
        font=("Arial", 40, "bold")
    )

    writer.goto(0, 70)
    writer.color("white")

    writer.write(
        "You just made my world brighter! 💕",
        align="center",
        font=("Arial", 22, "normal")
    )

    writer.goto(0, 20)
    writer.color("#ffd700")

    writer.write(
        "💍 Forever starts here 💍",
        align="center",
        font=("Arial", 25, "bold")
    )

    screen.update()


# =========================
# NO
# =========================

def no_clicked():

    writer.clear()

    writer.goto(0, 100)
    writer.color("white")

    writer.write(
        "Are you sure? 🥺",
        align="center",
        font=("Arial", 35, "bold")
    )

    writer.goto(0, 40)
    writer.color("#ff69b4")

    writer.write(
        "Think again... ❤️",
        align="center",
        font=("Arial", 25, "bold")
    )

    writer.goto(0, -10)
    writer.color("white")

    writer.write(
        "My heart is waiting... 💔",
        align="center",
        font=("Arial", 22, "normal")
    )

    screen.update()


# =========================
# CLICK
# =========================

def mouse_click(x, y):

    if -180 <= x <= -40 and -310 <= y <= -250:
        yes_clicked()

    elif 40 <= x <= 180 and -310 <= y <= -250:
        no_clicked()


# =========================
# ANIMATION
# =========================

heart_size = 170
direction = 1
animation_running = True


def animate_heart():

    global heart_size
    global direction

    # YES click ke baad animation dobara run nahi hogi
    if not animation_running:
        return

    draw_heart(heart_size)

    heart_size += direction * 3

    if heart_size >= 190:
        direction = -1

    if heart_size <= 165:
        direction = 1

    screen.update()

    screen.ontimer(animate_heart, 30)


# =========================
# START
# =========================

draw_stars()
main_message()
draw_buttons()

animate_heart()

screen.onclick(mouse_click)

screen.mainloop()



