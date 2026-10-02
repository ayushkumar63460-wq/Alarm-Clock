import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}.")
    alarm_sound = "sound.mp3.mp3"
    is_running = True

    while is_running:

        current_time = datetime.datetime.now().strftime("%I:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP!")

            pygame.mixer.init()
            pygame.mixer.music.load(alarm_sound)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False


        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("ENTER THE ALARM TIME  (HH:MM:SS): ")
    set_alarm(alarm_time)

