let y = 0
let x = 0
for (let i = 0; i < 5; i++) {
    x = 0
    for (let i = 0; i < 5; i++) {
        led.plot(x, y)
        x += 1
        basic.pause(100)
    }
    y += 1
}
basic.forever(() => {

})