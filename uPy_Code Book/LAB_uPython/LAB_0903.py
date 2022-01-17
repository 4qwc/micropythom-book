# ----------------------------------------
# LAB_0903 (PWM)
# MicroPython book by AppSoftTech
# ----------------------------------------
# DC Motor Control + L298N (Dual H-Bridge Motor Controller)

from machine import Pin, PWM
import time

# create PWM object on I/O pin
IN1 = PWM(Pin(26), freq=1000, duty=0)   # MotorA
IN2 = PWM(Pin(25), freq=1000, duty=0)
IN3 = PWM(Pin(17), freq=1000, duty=0)   # MotorB
IN4 = PWM(Pin(16), freq=1000, duty=0)

char_space = ' '

def motor_control(a, b):
    # MotorA
    if a > 0:
        print('MotorA forward', end=' : ')
        IN1.duty(a)         # Forward
        IN2.duty(0)
    elif a < 0:
        print('MotorA backward', end=' : ')
        IN1.duty(0)         # Backward
        IN2.duty(abs(a))
    else:
        print('MotorA stop', end=' : ')
        IN1.duty(0)         # Stop
        IN2.duty(0)

    # MotorB
    if b > 0:
        print('MotorB forward')
        IN3.duty(b)         # Forward
        IN4.duty(0)
    elif b < 0:
        print('MotorB backward')
        IN3.duty(0)         # Backward
        IN4.duty(abs(b))
    else:
        print('MotorB stop')
        IN3.duty(0)         # Stop
        IN4.duty(0)

while True:
    cmd = input('Motor cmd: ')
    if len(cmd) > 0:
        if cmd[0] == 'm':
            print('cmd:', cmd)
            s1 = cmd.find(char_space,0)
            s2 = cmd.find(char_space,2)
            if s1 != -1 and s2 != -1:
                a, b = cmd[s1:s2], cmd[s2:]
            elif s1 != -1 and s2 == -1:
                a, b = cmd[s1:], 0
            else:
                a, b = 0, 0

            motor_control(int(a), int(b))
        else:
            print('Invalid command')

    time.sleep_ms(100)
