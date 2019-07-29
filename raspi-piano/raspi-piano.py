import RPi.GPIO as GPIO
from time import sleep
import wiringpi, os, platform, psutil, pygame
from pygame.locals import *

#Instrument settings
inst_select = 0
INST_PIANO  = 0
INST_HARP   = 1
INST_JAZOR  = 2
INST_ELEPI  = 3
INST_ELEBA  = 4

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

    # UART
    KEY14  = 14
    KEY15  = 15

    # No.4 not available
    # KEY4  = 4

    # Sound settings
    pygame.init()
    pygame.mixer.init(frequency = 22050, size = 16, channels = 1, buffer = 1024)

    # Grand Piano
    piano21 = pygame.mixer.Sound("sound/piano21.wav")
    piano26 = pygame.mixer.Sound("sound/piano26.wav")
    piano20 = pygame.mixer.Sound("sound/piano20.wav")
    piano19 = pygame.mixer.Sound("sound/piano19.wav")
    piano16 = pygame.mixer.Sound("sound/piano16.wav")
    piano13 = pygame.mixer.Sound("sound/piano13.wav")
    piano12 = pygame.mixer.Sound("sound/piano12.wav")
    piano6  = pygame.mixer.Sound("sound/piano6.wav")
    piano5  = pygame.mixer.Sound("sound/piano5.wav")
    piano7  = pygame.mixer.Sound("sound/piano7.wav")
    piano11 = pygame.mixer.Sound("sound/piano11.wav")
    piano8  = pygame.mixer.Sound("sound/piano8.wav")
    piano9  = pygame.mixer.Sound("sound/piano9.wav")
    piano25 = pygame.mixer.Sound("sound/piano25.wav")
    piano10 = pygame.mixer.Sound("sound/piano10.wav")
    piano24 = pygame.mixer.Sound("sound/piano24.wav")
    piano22 = pygame.mixer.Sound("sound/piano22.wav")
    piano23 = pygame.mixer.Sound("sound/piano23.wav")
    piano27 = pygame.mixer.Sound("sound/piano27.wav")
    piano18 = pygame.mixer.Sound("sound/piano18.wav")
    piano17 = pygame.mixer.Sound("sound/piano17.wav")
    piano3  = pygame.mixer.Sound("sound/piano3.wav")
    piano2  = pygame.mixer.Sound("sound/piano2.wav")

    # Harp
    harp21 = pygame.mixer.Sound("sound/harp21.wav")
    harp26 = pygame.mixer.Sound("sound/harp26.wav")
    harp20 = pygame.mixer.Sound("sound/harp20.wav")
    harp19 = pygame.mixer.Sound("sound/harp19.wav")
    harp16 = pygame.mixer.Sound("sound/harp16.wav")
    harp13 = pygame.mixer.Sound("sound/harp13.wav")
    harp12 = pygame.mixer.Sound("sound/harp12.wav")
    harp6  = pygame.mixer.Sound("sound/harp6.wav")
    harp5  = pygame.mixer.Sound("sound/harp5.wav")
    harp7  = pygame.mixer.Sound("sound/harp7.wav")
    harp11 = pygame.mixer.Sound("sound/harp11.wav")
    harp8  = pygame.mixer.Sound("sound/harp8.wav")
    harp9  = pygame.mixer.Sound("sound/harp9.wav")
    harp25 = pygame.mixer.Sound("sound/harp25.wav")
    harp10 = pygame.mixer.Sound("sound/harp10.wav")
    harp24 = pygame.mixer.Sound("sound/harp24.wav")
    harp22 = pygame.mixer.Sound("sound/harp22.wav")
    harp23 = pygame.mixer.Sound("sound/harp23.wav")
    harp27 = pygame.mixer.Sound("sound/harp27.wav")
    harp18 = pygame.mixer.Sound("sound/harp18.wav")
    harp17 = pygame.mixer.Sound("sound/harp17.wav")
    harp3  = pygame.mixer.Sound("sound/harp3.wav")
    harp2  = pygame.mixer.Sound("sound/harp2.wav")

    # Electric Base
    eleba21 = pygame.mixer.Sound("sound/eleba21.wav")
    eleba26 = pygame.mixer.Sound("sound/eleba26.wav")
    eleba20 = pygame.mixer.Sound("sound/eleba20.wav")
    eleba19 = pygame.mixer.Sound("sound/eleba19.wav")
    eleba16 = pygame.mixer.Sound("sound/eleba16.wav")
    eleba13 = pygame.mixer.Sound("sound/eleba13.wav")
    eleba12 = pygame.mixer.Sound("sound/eleba12.wav")
    eleba6  = pygame.mixer.Sound("sound/eleba6.wav")
    eleba5  = pygame.mixer.Sound("sound/eleba5.wav")
    eleba7  = pygame.mixer.Sound("sound/eleba7.wav")
    eleba11 = pygame.mixer.Sound("sound/eleba11.wav")
    eleba8  = pygame.mixer.Sound("sound/eleba8.wav")
    eleba9  = pygame.mixer.Sound("sound/eleba9.wav")
    eleba25 = pygame.mixer.Sound("sound/eleba25.wav")
    eleba10 = pygame.mixer.Sound("sound/eleba10.wav")
    eleba24 = pygame.mixer.Sound("sound/eleba24.wav")
    eleba22 = pygame.mixer.Sound("sound/eleba22.wav")
    eleba23 = pygame.mixer.Sound("sound/eleba23.wav")
    eleba27 = pygame.mixer.Sound("sound/eleba27.wav")
    eleba18 = pygame.mixer.Sound("sound/eleba18.wav")
    eleba17 = pygame.mixer.Sound("sound/eleba17.wav")
    eleba3  = pygame.mixer.Sound("sound/eleba3.wav")
    eleba2  = pygame.mixer.Sound("sound/eleba2.wav")

    # Electric Piano
    elepi21 = pygame.mixer.Sound("sound/elepi21.wav")
    elepi26 = pygame.mixer.Sound("sound/elepi26.wav")
    elepi20 = pygame.mixer.Sound("sound/elepi20.wav")
    elepi19 = pygame.mixer.Sound("sound/elepi19.wav")
    elepi16 = pygame.mixer.Sound("sound/elepi16.wav")
    elepi13 = pygame.mixer.Sound("sound/elepi13.wav")
    elepi12 = pygame.mixer.Sound("sound/elepi12.wav")
    elepi6  = pygame.mixer.Sound("sound/elepi6.wav")
    elepi5  = pygame.mixer.Sound("sound/elepi5.wav")
    elepi7  = pygame.mixer.Sound("sound/elepi7.wav")
    elepi11 = pygame.mixer.Sound("sound/elepi11.wav")
    elepi8  = pygame.mixer.Sound("sound/elepi8.wav")
    elepi9  = pygame.mixer.Sound("sound/elepi9.wav")
    elepi25 = pygame.mixer.Sound("sound/elepi25.wav")
    elepi10 = pygame.mixer.Sound("sound/elepi10.wav")
    elepi24 = pygame.mixer.Sound("sound/elepi24.wav")
    elepi22 = pygame.mixer.Sound("sound/elepi22.wav")
    elepi23 = pygame.mixer.Sound("sound/elepi23.wav")
    elepi27 = pygame.mixer.Sound("sound/elepi27.wav")
    elepi18 = pygame.mixer.Sound("sound/elepi18.wav")
    elepi17 = pygame.mixer.Sound("sound/elepi17.wav")
    elepi3  = pygame.mixer.Sound("sound/elepi3.wav")
    elepi2  = pygame.mixer.Sound("sound/elepi2.wav")

    # Jazz Organ
    jazor21 = pygame.mixer.Sound("sound/jazor21.wav")
    jazor26 = pygame.mixer.Sound("sound/jazor26.wav")
    jazor20 = pygame.mixer.Sound("sound/jazor20.wav")
    jazor19 = pygame.mixer.Sound("sound/jazor19.wav")
    jazor16 = pygame.mixer.Sound("sound/jazor16.wav")
    jazor13 = pygame.mixer.Sound("sound/jazor13.wav")
    jazor12 = pygame.mixer.Sound("sound/jazor12.wav")
    jazor6  = pygame.mixer.Sound("sound/jazor6.wav")
    jazor5  = pygame.mixer.Sound("sound/jazor5.wav")
    jazor7  = pygame.mixer.Sound("sound/jazor7.wav")
    jazor11 = pygame.mixer.Sound("sound/jazor11.wav")
    jazor8  = pygame.mixer.Sound("sound/jazor8.wav")
    jazor9  = pygame.mixer.Sound("sound/jazor9.wav")
    jazor25 = pygame.mixer.Sound("sound/jazor25.wav")
    jazor10 = pygame.mixer.Sound("sound/jazor10.wav")
    jazor24 = pygame.mixer.Sound("sound/jazor24.wav")
    jazor22 = pygame.mixer.Sound("sound/jazor22.wav")
    jazor23 = pygame.mixer.Sound("sound/jazor23.wav")
    jazor27 = pygame.mixer.Sound("sound/jazor27.wav")
    jazor18 = pygame.mixer.Sound("sound/jazor18.wav")
    jazor17 = pygame.mixer.Sound("sound/jazor17.wav")
    jazor3  = pygame.mixer.Sound("sound/jazor3.wav")
    jazor2  = pygame.mixer.Sound("sound/jazor2.wav")

    # Instrumental
    inst_en_0 = pygame.mixer.Sound("sound/inst_en_grandpiano.wav")
    inst_en_1 = pygame.mixer.Sound("sound/inst_en_harp.wav")
    inst_en_2 = pygame.mixer.Sound("sound/inst_en_jazzorgan.wav")
    inst_en_3 = pygame.mixer.Sound("sound/inst_en_stageelectricpiano.wav")
    inst_en_4 = pygame.mixer.Sound("sound/inst_en_electricbase.wav")
    inst_jp_0 = pygame.mixer.Sound("sound/inst_jp_grandpiano.wav")
    inst_jp_1 = pygame.mixer.Sound("sound/inst_jp_harp.wav")
    inst_jp_2 = pygame.mixer.Sound("sound/inst_jp_jazzorgan.wav")
    inst_jp_3 = pygame.mixer.Sound("sound/inst_jp_stageelectricpiano.wav")
    inst_jp_4 = pygame.mixer.Sound("sound/inst_jp_electricbase.wav")

    print("Sound file set up(pygame)")

    # Callback functions
    def play21(key):
        if inst_select == 0:
            piano21.play()
        elif inst_select == 1:
            harp21.play()
        elif inst_select == 2:
            jazor21.play()
        elif inst_select == 3:
            elepi21.play()
        elif inst_select == 4:
            eleba21.play()
        else:
            print("Error invalid instrument number")

    def play26(key):
        if inst_select == 0:
            piano26.play()
        elif inst_select == 1:
            harp26.play()
        elif inst_select == 2:
            jazor26.play()
        elif inst_select == 3:
            elepi26.play()
        elif inst_select == 4:
            eleba26.play()
        else:
            print("Error invalid instrument number")

    def play20(key):
        if inst_select == 0:
            piano20.play()
        elif inst_select == 1:
            harp20.play()
        elif inst_select == 2:
            jazor20.play()
        elif inst_select == 3:
            elepi20.play()
        elif inst_select == 4:
            eleba20.play()
        else:
            print("Error invalid instrument number")

    def play19(key):
        if inst_select == 0:
            piano19.play()
        elif inst_select == 1:
            harp19.play()
        elif inst_select == 2:
            jazor19.play()
        elif inst_select == 3:
            elepi19.play()
        elif inst_select == 4:
            eleba19.play()
        else:
            print("Error invalid instrument number")

    def play16(key):
        if inst_select == 0:
            piano16.play()
        elif inst_select == 1:
            harp16.play()
        elif inst_select == 2:
            jazor16.play()
        elif inst_select == 3:
            elepi16.play()
        elif inst_select == 4:
            eleba16.play()
        else:
            print("Error invalid instrument number")

    def play13(key):
        if inst_select == 0:
            piano13.play()
        elif inst_select == 1:
            harp13.play()
        elif inst_select == 2:
            jazor13.play()
        elif inst_select == 3:
            elepi13.play()
        elif inst_select == 4:
            eleba13.play()
        else:
            print("Error invalid instrument number")

    def play12(key):
        if inst_select == 0:
            piano12.play()
        elif inst_select == 1:
            harp12.play()
        elif inst_select == 2:
            jazor12.play()
        elif inst_select == 3:
            elepi12.play()
        elif inst_select == 4:
            eleba12.play()
        else:
            print("Error invalid instrument number")

    def play6(key):
        if inst_select == 0:
            piano6.play()
        elif inst_select == 1:
            harp6.play()
        elif inst_select == 2:
            jazor6.play()
        elif inst_select == 3:
            elepi6.play()
        elif inst_select == 4:
            eleba6.play()
        else:
            print("Error invalid instrument number")

    def play5(key):
        if inst_select == 0:
            piano5.play()
        elif inst_select == 1:
            harp5.play()
        elif inst_select == 2:
            jazor5.play()
        elif inst_select == 3:
            elepi5.play()
        elif inst_select == 4:
            eleba5.play()
        else:
            print("Error invalid instrument number")

    def play7(key):
        if inst_select == 0:
            piano7.play()
        elif inst_select == 1:
            harp7.play()
        elif inst_select == 2:
            jazor7.play()
        elif inst_select == 3:
            elepi7.play()
        elif inst_select == 4:
            eleba7.play()
        else:
            print("Error invalid instrument number")

    def play11(key):
        if inst_select == 0:
            piano11.play()
        elif inst_select == 1:
            harp11.play()
        elif inst_select == 2:
            jazor11.play()
        elif inst_select == 3:
            elepi11.play()
        elif inst_select == 4:
            eleba11.play()
        else:
            print("Error invalid instrument number")

    def play8(key):
        if inst_select == 0:
            piano8.play()
        elif inst_select == 1:
            harp8.play()
        elif inst_select == 2:
            jazor8.play()
        elif inst_select == 3:
            elepi8.play()
        elif inst_select == 4:
            eleba8.play()
        else:
            print("Error invalid instrument number")

    def play9(key):
        if inst_select == 0:
            piano9.play()
        elif inst_select == 1:
            harp9.play()
        elif inst_select == 2:
            jazor9.play()
        elif inst_select == 3:
            elepi9.play()
        elif inst_select == 4:
            eleba9.play()
        else:
            print("Error invalid instrument number")

    def play25(key):
        if inst_select == 0:
            piano25.play()
        elif inst_select == 1:
            harp25.play()
        elif inst_select == 2:
            jazor25.play()
        elif inst_select == 3:
            elepi25.play()
        elif inst_select == 4:
            eleba25.play()
        else:
            print("Error invalid instrument number")

    def play10(key):
        if inst_select == 0:
            piano10.play()
        elif inst_select == 1:
            harp10.play()
        elif inst_select == 2:
            jazor10.play()
        elif inst_select == 3:
            elepi10.play()
        elif inst_select == 4:
            eleba10.play()
        else:
            print("Error invalid instrument number")

    def play24(key):
        if inst_select == 0:
            piano24.play()
        elif inst_select == 1:
            harp24.play()
        elif inst_select == 2:
            jazor24.play()
        elif inst_select == 3:
            elepi24.play()
        elif inst_select == 4:
            eleba24.play()
        else:
            print("Error invalid instrument number")

    def play22(key):
        if inst_select == 0:
            piano22.play()
        elif inst_select == 1:
            harp22.play()
        elif inst_select == 2:
            jazor22.play()
        elif inst_select == 3:
            elepi22.play()
        elif inst_select == 4:
            eleba22.play()
        else:
            print("Error invalid instrument number")

    def play23(key):
        if inst_select == 0:
            piano23.play()
        elif inst_select == 1:
            harp23.play()
        elif inst_select == 2:
            jazor23.play()
        elif inst_select == 3:
            elepi23.play()
        elif inst_select == 4:
            eleba23.play()
        else:
            print("Error invalid instrument number")

    def play27(key):
        if inst_select == 0:
            piano27.play()
        elif inst_select == 1:
            harp27.play()
        elif inst_select == 2:
            jazor27.play()
        elif inst_select == 3:
            elepi27.play()
        elif inst_select == 4:
            eleba27.play()
        else:
            print("Error invalid instrument number")

    def play18(key):
        if inst_select == 0:
            piano18.play()
        elif inst_select == 1:
            harp18.play()
        elif inst_select == 2:
            jazor18.play()
        elif inst_select == 3:
            elepi18.play()
        elif inst_select == 4:
            eleba18.play()
        else:
            print("Error invalid instrument number")

    def play17(key):
        if inst_select == 0:
            piano17.play()
        elif inst_select == 1:
            harp17.play()
        elif inst_select == 2:
            jazor17.play()
        elif inst_select == 3:
            elepi17.play()
        elif inst_select == 4:
            eleba17.play()
        else:
            print("Error invalid instrument number")

    def play3(key):
        if inst_select == 0:
            piano3.play()
        elif inst_select == 1:
            harp3.play()
        elif inst_select == 2:
            jazor3.play()
        elif inst_select == 3:
            elepi3.play()
        elif inst_select == 4:
            eleba3.play()
        else:
            print("Error invalid instrument number")

    def play2(key):
        if inst_select == 0:
            piano2.play()
        elif inst_select == 1:
            harp2.play()
        elif inst_select == 2:
            jazor2.play()
        elif inst_select == 3:
            elepi2.play()
        elif inst_select == 4:
            eleba2.play()
        else:
            print("Error invalid instrument number")

    def play14(key):
        global inst_select
        inst_select += 1
        if inst_select > 4:
            inst_select = 0
        print("Instrument No." + str(inst_select))

        if inst_select == 0:
            inst_en_0.play()
            print("Grand Piano")
        elif inst_select == 1:
            inst_en_1.play()
            print("Harp")
        elif inst_select == 2:
            inst_en_2.play()
            print("Jazz Organ")
        elif inst_select == 3:
            inst_en_3.play()
            print("Stage Electric Piano")
        elif inst_select == 4:
            inst_en_4.play()
            print("Electric Base")
        else:
            print("Error invalid instrument number")
        
    def play15(key):
        global inst_select
        inst_select -= 1
        if inst_select < 0:
            inst_select = 4
        print("Instrument No." + str(inst_select))

        if inst_select == 0:
            inst_jp_0.play()
            print("Grand Piano")
        elif inst_select == 1:
            inst_jp_1.play()
            print("Harp")
        elif inst_select == 2:
            inst_jp_2.play()
            print("Jazz Organ")
        elif inst_select == 3:
            inst_jp_3.play()
            print("Stage Electric Piano")
        elif inst_select == 4:
            inst_jp_4.play()
            print("Electric Base")
        else:
            print("Error invalid instrument number")

    # def play4(key):
    #     print("Key 4")

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

    #GPIO.setup(KEY4,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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

    #GPIO.add_event_detect(KEY4,  GPIO.RISING, callback=play4,   bouncetime=300)
    GPIO.add_event_detect(KEY14, GPIO.RISING, callback=play14,  bouncetime=1000)
    GPIO.add_event_detect(KEY15, GPIO.RISING, callback=play15,  bouncetime=1000)

    print("Starting main loop. Press ctrl+c to quit.")

    while True:
        try:
            sleep(0.5)
        except KeyboardInterrupt:
            pygame.mixer.quit()
            pygame.quit()
            del p
            break

    GPIO.cleanup()

if __name__ == "__main__":
    main()
