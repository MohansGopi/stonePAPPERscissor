import random
print('''
          ,-------------------------------.
          |  Island                       |
          | .---------------------------. |
          | |,---'!!!!!!`...'!,.'!!!!!!!| |
          | |'',.,'!!!,--.!!!!!!!!,-'%%%| |
          | |`'!!!!!!;/|||\--'%%%%%%%%%%| |
          | |!!!!!!!,||/||\\%%%%%%%%%%%%| |
          | !!,-'%%%$;/||\\\\###-.%%%%%%| |
          | |%%%%,-$/|||\\|\\\.###)%%%%%| |
          | |%%%(p$$$$::$$$_$$$&&,%%%%%%| |
          | |%%%%%`-.$$pp,' ;,--'%%%%%%%| |
          | `---------------------------' |
          | Land                      7   |
          | .---------------------------. |
          | |            ,              | |
          | |           /(              | |
          | |          /  \             | |
          | |         (   ))            | |
          | |          `--'             | |
          | |___________________________| |
          |      Illus.Tony Szczudlo      |
          |tm&C1993-1994 WoTC,Inc. 335/350|
          `------------------------------Gr
''')

print("\nWelcome to game of stone, papper,scissor\n")


stone = """
                  _______
              ---'   ____)
                    (_____)
                    (_____)
                    (____)
              ---.__(___)
"""

papper = ("""
                   _______
              ---'    ____)____
                         ______)
                        _______)
                       _______)
              ---.__________)
""")

scissor = ("""
                  _______
              ---'   ____)____
                        ______)
                     __________)
                    (____)
              ---.__(___)
""")

list = [stone,papper,scissor]
def loop():
  random_l = random.randint(0,2)
  user_input = input("play game ..... : s - stone, p - papper, c - scissor : ")
  user_input = user_input.lower()
  
  if user_input == 's':
    print(stone)
  elif user_input == 'p':
    print(papper)
  elif user_input == 'c':
    print(scissor)
  else:
    print("Wrong input")
    exit()
  
  
  sys_choose = list[random_l]
  print(sys_choose)
  
  if user_input == 's' and sys_choose == stone or user_input == 'p' and sys_choose == papper or user_input == 'c' and sys_choose == scissor:
    print("match is draw")
  elif user_input == 's' and sys_choose == scissor or user_input == 'c' and sys_choose==papper or user_input == 'p' and sys_choose == stone:
    print("Congratulation!  You win the game")
  elif user_input == 's' and sys_choose == papper or user_input == 'c' and sys_choose == stone or user_input == 'p' and sys_choose == scissor:
    print("Sorry, you have to try again....")

while True:
  loop()



