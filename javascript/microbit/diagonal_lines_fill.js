let y = 0
let x = 0
let dots = 0
led.plot(0, 0)
basic.pause(100)
led.plot(0, 1)
led.plot(1, 0)
basic.pause(100)
led.plot(0, 2)
led.plot(1, 1)
led.plot(2, 0)
basic.pause(100)
led.plot(0, 3)
led.plot(1, 2)
led.plot(2, 1)
led.plot(3, 0)
basic.forever(() => {
    for (let index = 0; index <= 10; index++) {
        dots = index
        x = 0
        y = dots - 1
        for (let i = 0; i < dots; i++) {
            led.plot(x, y)
            x += 1
            y += -1
        }
        basic.pause(100)
    }
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
