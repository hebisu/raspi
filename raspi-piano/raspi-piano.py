"""
raspi-piano.py
Electric piano application with Raspberry pi 3B
Watch introduction video -> https://vimeo.com/352014490
Written by Hiro Ebisu
"""
import random
import socket

import psutil
import pygame
import RPi.GPIO as GPIO

import julius_cli

# Instrument settings
inst_select = 0
INST_PIANO = 0  # Grand piano
INST_HARP = 1  # Harp
INST_JAZOR = 2  # Jazz organ
INST_ELEPI = 3  # Stage electric piano
INST_ELEBA = 4  # Electric base

# GPIO port settings
# key (BCM number)
KEY21 = 21
KEY26 = 26
KEY20 = 20
KEY19 = 19
KEY16 = 16
KEY13 = 13
KEY12 = 12
KEY6 = 6
KEY5 = 5
KEY7 = 7
KEY11 = 11
KEY8 = 8
KEY9 = 9
KEY25 = 25
KEY10 = 10
KEY24 = 24
KEY22 = 22
KEY23 = 23
KEY27 = 27
KEY18 = 18
KEY17 = 17
KEY3 = 3
KEY2 = 2

# UART
KEY14 = 14
KEY15 = 15

# No.4 not available
# KEY4  = 4


def main():
    """
    Main function
    Setup audio and gpio settings
    Run Julius
    """
    # Process priority setting
    process_priority = psutil.Process()
    print('PID: %s, Priority: %s' % (process_priority.pid,
                                     process_priority.nice()))

    # Highest priority
    process_priority.nice(-20)

    print('PID: %s, Priority: %s' % (process_priority.pid,
                                     process_priority.nice()))

    # Sound settings
    pygame.init()
    pygame.mixer.init(frequency=22050, size=16, channels=1, buffer=1024)

    # Grand Piano
    piano21 = pygame.mixer.Sound("sound/piano21.wav")
    piano26 = pygame.mixer.Sound("sound/piano26.wav")
    piano20 = pygame.mixer.Sound("sound/piano20.wav")
    piano19 = pygame.mixer.Sound("sound/piano19.wav")
    piano16 = pygame.mixer.Sound("sound/piano16.wav")
    piano13 = pygame.mixer.Sound("sound/piano13.wav")
    piano12 = pygame.mixer.Sound("sound/piano12.wav")
    piano6 = pygame.mixer.Sound("sound/piano6.wav")
    piano5 = pygame.mixer.Sound("sound/piano5.wav")
    piano7 = pygame.mixer.Sound("sound/piano7.wav")
    piano11 = pygame.mixer.Sound("sound/piano11.wav")
    piano8 = pygame.mixer.Sound("sound/piano8.wav")
    piano9 = pygame.mixer.Sound("sound/piano9.wav")
    piano25 = pygame.mixer.Sound("sound/piano25.wav")
    piano10 = pygame.mixer.Sound("sound/piano10.wav")
    piano24 = pygame.mixer.Sound("sound/piano24.wav")
    piano22 = pygame.mixer.Sound("sound/piano22.wav")
    piano23 = pygame.mixer.Sound("sound/piano23.wav")
    piano27 = pygame.mixer.Sound("sound/piano27.wav")
    piano18 = pygame.mixer.Sound("sound/piano18.wav")
    piano17 = pygame.mixer.Sound("sound/piano17.wav")
    piano3 = pygame.mixer.Sound("sound/piano3.wav")
    piano2 = pygame.mixer.Sound("sound/piano2.wav")

    # Harp
    harp21 = pygame.mixer.Sound("sound/harp21.wav")
    harp26 = pygame.mixer.Sound("sound/harp26.wav")
    harp20 = pygame.mixer.Sound("sound/harp20.wav")
    harp19 = pygame.mixer.Sound("sound/harp19.wav")
    harp16 = pygame.mixer.Sound("sound/harp16.wav")
    harp13 = pygame.mixer.Sound("sound/harp13.wav")
    harp12 = pygame.mixer.Sound("sound/harp12.wav")
    harp6 = pygame.mixer.Sound("sound/harp6.wav")
    harp5 = pygame.mixer.Sound("sound/harp5.wav")
    harp7 = pygame.mixer.Sound("sound/harp7.wav")
    harp11 = pygame.mixer.Sound("sound/harp11.wav")
    harp8 = pygame.mixer.Sound("sound/harp8.wav")
    harp9 = pygame.mixer.Sound("sound/harp9.wav")
    harp25 = pygame.mixer.Sound("sound/harp25.wav")
    harp10 = pygame.mixer.Sound("sound/harp10.wav")
    harp24 = pygame.mixer.Sound("sound/harp24.wav")
    harp22 = pygame.mixer.Sound("sound/harp22.wav")
    harp23 = pygame.mixer.Sound("sound/harp23.wav")
    harp27 = pygame.mixer.Sound("sound/harp27.wav")
    harp18 = pygame.mixer.Sound("sound/harp18.wav")
    harp17 = pygame.mixer.Sound("sound/harp17.wav")
    harp3 = pygame.mixer.Sound("sound/harp3.wav")
    harp2 = pygame.mixer.Sound("sound/harp2.wav")

    # Electric Base
    eleba21 = pygame.mixer.Sound("sound/eleba21.wav")
    eleba26 = pygame.mixer.Sound("sound/eleba26.wav")
    eleba20 = pygame.mixer.Sound("sound/eleba20.wav")
    eleba19 = pygame.mixer.Sound("sound/eleba19.wav")
    eleba16 = pygame.mixer.Sound("sound/eleba16.wav")
    eleba13 = pygame.mixer.Sound("sound/eleba13.wav")
    eleba12 = pygame.mixer.Sound("sound/eleba12.wav")
    eleba6 = pygame.mixer.Sound("sound/eleba6.wav")
    eleba5 = pygame.mixer.Sound("sound/eleba5.wav")
    eleba7 = pygame.mixer.Sound("sound/eleba7.wav")
    eleba11 = pygame.mixer.Sound("sound/eleba11.wav")
    eleba8 = pygame.mixer.Sound("sound/eleba8.wav")
    eleba9 = pygame.mixer.Sound("sound/eleba9.wav")
    eleba25 = pygame.mixer.Sound("sound/eleba25.wav")
    eleba10 = pygame.mixer.Sound("sound/eleba10.wav")
    eleba24 = pygame.mixer.Sound("sound/eleba24.wav")
    eleba22 = pygame.mixer.Sound("sound/eleba22.wav")
    eleba23 = pygame.mixer.Sound("sound/eleba23.wav")
    eleba27 = pygame.mixer.Sound("sound/eleba27.wav")
    eleba18 = pygame.mixer.Sound("sound/eleba18.wav")
    eleba17 = pygame.mixer.Sound("sound/eleba17.wav")
    eleba3 = pygame.mixer.Sound("sound/eleba3.wav")
    eleba2 = pygame.mixer.Sound("sound/eleba2.wav")

    # Electric Piano
    elepi21 = pygame.mixer.Sound("sound/elepi21.wav")
    elepi26 = pygame.mixer.Sound("sound/elepi26.wav")
    elepi20 = pygame.mixer.Sound("sound/elepi20.wav")
    elepi19 = pygame.mixer.Sound("sound/elepi19.wav")
    elepi16 = pygame.mixer.Sound("sound/elepi16.wav")
    elepi13 = pygame.mixer.Sound("sound/elepi13.wav")
    elepi12 = pygame.mixer.Sound("sound/elepi12.wav")
    elepi6 = pygame.mixer.Sound("sound/elepi6.wav")
    elepi5 = pygame.mixer.Sound("sound/elepi5.wav")
    elepi7 = pygame.mixer.Sound("sound/elepi7.wav")
    elepi11 = pygame.mixer.Sound("sound/elepi11.wav")
    elepi8 = pygame.mixer.Sound("sound/elepi8.wav")
    elepi9 = pygame.mixer.Sound("sound/elepi9.wav")
    elepi25 = pygame.mixer.Sound("sound/elepi25.wav")
    elepi10 = pygame.mixer.Sound("sound/elepi10.wav")
    elepi24 = pygame.mixer.Sound("sound/elepi24.wav")
    elepi22 = pygame.mixer.Sound("sound/elepi22.wav")
    elepi23 = pygame.mixer.Sound("sound/elepi23.wav")
    elepi27 = pygame.mixer.Sound("sound/elepi27.wav")
    elepi18 = pygame.mixer.Sound("sound/elepi18.wav")
    elepi17 = pygame.mixer.Sound("sound/elepi17.wav")
    elepi3 = pygame.mixer.Sound("sound/elepi3.wav")
    elepi2 = pygame.mixer.Sound("sound/elepi2.wav")

    # Jazz Organ
    jazor21 = pygame.mixer.Sound("sound/jazor21.wav")
    jazor26 = pygame.mixer.Sound("sound/jazor26.wav")
    jazor20 = pygame.mixer.Sound("sound/jazor20.wav")
    jazor19 = pygame.mixer.Sound("sound/jazor19.wav")
    jazor16 = pygame.mixer.Sound("sound/jazor16.wav")
    jazor13 = pygame.mixer.Sound("sound/jazor13.wav")
    jazor12 = pygame.mixer.Sound("sound/jazor12.wav")
    jazor6 = pygame.mixer.Sound("sound/jazor6.wav")
    jazor5 = pygame.mixer.Sound("sound/jazor5.wav")
    jazor7 = pygame.mixer.Sound("sound/jazor7.wav")
    jazor11 = pygame.mixer.Sound("sound/jazor11.wav")
    jazor8 = pygame.mixer.Sound("sound/jazor8.wav")
    jazor9 = pygame.mixer.Sound("sound/jazor9.wav")
    jazor25 = pygame.mixer.Sound("sound/jazor25.wav")
    jazor10 = pygame.mixer.Sound("sound/jazor10.wav")
    jazor24 = pygame.mixer.Sound("sound/jazor24.wav")
    jazor22 = pygame.mixer.Sound("sound/jazor22.wav")
    jazor23 = pygame.mixer.Sound("sound/jazor23.wav")
    jazor27 = pygame.mixer.Sound("sound/jazor27.wav")
    jazor18 = pygame.mixer.Sound("sound/jazor18.wav")
    jazor17 = pygame.mixer.Sound("sound/jazor17.wav")
    jazor3 = pygame.mixer.Sound("sound/jazor3.wav")
    jazor2 = pygame.mixer.Sound("sound/jazor2.wav")

    # Instrumental select voice play
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
        """
        Play wave file No.21 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano21.play()
        elif inst_select == INST_HARP:
            harp21.play()
        elif inst_select == INST_JAZOR:
            jazor21.play()
        elif inst_select == INST_ELEPI:
            elepi21.play()
        elif inst_select == INST_ELEBA:
            eleba21.play()
        else:
            print("Error invalid instrument number")
        return key

    def play26(key):
        """
        Play wave file No.26 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano26.play()
        elif inst_select == INST_HARP:
            harp26.play()
        elif inst_select == INST_JAZOR:
            jazor26.play()
        elif inst_select == INST_ELEPI:
            elepi26.play()
        elif inst_select == INST_ELEBA:
            eleba26.play()
        else:
            print("Error invalid instrument number")
        return key

    def play20(key):
        """
        Play wave file No.20 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano20.play()
        elif inst_select == INST_HARP:
            harp20.play()
        elif inst_select == INST_JAZOR:
            jazor20.play()
        elif inst_select == INST_ELEPI:
            elepi20.play()
        elif inst_select == INST_ELEBA:
            eleba20.play()
        else:
            print("Error invalid instrument number")
        return key

    def play19(key):
        """
        Play wave file No.19 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano19.play()
        elif inst_select == INST_HARP:
            harp19.play()
        elif inst_select == INST_JAZOR:
            jazor19.play()
        elif inst_select == INST_ELEPI:
            elepi19.play()
        elif inst_select == INST_ELEBA:
            eleba19.play()
        else:
            print("Error invalid instrument number")
        return key

    def play16(key):
        """
        Play wave file No.16 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano16.play()
        elif inst_select == INST_HARP:
            harp16.play()
        elif inst_select == INST_JAZOR:
            jazor16.play()
        elif inst_select == INST_ELEPI:
            elepi16.play()
        elif inst_select == INST_ELEBA:
            eleba16.play()
        else:
            print("Error invalid instrument number")
        return key

    def play13(key):
        """
        Play wave file No.13 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano13.play()
        elif inst_select == INST_HARP:
            harp13.play()
        elif inst_select == INST_JAZOR:
            jazor13.play()
        elif inst_select == INST_ELEPI:
            elepi13.play()
        elif inst_select == INST_ELEBA:
            eleba13.play()
        else:
            print("Error invalid instrument number")
        return key

    def play12(key):
        """
        Play wave file No.12 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano12.play()
        elif inst_select == INST_HARP:
            harp12.play()
        elif inst_select == INST_JAZOR:
            jazor12.play()
        elif inst_select == INST_ELEPI:
            elepi12.play()
        elif inst_select == INST_ELEBA:
            eleba12.play()
        else:
            print("Error invalid instrument number")
        return key

    def play6(key):
        """
        Play wave file No.6 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano6.play()
        elif inst_select == INST_HARP:
            harp6.play()
        elif inst_select == INST_JAZOR:
            jazor6.play()
        elif inst_select == INST_ELEPI:
            elepi6.play()
        elif inst_select == INST_ELEBA:
            eleba6.play()
        else:
            print("Error invalid instrument number")
        return key

    def play5(key):
        """
        Play wave file No.5 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano5.play()
        elif inst_select == INST_HARP:
            harp5.play()
        elif inst_select == INST_JAZOR:
            jazor5.play()
        elif inst_select == INST_ELEPI:
            elepi5.play()
        elif inst_select == INST_ELEBA:
            eleba5.play()
        else:
            print("Error invalid instrument number")
        return key

    def play7(key):
        """
        Play wave file No.7 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano7.play()
        elif inst_select == INST_HARP:
            harp7.play()
        elif inst_select == INST_JAZOR:
            jazor7.play()
        elif inst_select == INST_ELEPI:
            elepi7.play()
        elif inst_select == INST_ELEBA:
            eleba7.play()
        else:
            print("Error invalid instrument number")
        return key

    def play11(key):
        """
        Play wave file No.11 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano11.play()
        elif inst_select == INST_HARP:
            harp11.play()
        elif inst_select == INST_JAZOR:
            jazor11.play()
        elif inst_select == INST_ELEPI:
            elepi11.play()
        elif inst_select == INST_ELEBA:
            eleba11.play()
        else:
            print("Error invalid instrument number")
        return key

    def play8(key):
        """
        Play wave file No.8 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano8.play()
        elif inst_select == INST_HARP:
            harp8.play()
        elif inst_select == INST_JAZOR:
            jazor8.play()
        elif inst_select == INST_ELEPI:
            elepi8.play()
        elif inst_select == INST_ELEBA:
            eleba8.play()
        else:
            print("Error invalid instrument number")
        return key

    def play9(key):
        """
        Play wave file No.9 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano9.play()
        elif inst_select == INST_HARP:
            harp9.play()
        elif inst_select == INST_JAZOR:
            jazor9.play()
        elif inst_select == INST_ELEPI:
            elepi9.play()
        elif inst_select == INST_ELEBA:
            eleba9.play()
        else:
            print("Error invalid instrument number")
        return key

    def play25(key):
        """
        Play wave file No.25 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano25.play()
        elif inst_select == INST_HARP:
            harp25.play()
        elif inst_select == INST_JAZOR:
            jazor25.play()
        elif inst_select == INST_ELEPI:
            elepi25.play()
        elif inst_select == INST_ELEBA:
            eleba25.play()
        else:
            print("Error invalid instrument number")
        return key

    def play10(key):
        """
        Play wave file No.10 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano10.play()
        elif inst_select == INST_HARP:
            harp10.play()
        elif inst_select == INST_JAZOR:
            jazor10.play()
        elif inst_select == INST_ELEPI:
            elepi10.play()
        elif inst_select == INST_ELEBA:
            eleba10.play()
        else:
            print("Error invalid instrument number")
        return key

    def play24(key):
        """
        Play wave file No.24 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano24.play()
        elif inst_select == INST_HARP:
            harp24.play()
        elif inst_select == INST_JAZOR:
            jazor24.play()
        elif inst_select == INST_ELEPI:
            elepi24.play()
        elif inst_select == INST_ELEBA:
            eleba24.play()
        else:
            print("Error invalid instrument number")
        return key

    def play22(key):
        """
        Play wave file No.22 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano22.play()
        elif inst_select == INST_HARP:
            harp22.play()
        elif inst_select == INST_JAZOR:
            jazor22.play()
        elif inst_select == INST_ELEPI:
            elepi22.play()
        elif inst_select == INST_ELEBA:
            eleba22.play()
        else:
            print("Error invalid instrument number")
        return key

    def play23(key):
        """
        Play wave file No.23 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano23.play()
        elif inst_select == INST_HARP:
            harp23.play()
        elif inst_select == INST_JAZOR:
            jazor23.play()
        elif inst_select == INST_ELEPI:
            elepi23.play()
        elif inst_select == INST_ELEBA:
            eleba23.play()
        else:
            print("Error invalid instrument number")
        return key

    def play27(key):
        """
        Play wave file No.27 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano27.play()
        elif inst_select == INST_HARP:
            harp27.play()
        elif inst_select == INST_JAZOR:
            jazor27.play()
        elif inst_select == INST_ELEPI:
            elepi27.play()
        elif inst_select == INST_ELEBA:
            eleba27.play()
        else:
            print("Error invalid instrument number")
        return key

    def play18(key):
        """
        Play wave file No.18 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano18.play()
        elif inst_select == INST_HARP:
            harp18.play()
        elif inst_select == INST_JAZOR:
            jazor18.play()
        elif inst_select == INST_ELEPI:
            elepi18.play()
        elif inst_select == INST_ELEBA:
            eleba18.play()
        else:
            print("Error invalid instrument number")
        return key

    def play17(key):
        """
        Play wave file No.17 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano17.play()
        elif inst_select == INST_HARP:
            harp17.play()
        elif inst_select == INST_JAZOR:
            jazor17.play()
        elif inst_select == INST_ELEPI:
            elepi17.play()
        elif inst_select == INST_ELEBA:
            eleba17.play()
        else:
            print("Error invalid instrument number")
        return key

    def play3(key):
        """
        Play wave file No.3 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano3.play()
        elif inst_select == INST_HARP:
            harp3.play()
        elif inst_select == INST_JAZOR:
            jazor3.play()
        elif inst_select == INST_ELEPI:
            elepi3.play()
        elif inst_select == INST_ELEBA:
            eleba3.play()
        else:
            print("Error invalid instrument number")
        return key

    def play2(key):
        """
        Play wave file No.2 (GPIO BCM number)
        """
        if inst_select == INST_PIANO:
            piano2.play()
        elif inst_select == INST_HARP:
            harp2.play()
        elif inst_select == INST_JAZOR:
            jazor2.play()
        elif inst_select == INST_ELEPI:
            elepi2.play()
        elif inst_select == INST_ELEBA:
            eleba2.play()
        else:
            print("Error invalid instrument number")
        return key

    def play14(key):
        """
        Change instrument (GPIO BCM number 14)
        """
        global inst_select
        inst_select += 1
        if inst_select > INST_ELEBA:
            inst_select = INST_PIANO
        # print("Instrument No." + str(inst_select))
        # Call selected instrument
        if inst_select == INST_PIANO:
            inst_en_0.play()
            print("Grand Piano")
        elif inst_select == INST_HARP:
            inst_en_1.play()
            print("Harp")
        elif inst_select == INST_JAZOR:
            inst_en_2.play()
            print("Jazz Organ")
        elif inst_select == INST_ELEPI:
            inst_en_3.play()
            print("Stage Electric Piano")
        elif inst_select == INST_ELEBA:
            inst_en_4.play()
            print("Electric Base")
        else:
            print("Error invalid instrument number")
        return key

    def play15(key):
        """
        Change instrument (GPIO BCM number 15)
        """
        global inst_select
        inst_select -= 1
        if inst_select < INST_PIANO:
            inst_select = INST_ELEBA
        # print("Instrument No." + str(inst_select))
        # Call selected instrument
        if inst_select == INST_PIANO:
            inst_jp_0.play()
            print("Grand Piano")
        elif inst_select == INST_HARP:
            inst_jp_1.play()
            print("Harp")
        elif inst_select == INST_JAZOR:
            inst_jp_2.play()
            print("Jazz Organ")
        elif inst_select == INST_ELEPI:
            inst_jp_3.play()
            print("Stage Electric Piano")
        elif inst_select == INST_ELEBA:
            inst_jp_4.play()
            print("Electric Base")
        else:
            print("Error invalid instrument number")
        return key

    def voice_command_cb(words):
        """
        Callback function for Julius voice control
        """
        global inst_select
        # Select and call selected instrument
        cmd = "".join(words)
        if cmd == "グランドピアノ" or cmd == "ピアノ":
            inst_select = 0
            # Play English or Japanese voice by 50%
            if random.randint(0, 100) < 50:
                inst_jp_0.play()
            else:
                inst_en_0.play()
            print("Grand Piano")
        elif cmd == "ハープ":
            inst_select = 1
            # Play English or Japanese voice by 50%
            if random.randint(0, 100) < 50:
                inst_jp_1.play()
            else:
                inst_en_1.play()
            print("Harp")
        elif cmd == "ジャズオルガン" or cmd == "オルガン":
            inst_select = 2
            # Play English or Japanese voice by 50%
            if random.randint(0, 100) < 50:
                inst_jp_2.play()
            else:
                inst_en_2.play()
            print("Jazz Organ")
        elif (cmd == "ステージエレクトリックピアノ" or cmd == "エレクトリックピアノ"
              or cmd == "ステージエレピ" or cmd == "エレピ"):
            inst_select = 3
            # Play English or Japanese voice by 50%
            if random.randint(0, 100) < 50:
                inst_jp_3.play()
            else:
                inst_en_3.play()
            print("Stage Electric Piano")
        elif cmd == "エレクトリックベース" or cmd == "エレベ" or cmd == "ベース":
            inst_select = 4
            # Play English or Japanese voice by 50%
            if random.randint(0, 100) < 50:
                inst_jp_4.play()
            else:
                inst_en_4.play()
            print("Electric Base")
        else:
            print("Unknown command: ", cmd)
        return True

    # def play4(key):
    #     print("Key 4")
    #     return key

    # GPIO settings (BCM mode)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(KEY21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY9, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY3, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Physical pull up
    GPIO.setup(KEY2, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Physical pull up

    # GPIO.setup(KEY4,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(KEY15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # HW interrupt settings (bouncetime is to prevent contact bounce)
    GPIO.add_event_detect(KEY21, GPIO.RISING, callback=play21, bouncetime=300)
    GPIO.add_event_detect(KEY26, GPIO.RISING, callback=play26, bouncetime=300)
    GPIO.add_event_detect(KEY20, GPIO.RISING, callback=play20, bouncetime=300)
    GPIO.add_event_detect(KEY19, GPIO.RISING, callback=play19, bouncetime=300)
    GPIO.add_event_detect(KEY16, GPIO.RISING, callback=play16, bouncetime=300)
    GPIO.add_event_detect(KEY13, GPIO.RISING, callback=play13, bouncetime=300)
    GPIO.add_event_detect(KEY12, GPIO.RISING, callback=play12, bouncetime=300)
    GPIO.add_event_detect(KEY6, GPIO.RISING, callback=play6, bouncetime=300)
    GPIO.add_event_detect(KEY5, GPIO.RISING, callback=play5, bouncetime=300)
    GPIO.add_event_detect(KEY7, GPIO.RISING, callback=play7, bouncetime=300)
    GPIO.add_event_detect(KEY11, GPIO.RISING, callback=play11, bouncetime=300)
    GPIO.add_event_detect(KEY8, GPIO.RISING, callback=play8, bouncetime=300)
    GPIO.add_event_detect(KEY9, GPIO.RISING, callback=play9, bouncetime=300)
    GPIO.add_event_detect(KEY25, GPIO.RISING, callback=play25, bouncetime=300)
    GPIO.add_event_detect(KEY10, GPIO.RISING, callback=play10, bouncetime=300)
    GPIO.add_event_detect(KEY24, GPIO.RISING, callback=play24, bouncetime=300)
    GPIO.add_event_detect(KEY22, GPIO.RISING, callback=play22, bouncetime=300)
    GPIO.add_event_detect(KEY23, GPIO.RISING, callback=play23, bouncetime=300)
    GPIO.add_event_detect(KEY27, GPIO.RISING, callback=play27, bouncetime=300)
    GPIO.add_event_detect(KEY18, GPIO.RISING, callback=play18, bouncetime=300)
    GPIO.add_event_detect(KEY17, GPIO.RISING, callback=play17, bouncetime=300)
    # Physical pull up
    GPIO.add_event_detect(KEY3, GPIO.FALLING, callback=play3, bouncetime=300)
    # Physical pull up
    GPIO.add_event_detect(KEY2, GPIO.FALLING, callback=play2, bouncetime=300)

    # GPIO.add_event_detect(KEY4,  GPIO.RISING, callback=play4, bouncetime=300)
    GPIO.add_event_detect(KEY14, GPIO.RISING, callback=play14, bouncetime=1000)
    GPIO.add_event_detect(KEY15, GPIO.RISING, callback=play15, bouncetime=1000)

    print("Starting main loop. Press ctrl+c to quit.")

    # Connect Julius (voice recognition engine)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        julius_cli.julius_connect(client)
        julius_cli.julius_recv(voice_command_cb, client)
    print("Socket closed.")

    # Free objects
    pygame.mixer.quit()
    pygame.quit()
    print("pygame quit.")
    del process_priority
    print("Deleted process priority object.")
    GPIO.cleanup()
    print("GPIO cleanup.")


if __name__ == "__main__":
    main()
