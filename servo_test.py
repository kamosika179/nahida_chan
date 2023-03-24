import RPi.GPIO as GPIO
import time

#左から右へ、上から下へ振り向きます。

servo_pin = 18 # サーボモーターを接続したGPIOピン番号
servo_pin2 = 23
def init(pin_num):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_num, GPIO.OUT)
    pwm = GPIO.PWM(pin_num, 50) # 周波数50HzでPWMを設定
    pwm.start(0) # デューティ比0%で開始
    return pwm

def move(pwm, angle):
    duty = 2.5 + 10.0 * angle / 180 # 角度に応じたデューティ比を計算
    pwm.ChangeDutyCycle(duty) # デューティ比に設定
    time.sleep(0.3) # サーボモーターの動作に余裕をもたせる
    pwm.ChangeDutyCycle(0) # デューティ0で止める

if __name__ == '__main__':
    pwm = init(servo_pin)
    pwm2 = init(servo_pin2)
    try:
        while True:
            #move(pwm, 0) # 0度に動かす
            #time.sleep(3)
            for deg in range(80,160,5):
                move(pwm,deg)
                for deg_axis in range(50,100,5):
                    move(pwm2,deg_axis)
                
                #time.sleep(0.3)
            #move(pwm, 120) # 90度に動かす
            #time.sleep(3)
            #move(pwm, 180) # 180度に動かす
            #time.sleep(3)

            print("loop")

    except KeyboardInterrupt:
        pass

    pwm.stop()
    GPIO.cleanup()