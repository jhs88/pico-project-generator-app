from machine import Pin, Timer
import time

clk = Pin(16, Pin.OUT)
led = Pin("LED", Pin.OUT)
clk.off()
led.off()
monostable_trigger = Pin(15, Pin.IN, Pin.PULL_DOWN)
astable_monostable = Pin(10, Pin.IN, Pin.PULL_DOWN)
timer = Timer()
astable_monostable_last = time.ticks_ms()
astable = True

def wait_pin_change(pin):
    # wait for pin to change value
    # it needs to be stable for a continuous 50ms
    cur_value = pin.value()
    active = 0
    while active < 50:
        if pin.value() != cur_value:
            active += 1
        else:
            active = 0
        time.sleep_ms(1)

def btn_handler(pin):
    global astable_monostable
    global astable_monostable_last
    global timer, clk, astable
    if time.ticks_diff(time.ticks_ms(), astable_monostable_last) > 500:
        if astable == True:
            astable = False
            clk.off()
            led.off()
            timer.deinit()
            astable_monostable_last = time.ticks_ms()
            print("TURN OFF LED & TIMER")
        else:
            astable = True
            timer.init(freq=2, mode=Timer.PERIODIC, callback=clk_callback)
            astable_monostable_last = time.ticks_ms()
            print("TURN ON LED & TIMER")
    print(astable)        

astable_monostable.irq(trigger=Pin.IRQ_RISING, handler=btn_handler)

def clk_callback(timer):
    clk.toggle()
    led.toggle()
    
timer.init(freq=2, mode=Timer.PERIODIC, callback=clk_callback)

while True:
    wait_pin_change(monostable_trigger)
    if astable == False:
        clk.toggle()
        led.toggle()