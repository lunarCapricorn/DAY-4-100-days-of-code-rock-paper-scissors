import sys
from time import sleep

def typingEffect(text, speed, hangTime):
    for char in text:
        sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(hangTime)



def result(compChoice):
    switches = {
        0 : '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
        1 : '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
        2 : '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''',
    }
    return print(switches[compChoice])