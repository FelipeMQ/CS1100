#from pynput.mouse import Button, Controller
from libpynput.keyboard import Key, Controller

#mouse = Controller()
keyboard = Controller()
# Press and release space
keyboard.press(Key.space)
keyboard.release(Key.space)

# Type a lower case A; this will work even if no key on the
# physical keyboard is labelled 'A'
keyboard.press('a')
keyboard.release('a')

# Type two upper case As
keyboard.press('A')
keyboard.release('A')
with keyboard.pressed(Key.shift):
    keyboard.press('a')
    keyboard.release('a')

# Type 'Hello World' using the shortcut type method
keyboard.press(Key.ctrl_l)
keyboard.press(Key.esc)
keyboard.release(Key.ctrl_l)
keyboard.release(Key.esc)
# Read pointer position
#print('The current pointer position is {0}'.format(mouse.position))

# Set pointer position
#mouse.position = (10, 20)
#print('Now we have moved it to {0}'.format(mouse.position))

# Move pointer relative to current position
#mouse.move(5, -5)

# Press and release
#mouse.press(Button.left)
#mouse.release(Button.left)

# Double click; this is different from pressing and releasing
# twice on Mac OSX
#mouse.click(Button.left, 2)

# Scroll two steps down
#mouse.scroll(0, 2)