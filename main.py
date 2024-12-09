import pyb
import lcd160cr
lcd = lcd160cr.LCD160CR('X')

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
            if touch_x > WIDTH // 2:
                run_motor(1, 1000)
            else:
                run_motor(0, 1000)
            # pin_1.high()
        # else:
        #     pin_1.low()


        pyb.delay(100)

detect_touch()



