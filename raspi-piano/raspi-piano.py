import RPi.GPIO as GPIO
from time import sleep
import wiringpi, os, platform, psutil, pygame
from pygame.locals import *

def main():
    p = psutil.Process()
    print('PID: %s, Priority: %s' % (p.pid, p.nice()))
    p.nice(-20) # Highest priority
    print('PID: %s, Priority: %s' % (p.pid, p.nice()))

    # GPIO port settings
    # key (BCM number)
    KEY21 = 21
    KEY26 = 26
    KEY20 = 20
    KEY19 = 19
    KEY16 = 16
    KEY13 = 13
    KEY12 = 12
    KEY6  = 6
    KEY5  = 5
    KEY7  = 7
    KEY11 = 11
    KEY8  = 8
    KEY9  = 9
    KEY25 = 25
    KEY10 = 10
    KEY24 = 24
    KEY22 = 22
    KEY23 = 23
    KEY27 = 27
    KEY18 = 18
    KEY17 = 17
    KEY3  = 3
    KEY2  = 2

    # Sound settings
    pygame.init()
    pygame.mixer.init(frequency = 22050, size = 16, channels = 1, buffer = 1024)
    w21 = pygame.mixer.Sound("21.wav")
    w26 = pygame.mixer.Sound("26.wav")
    w20 = pygame.mixer.Sound("20.wav")
    w19 = pygame.mixer.Sound("19.wav")
    w16 = pygame.mixer.Sound("16.wav")
    w13 = pygame.mixer.Sound("13.wav")
    w12 = pygame.mixer.Sound("12.wav")
    w6  = pygame.mixer.Sound("6.wav")
    w5  = pygame.mixer.Sound("5.wav")
    w7  = pygame.mixer.Sound("7.wav")
    w11 = pygame.mixer.Sound("11.wav")
    w8  = pygame.mixer.Sound("8.wav")
    w9  = pygame.mixer.Sound("9.wav")
    w25 = pygame.mixer.Sound("25.wav")
    w10 = pygame.mixer.Sound("10.wav")
    w24 = pygame.mixer.Sound("24.wav")
    w22 = pygame.mixer.Sound("22.wav")
    w23 = pygame.mixer.Sound("23.wav")
    w27 = pygame.mixer.Sound("27.wav")
    w18 = pygame.mixer.Sound("18.wav")
    w17 = pygame.mixer.Sound("17.wav")
    w3  = pygame.mixer.Sound("3.wav")
    w2  = pygame.mixer.Sound("2.wav")

    print("Sound file set up(pygame)")

    # Callback functions
    def play21(key):
        w21.play()

    def play26(key):
        w26.play()

    def play20(key):
        w20.play()

    def play19(key):
        w19.play()

    def play16(key):
        w16.play()

    def play13(key):
        w13.play()

    def play12(key):
        w12.play()

    def play6(key):
        w6.play()

    def play5(key):
        w5.play()

    def play7(key):
        w7.play()

    def play11(key):
        w11.play()

    def play8(key):
        w8.play()

    def play9(key):
        w9.play()

    def play25(key):
        w25.play()

    def play10(key):
        w10.play()

    def play24(key):
        w24.play()

    def play22(key):
        w22.play()

    def play23(key):
        w23.play()

    def play27(key):
        w27.play()

    def play18(key):
        w18.play()

    def play17(key):
        w17.play()

    def play3(key):
        w3.play()

    def play2(key):
        w2.play()

    # GPIO settings (BCM mode)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(KEY21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY6,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY5,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY7,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY8,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY9,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY3,  GPIO.IN, pull_up_down=GPIO.PUD_UP) # Physical pull up
    GPIO.setup(KEY2,  GPIO.IN, pull_up_down=GPIO.PUD_UP) # Physical pull up

    # HW interrupt settings
    GPIO.add_event_detect(KEY21, GPIO.RISING, callback=play21,  bouncetime=300)
    GPIO.add_event_detect(KEY26, GPIO.RISING, callback=play26,  bouncetime=300)
    GPIO.add_event_detect(KEY20, GPIO.RISING, callback=play20,  bouncetime=300)
    GPIO.add_event_detect(KEY19, GPIO.RISING, callback=play19,  bouncetime=300)
    GPIO.add_event_detect(KEY16, GPIO.RISING, callback=play16,  bouncetime=300)
    GPIO.add_event_detect(KEY13, GPIO.RISING, callback=play13,  bouncetime=300)
    GPIO.add_event_detect(KEY12, GPIO.RISING, callback=play12,  bouncetime=300)
    GPIO.add_event_detect(KEY6,  GPIO.RISING, callback=play6,   bouncetime=300)
    GPIO.add_event_detect(KEY5,  GPIO.RISING, callback=play5,   bouncetime=300)
    GPIO.add_event_detect(KEY7,  GPIO.RISING, callback=play7,   bouncetime=300)
    GPIO.add_event_detect(KEY11, GPIO.RISING, callback=play11,  bouncetime=300)
    GPIO.add_event_detect(KEY8,  GPIO.RISING, callback=play8,   bouncetime=300)
    GPIO.add_event_detect(KEY9,  GPIO.RISING, callback=play9,   bouncetime=300)
    GPIO.add_event_detect(KEY25, GPIO.RISING, callback=play25,  bouncetime=300)
    GPIO.add_event_detect(KEY10, GPIO.RISING, callback=play10,  bouncetime=300)
    GPIO.add_event_detect(KEY24, GPIO.RISING, callback=play24,  bouncetime=300)
    GPIO.add_event_detect(KEY22, GPIO.RISING, callback=play22,  bouncetime=300)
    GPIO.add_event_detect(KEY23, GPIO.RISING, callback=play23,  bouncetime=300)
    GPIO.add_event_detect(KEY27, GPIO.RISING, callback=play27,  bouncetime=300)
    GPIO.add_event_detect(KEY18, GPIO.RISING, callback=play18,  bouncetime=300)
    GPIO.add_event_detect(KEY17, GPIO.RISING, callback=play17,  bouncetime=300)
    GPIO.add_event_detect(KEY3,  GPIO.FALLING, callback=play3,  bouncetime=300) # Physical pull up
    GPIO.add_event_detect(KEY2,  GPIO.FALLING, callback=play2,  bouncetime=300) # Physical pull up

    while True:
        try:
            sleep(1.0)
        except KeyboardInterrupt:
            pygame.mixer.quit()
            pygame.quit()
            del p
            break

    GPIO.cleanup()

if __name__ == "__main__":
    main()
