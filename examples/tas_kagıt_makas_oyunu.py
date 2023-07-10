import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock,paper,scissors] # ekrana görsel kodları yazdırmak için indeks numarasından seçmek için değişkenler liste içine atıldı
choices = []        # Seçimler için bir liste değişkeni oluşturuldu
choice =int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")) # Kullanıcıdan seçimi alınıp değişkene atandı
choices.append(choice)      # Kullanıcının seçimi seçimler listesine eklendi
comp_choice = random.randint(0,2) # Birlgisayarın seçimi için rastgele değer üretildi
choices.append(comp_choice)  # bilgisayarın seçimi seçimlere eklendi

wins = [[1,0],[0,2],[2,1]]    # kullanıcın kazanma kombinasyonları
loses = [[0,1],[2,0],[1,2]]     # Kullanıcının kaybetme kombinasyonları
if choices in wins:  # eğer seçimler kazanan kombinasyınundaysa
    print("your choice :\n", game_images[choice], "\nComputer choice: \n",game_images[comp_choice], "\n You are WİN!!!")
elif choices in loses: # eğer seçimler kaybeden kombinasyonlarındaysa
    print("your choice :\n", game_images[choice], "\nComputer choice: \n",game_images[comp_choice], "\n You are LOSE!!!\n")
else:  # diğer durumlar için
    print("play again")