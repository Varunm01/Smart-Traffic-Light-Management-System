import RPi.GPIO as GPIO
import time


def traffic_light(count1, count2, count3):
    GPIO.setmode(GPIO.BCM)
    output_pins = [4, 17, 18, 27, 22, 23, 24, 25, 5]
    for pin in output_pins:
        GPIO.setup(pin, GPIO.OUT)
    
    if (count1>count2 and count1>count3):
        GPIO.output([18,27,24], GPIO.HIGH)
        time.sleep(20)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(17, GPIO.HIGH)
        time.sleep(3)
        GPIO.output([17,27,24], GPIO.LOW)
        if count2>count3:
            GPIO.output([4,23,24], GPIO.HIGH)
            time.sleep(20)
            GPIO.output(23, GPIO.LOW)
            GPIO.output(22, GPIO.HIGH)
            time.sleep(3)
            GPIO.output([22,4,24], GPIO.LOW)
            
            GPIO.output([4,27,5], GPIO.HIGH)
            time.sleep(20)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(25, GPIO.HIGH)
            time.sleep(3)
            GPIO.output([25,4,5], GPIO.LOW)
        else:
            GPIO.output([4,27,5], GPIO.HIGH)
            time.sleep(20)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(25, GPIO.HIGH)
            time.sleep(3)
            GPIO.output([25,4,27], GPIO.LOW)

            GPIO.output([4,23,24], GPIO.HIGH)
            time.sleep(20)
            GPIO.output(23, GPIO.LOW)
            GPIO.output(22, GPIO.HIGH)
            time.sleep(3)
            GPIO.output([22,4,24], GPIO.LOW)
            
    elif count2>count3:
        GPIO.output([4,23,24], GPIO.HIGH)
        time.sleep(20)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(22, GPIO.HIGH)
        time.sleep(3)
        GPIO.output([22,4,24], GPIO.LOW)
        if count1>count3:
            GPIO.output([18,27,24], GPIO.HIGH)
            time.sleep(20)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)
            time.sleep(3)
            GPIO.output([17,27,24], GPIO.LOW)
            
            GPIO.output([4,27,5], GPIO.HIGH)
            time.sleep(20)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(25, GPIO.HIGH)
            time.sleep(3)
            GPIO.output([25,4,5], GPIO.LOW)
        else:
            GPIO.output([4,27,5], GPIO.HIGH)
            time.sleep(20)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(25, GPIO.HIGH)
            time.sleep(3)
            GPIO.output([25,4,5], GPIO.LOW)

            GPIO.output([18,27,24], GPIO.HIGH)
            time.sleep(20)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)
            time.sleep(3)
            GPIO.output([17,27,24], GPIO.LOW)
    else:
        GPIO.output([4,27,5], GPIO.HIGH)
        time.sleep(20)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(25, GPIO.HIGH)
        time.sleep(3)
        GPIO.output([25,4,27], GPIO.LOW)
        if count1>count2:
            GPIO.output([18,27,24], GPIO.HIGH)
            time.sleep(20)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)
            time.sleep(3)
            GPIO.output([17,27,24], GPIO.LOW)
            
            GPIO.output([4,23,24], GPIO.HIGH)
            time.sleep(20)
            GPIO.output(23, GPIO.LOW)
            GPIO.output(22, GPIO.HIGH)
            time.sleep(3)
            GPIO.output([22,4,24], GPIO.LOW)
        else:
            GPIO.output([4,23,24], GPIO.HIGH)
            time.sleep(20)
            GPIO.output(23, GPIO.LOW)
            GPIO.output(22, GPIO.HIGH)
            time.sleep(3)
            GPIO.output([22,4,24], GPIO.LOW)

            GPIO.output([18,27,24], GPIO.HIGH)
            time.sleep(20)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)
            time.sleep(3)
            GPIO.output([17,27,24], GPIO.LOW)
            
            
    for pin in output_pins:
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()
