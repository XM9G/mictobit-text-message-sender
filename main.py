radio.set_group(1)
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'space'
]
message = ''
count = 0
def on_button_pressed_a2():
    global count
    global message

    if input.button_is_pressed(Button.B):
            global message
            radio.send_string(message)
            return

    letter = letters[count]
    basic.show_string(letter)
    count +=1
    
input.on_button_pressed(Button.A, on_button_pressed_a2)

def on_button_pressed_b2():
    global message, count
    letter = letters[count - 1]
    if letter == 'space':
        message += ' '
    else:
        message += letter
    basic.show_string(message)
    print(message)
input.on_button_pressed(Button.B, on_button_pressed_b2)


def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)