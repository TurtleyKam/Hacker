from uagame import Window
from time import sleep

window = Window('Hacking', 600, 500)
window.set_font_color('green')
window.set_font_name('couriernew')
window.set_bg_color('black')
window.set_font_size(18)

line_y = 0
string_height = window.get_font_height()

window.draw_string('1 ATTEMPT(S) LEFT', 0, line_y)
window.update()
line_y = line_y + string_height

window.draw_string('DOG', 0, line_y)
window.update()
line_y = line_y + string_height

window.draw_string('PEPE', 0, line_y)
window.update()
line_y = line_y + string_height

guess = window.input_string('ENTER PASSWORD > ', 0, line_y)

window.clear()

if guess == 'PEPE':
    window.draw_string('SUCCESS!!', 0, line_y)
    window.update()
else:
    window.draw_string('FAILURE!!', 0, 0)
    window.update()
     
sleep(3)

window.clear()

window.input_string('PRESS ENTER TO QUIT', 0, 0)

window.close()