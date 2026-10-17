from time import sleep
import focar

ONE_METER_TIME = 5
TURN_TIME = 2
RETURN_TIME = 3


def three_point_turn():
    focar.forward_left(TURN_TIME)
    sleep(0.5)

    focar.backward_right(TURN_TIME)
    sleep(0.5)

    focar.forward_left(TURN_TIME)
    sleep(0.5)


def main():
    sleep(5)
    focar.led_on()

    focar.forward(ONE_METER_TIME)
    sleep(0.5)

    three_point_turn()

    focar.forward(RETURN_TIME)


    focar.led_off()


main()