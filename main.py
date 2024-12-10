import pyb
import lcd160cr
lcd = lcd160cr.LCD160CR('X')
from pyb import Timer

timer_4 = Timer(4)
timer_4.init(freq=10000)

WIDTH = 160
HEIGHT = 128

RED = lcd.rgb(255,0,0)
GREEN = lcd.rgb(0,255,0)
BLUE = lcd.rgb(0,0,255)
WHITE = lcd.rgb(255,255,255)
BLACK = lcd.rgb(0,0,0)

lcd.erase()
lcd.set_orient(lcd160cr.LANDSCAPE)

direction_pin = pyb.Pin('Y1', pyb.Pin.OUT_PP)
pulse_pin = pyb.Pin('Y2', pyb.Pin.OUT_PP)
test_pin = pyb.Pin('Y3', pyb.Pin.OUT_PP)

PULSE_DELAY = 1

def write_output(output):
    lcd.set_text_color(RED, BLACK)
    lcd.set_font(1, bold=False, trans=False, scroll=True)
    lcd.set_pos(0, HEIGHT - 10)
    lcd.write(output)


def draw_button():
    lcd.set_pen(RED, "")
    lcd.rect(0, 0, 50, 75)

def run_motor(direction, pulses):
    write_output("Running          ")
    if direction:
        direction_pin.high()
    else:
        direction_pin.low()
    for i in range(pulses):
        pulse_pin.high()
        pyb.delay(PULSE_DELAY)
        pulse_pin.low()
        pyb.delay(PULSE_DELAY)

    write_output("Done Running    ")

def detect_touch():
    while True:
        if lcd.is_touched():
            _, touch_x, touch_y = lcd.get_touch()
            # write_output(str(touch_x) + "    ")
            if pulse_object.count == 0:
                if touch_x > WIDTH // 2:
                    timer_4.callback(lambda t: pulse_object.toggle(timer_4, 1))
                    # run_motor(1, 1000)
                else:
                    timer_4.callback(lambda t: pulse_object.toggle(timer_4, 0))
                    # run_motor(0, 1000)
            else:
                pass
                # run_motor(0, 1000)
            # pin_1.high()
        # else:
        #     pin_1.low()


        pyb.delay(100)

def pulse(pulse_object, pulse_count):
    pulse_object.toggle()
    
    
class Pulse:
    def __init__(self, pin, pulse_count):
        self.state = False
        self.pin = pin
        self.count = 0
        self.pulse_count = pulse_count

        self.direction = 0
        direction_pin.low()

    def toggle(self, timer, direction):
        if self.direction == direction:
            pass
        else:
            self.direction = direction
            if direction:
                direction_pin.high()
            else:
                direction_pin.low()
        if self.state:
            self.pin.low()
        else:
            self.pin.high()
        self.state = not self.state
        self.count += 1
        if self.count >= self.pulse_count:
            self.count = 0
            timer.callback(None)


        

pulse_object = Pulse(pulse_pin, 6400 * 2)
detect_touch()