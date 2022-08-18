from os import name
import random

class Char():
    
         ## Character's Sheet ##
                
     def __init__(self, name, role):
               
          self.name = name
          self.role = role
          self.level = 1       
          self.strenght = 0
          self.agility = 0
          self.resistance = 0
          self.armor = 0
          self.fpower = 0                                           
          self.defense = 0                              
          self.mattack = 0
          self.rattack = 0
          self.life = 0
          self.cp = 0   
             
             ## Name generator ## 
                
          while True:
                   self.name = input("What's your name? ").title()         
                   if any(char.isdigit() for char in self.name):
                         print("No numbers on the name")                                        
                   elif self.name == "":
                           print("You cannot have a blank name")                           
                   elif any(not char.isalnum() for char in "".join(self.name.split())):    
                           print("No special characters")
                   elif len(self.name) > 20:     
                           print("Name cannot be longer than 20 digits including spaces.")
                   else:
                           print("Are you happy with the name " + self.name + "?")                                    
                           while True:
                                conf = input("Y or N ").title()
                                if conf == "Y":
                                       print("Welcome " + self.name + ".")                                       
                                       Char.attributes(self)
                                       return
                                elif conf == "N":
                                       print("Please choose another name")
                                       break
                                else:
                                       print("Invalid option")
                
                ## Attributes Allocation ##
        
     def attributes(self):
        
          print("""Time to set your attributes
You have 15 points to distribute among your 5 attributes.
The attributes are: Strenght, Agility, Endurance, Armor and Fire Power.
You can allocate max 5 points in one single attribute and no attribute can have a 0 value
                   """)    
          total = int(15)
                  
             ## Strenght ##
                   
          while True:       
                     self.strenght = input("How many points in Strenght? ")
                     if self.strenght == "":
                         print("Please input a value")
                     elif not self.strenght.isdigit():
                         print("Only numbers please")
                     elif int(self.strenght) <= 0 or int(self.strenght) > 5:
                         print("Choose a value above 1 and below 5")         
                     else:
                         print("Strenght is " + str(self.strenght))
                         total -= int(self.strenght)
                         print("you have now " + str(total) + " left")
                         break
                                      
                 ## Agility ##     
                   
          while True:
                        self.agility = input("How many points in Agility? ")
                        if self.agility == "":
                         print("Please input a value")
                        elif not self.agility.isdigit():
                         print("Only numbers please")
                        elif int(self.agility) <= 0 or int(self.agility) > 5:
                         print("Choose a value above 1 and below 5")            
                        else:
                         print("Agility is " + str(self.agility))
                         total -= int(self.agility)
                         print("you have now " + str(total) + " left")
                         break
                   
                   ## Resistance ##
                   
          while True:      
                        self.resistance = input("How many points in Resistance? ")
                        if self.resistance == "":
                         print("Please input a value")
                        elif not self.resistance.isdigit():
                         print("Only numbers please")
                        elif int(self.resistance) <= 0 or int(self.resistance) > 5:
                         print("Choose a value above 1 and below 5")           
                        else:
                         print("Resistance is " + str(self.resistance))
                         total -= int(self.resistance)
                         print("you have now " + str(total) + " left")
                         break             
                   
                   ## Armor ##
                   
          while True:
                    if total <= 0:
                        print("""You don't have more points to spend...
            Reseting distribution            
                        """)
                        Char.attributes(self)
                    else:    
                        self.armor = input("How many points in Armor? ")
                        if self.armor == "":
                         print("Please input a value")
                        elif not self.armor.isdigit():
                         print("Only numbers please")
                        elif int(self.armor) <= 0 or int(self.armor) > 5:
                         print("Choose a value above 1 and below 5")            
                        else:
                         print("Armor is " + str(self.armor))
                         total -= int(self.armor)
                         print("you have now " + str(total) + " left")
                         break           
                   
                   ## Fire Power ##
                   
          while True:
                        self.fpower = input("How many points in Fire Power? ")
                        total -= int(self.fpower)
                        if total < 0:
                            print("""You spent more points than you had available...
            Reseting distribution            
                        """)
                            Char.attributes(self)
                        elif self.fpower == "":
                            print("Please input a value")
                        elif not self.fpower.isdigit():
                            print("Only numbers please")
                        elif int(self.fpower) <= 0 or int(self.fpower) > 5:
                            print("Choose a value above 1 and below 5")
                        else:
                            if total > 0:
                                 print("""You didn't spend all your points...
            Reseting distribution...                  
                               """)
                                 Char.attributes(self)
                            else:
                                  print("Fire Power is " + str(self.fpower))                     
                                  print("you have now " + str(total) + " left")
                            break
              
          self.defense = int(self.armor) + int(self.agility)
          self.mattack = int(self.strenght) + int(self.agility)
          self.rattack = int(self.agility) + int(self.fpower)
          self.life = int(self.armor) + int(self.resistance) + 5   
          self.cp = (int(self.level) + int(self.strenght) + int(self.agility) + int(self.armor) + int(self.resistance) + int(self.fpower)) * 10
                                                                             
               ## Call character's menu ##    
        
     def playermenu(self):
             while True:
                          info = input("What do you want to check?\n P for Profile:\n I for Inventory or N: ").title()
                          if info == "P":
                              Char.status(self)
                              break
                          elif info == "I":
                              break
                          else:
                              print("Choose one option")
                              
                     ## Character's sheet ##
        
     def status(self):
               sheet = """
              
                         PROFILE           
               
               Name: {n}
               
               Role: {ro}
               Level: {le}                                 
               CP: {cp}
               
               Strenght: {s}
               Agility: {a}
               Resistance: {r}
               Armor: {aa}
               Fire Power: {f}
                                                 
               Meele Attack: {ma}
               Range Attack: {ra}
                                                   
               Defense: {d}
                                                 
               Life: {l}
               """.format(n=self.name, ro=self.role, le=self.level, cp=self.cp, s=self.strenght, a=self.agility, r=self.resistance, aa=self.armor, f=self.fpower, ma=self.mattack, ra=self.rattack, d=self.defense, l=self.life)
               print(sheet)
               
story = input('choose ur direction: left or right').little()
if story == 'left':
    print('you are in a forest')
    print('you see a cave')
    print('you go inside')
    print('you see a big dragon')
    print('you can fight or run')
    print('choose your action')
    action = input('fight or run')
    if action == 'fight':
        print('you fight the dragon')
        player_choice = input('Choose your weapon: sword, bow, spear\n')
        computer_choice = random.choice(['fire', 'tail', 'bite'])
        
if player_choice == 'sword' and computer_choice == 'fire':
    print('\nDragon tried to burn you with its fire ball. n/Your sword didnt help but you survived thanks your shiny armory. n/Do yoy wont to try again? y or n').little()
elif player_choice == 'sword' and computer_choice == 'tail':
    print('\nThe dragon tried to sweep you with its golden tail but you cut it off. n/The dragon is deadly injured and dies!)')
elif player_choice == 'sword' and computer_choice == 'bite':
    print('\nthe Dragon tried to bite you with its head and you. n/You felt over a stone and lost balance.n\Very unfortunate and you got teared into bloody pieces....')
elif player_choice == 'bowl' and computer_choice == 'fire':
    print('\nBefore your arrow could leave your bowl and hit his unpenetrated body, n\ the dragon roared and roasted you.n/You died in painful death.')
elif player_choice == 'bowl' and computer_choice == 'tail':
    print('\nThe dragon tried to sweep you with its massive tail but you managed move away and archer his nose. n/You managed to get away from the dragon and you are safe. Do you want to try again?').little()
elif player_choice == 'bowl' and computer_choice == 'bite':
    print(f'You send the arrow right through his eye into his brain.n\You are the hero of the local people. n\ Hura to hero' + name )
elif player_choice == 'spear' and computer_choice == 'fire':
    print('\n The dragon send some fire balls but you send back your spear. \n You hit him right in the eye n\ and the dragon dies in an agony. Well done!')
elif player_choice == 'spear' and computer_choice == 'tail':
    print("\nYour spear didnt help you much against dragon's tail.\n Its weight squashed.n\ You are dying looking n\ like a very bloody pancake")
elif player_choice == 'spear' and computer_choice == 'bite':
    print('\nHe tried to bite you only to get speared his tongue. It hurts and he stepped back. Do you want to attack again? y or n').little()

elif action == 'run':
        print('you run away')
        print('you saved your life coward, well done')
