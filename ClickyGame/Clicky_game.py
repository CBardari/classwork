
import arcade
import math
from random import seed
from random import randint

WIDTH = 800
HEIGHT = 600

window = arcade.Window(WIDTH, HEIGHT, "My Clicker Game")
arcade.set_background_color(arcade.color.BLACK)

# Initialize your variables here
middle_x = WIDTH // 2
middle_y = HEIGHT // 2
Radius_white_circle_ls = 10
Radius_ws_ls_max = min(WIDTH // 2, HEIGHT // 2)
Radius_ws_increase_size = 25
Radius_ws_det = 0
ticks = 0
second_counter = 0
LetterCom = "String"
bubble_one_radius = randint(40, 80)
bubble_one_x = randint(0 + bubble_one_radius, WIDTH - bubble_one_radius)
bubble_one_y = randint(0 + bubble_one_radius, int(HEIGHT * 0.85) - bubble_one_radius)
bubble_two_radius = randint(40, 80)
bubble_two_x = randint(0 + bubble_one_radius, WIDTH - bubble_one_radius)
bubble_two_y = randint(0 + bubble_one_radius, int(HEIGHT * 0.85) - bubble_one_radius)
bubble_three_radius = randint(40, 80)
bubble_three_x = randint(0 + bubble_one_radius, WIDTH - bubble_one_radius)
bubble_three_y = randint(0 + bubble_one_radius, int(HEIGHT * 0.85) - bubble_one_radius)
LettersRan = randint(1, 3)
LetterChange = 0
Letters_com_1 = "cat"
Letters_com_2 = "bat"
Letters_com_3 = "rat"
ChangePosition = 0
Correct = 0
Wrong = 0


@window.event("on_draw")
def game_loop():
    # import global variables here.
    global Correct
    global Wrong
    global middle_x
    global middle_y
    global Radius_white_circle_ls
    global Radius_ws_ls_max
    global Radius_ws_det
    global Radius_ws_increase_size
    global second_counter
    global ticks
    global LetterCom
    global bubble_one_x
    global bubble_one_y
    global bubble_two_x
    global bubble_two_y
    global bubble_three_x
    global bubble_three_y
    global bubble_one_radius
    global bubble_two_radius
    global bubble_three_radius
    global LetterCom
    global LettersRan
    global LetterChange
    global bubble_one_radius
    global Letters_com_1
    global Letters_com_2
    global Letters_com_3
    global ChangePosition
    # update your variables here.
    if LetterChange == 0:
        LettersRan = randint(1, 3)
        if LettersRan == 1:
            LetterCom = Letters_com_1
            LetterChange = 1
        if LettersRan == 2:
            LetterCom = Letters_com_2
            LetterChange = 1
        if LettersRan == 3:
            LetterCom = Letters_com_3
            LetterChange = 1
    if ChangePosition == 1:
        bubble_one_x = randint(0 + bubble_one_radius, WIDTH - bubble_one_radius)
        bubble_one_y = randint(0 + bubble_one_radius, int(HEIGHT * 0.85) - bubble_one_radius)
        bubble_two_x = randint(0 + bubble_one_radius, WIDTH - bubble_one_radius)
        bubble_two_y = randint(0 + bubble_one_radius, int(HEIGHT * 0.85) - bubble_one_radius)
        bubble_three_x = randint(0 + bubble_one_radius, WIDTH - bubble_one_radius)
        bubble_three_y = randint(0 + bubble_one_radius, int(HEIGHT * 0.85) - bubble_one_radius)
        bubble_one_radius = randint(40, 80)
        bubble_two_radius = randint(40, 80)
        bubble_three_radius = randint(40, 80)
        ChangePosition = 0
    ticks += 1
    second_counter = ticks / 15
    if Radius_ws_det == 5:
        Radius_white_circle_ls -= Radius_ws_increase_size
    if Radius_ws_det == 4 and Radius_white_circle_ls >= ((1/4) * Radius_ws_ls_max):
        Radius_white_circle_ls -= Radius_ws_increase_size
    if Radius_ws_det == 4 and Radius_white_circle_ls <= ((1/4) * Radius_ws_ls_max):
        Radius_ws_det = 5
    if Radius_ws_det == 4 and Radius_white_circle_ls <= (0.625 * Radius_ws_ls_max):
        Radius_white_circle_ls += Radius_ws_increase_size
    if Radius_ws_det == 4 and Radius_white_circle_ls <= ((0.625) * Radius_ws_ls_max):
        Radius_ws_det = 5
    if Radius_ws_det == 3 and Radius_white_circle_ls >= ((2/4) * Radius_ws_ls_max):
        Radius_white_circle_ls -= Radius_ws_increase_size
    if Radius_ws_det == 3 and Radius_white_circle_ls <= ((2/4) * Radius_ws_ls_max):
        Radius_ws_det = 4
    if Radius_ws_det == 2 and Radius_white_circle_ls <= (0.875 * Radius_ws_ls_max):
        Radius_white_circle_ls += Radius_ws_increase_size
    if Radius_ws_det == 2 and Radius_white_circle_ls <= ((0.875) * Radius_ws_ls_max):
        Radius_ws_det = 3
    if Radius_ws_det == 1 and Radius_white_circle_ls >= ((3/4) * Radius_ws_ls_max):
        Radius_white_circle_ls -= Radius_ws_increase_size
    if Radius_ws_det == 1 and Radius_white_circle_ls <= ((3/4) * Radius_ws_ls_max):
        Radius_ws_det = 2
    if Radius_white_circle_ls <= Radius_ws_ls_max and Radius_ws_det == 0:
        Radius_white_circle_ls += Radius_ws_increase_size
    if Radius_ws_det == 0 and Radius_white_circle_ls >= Radius_ws_ls_max:
        Radius_ws_det = 1
    # Draw things here.
    # Loading Screen
    arcade.start_render()
    arcade.draw_circle_filled(middle_x, middle_y, Radius_white_circle_ls, arcade.color.WHITE)
    print(second_counter)
    if second_counter >= 3:
        arcade.draw_text(f"Click on the bubble with the letters: {LetterCom} Score: {Correct - Wrong}", (0), (HEIGHT * 0.925), arcade.color.BLACK_LEATHER_JACKET, 25)
        arcade.draw_line(0, (0.875 * HEIGHT), WIDTH, (0.875 * HEIGHT), arcade.color.BLIZZARD_BLUE, 10)
        arcade.draw_circle_filled(bubble_two_x, bubble_two_y, bubble_two_radius, arcade.color.ANDROID_GREEN)
        arcade.draw_circle_filled(bubble_three_x, bubble_three_y, bubble_three_radius, arcade.color.ANDROID_GREEN)
        arcade.draw_circle_filled(bubble_one_x, bubble_one_y, bubble_one_radius, arcade.color.ANDROID_GREEN)
        arcade.draw_text(f"{Letters_com_1}", (bubble_one_x - bubble_one_radius + 25), (bubble_one_y - 25), arcade.color.BLACK_LEATHER_JACKET, 25)
        arcade.draw_text(f"{Letters_com_3}", (bubble_three_x - bubble_three_radius + 25), (bubble_three_y - 25), arcade.color.BLACK_LEATHER_JACKET, 25)
        arcade.draw_text(f"{Letters_com_2}", (bubble_two_x - bubble_two_radius + 25), (bubble_two_y - 25), arcade.color.BLACK_LEATHER_JACKET, 25)


@window.event
def on_mouse_press(mouse_x, mouse_y, button, modifiers):
    global Correct
    global Wrong
    global middle_x
    global middle_y
    global Radius_white_circle_ls
    global Radius_ws_ls_max
    global Radius_ws_det
    global Radius_ws_increase_size
    global second_counter
    global ticks
    global LetterCom
    global bubble_one_x
    global bubble_one_y
    global bubble_two_x
    global bubble_two_y
    global bubble_three_x
    global bubble_three_y
    global bubble_one_radius
    global bubble_two_radius
    global bubble_three_radius
    global LetterCom
    global LettersRan
    global LetterChange
    global bubble_one_radius
    global Letters_com_1
    global Letters_com_2
    global Letters_com_3
    global ChangePosition
    if button == arcade.MOUSE_BUTTON_LEFT:
        ChangePosition = 1
    if LettersRan == 1:
        a = max(mouse_x - bubble_one_x, bubble_one_x - mouse_x)
        b = max(mouse_y - bubble_one_y, bubble_one_y - mouse_y)
        c = math.sqrt(a * a + b * b)
        if c <= bubble_one_radius:
            Correct += 1
        else:
            Wrong += 1
    if LettersRan == 2:
        a = max(mouse_x - bubble_two_x, bubble_two_x - mouse_x)
        b = max(mouse_y - bubble_two_y, bubble_two_y - mouse_y)
        c = math.sqrt(a * a + b * b)
        if c <= bubble_two_radius:
            Correct += 1
        else:
            Wrong += 1
    if LettersRan == 3:
        a = max(mouse_x - bubble_three_x, bubble_three_x - mouse_x)
        b = max(mouse_y - bubble_three_y, bubble_three_y - mouse_y)
        c = math.sqrt((a * a) + (b * b))
        if c <= bubble_three_radius:
            Correct += 1
        else:
            Wrong += 1
    if button == arcade.MOUSE_BUTTON_RIGHT:
        print("You Right Clicked you are dumb you weren't supposed to do that")
    LetterChange = 0


arcade.run()
