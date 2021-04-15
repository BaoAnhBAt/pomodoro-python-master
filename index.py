import time
from playsound import playsound

while (True):
    print('Start working in 25 minutes')
    for i in range(25):
        print('... doing %s minutes'%i)
        time.sleep(60)
    playsound('Midnight-chimes-sound-effect.mp3')

    print('Start relaxing in 5 minutes')
    for i in range(5):
        print('... relaxing %s minutes'%i)
        time.sleep(60)
    playsound('Midnight-chimes-sound-effect.mp3')
    input('Continue work ....')