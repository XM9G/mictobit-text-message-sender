radio.setGroup(1)
let letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "space"]
let message = ""
let count = 0
input.onButtonPressed(Button.A, function on_button_pressed_a2() {
    
    
    if (input.buttonIsPressed(Button.B)) {
        
        radio.sendString(message)
        return
    }
    
    let letter = letters[count]
    basic.showString(letter)
    count += 1
})
input.onButtonPressed(Button.B, function on_button_pressed_b2() {
    
    let letter = letters[count - 1]
    if (letter == "space") {
        message += " "
    } else {
        message += letter
    }
    
    basic.showString(message)
    console.log(message)
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showString(receivedString)
})
