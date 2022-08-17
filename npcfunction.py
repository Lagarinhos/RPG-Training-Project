import random as ran

class Npc():

        ## NPC Generator ##

     def __init__(self, name, role, level):
         
         self.name = name
         self.role = role
         self.level = level     
         self.strenght = 0
         self.agility = 0
         self.armor = 0
         self.resistance = 0
         self.fpower = 0
                                                                
        ## Attribute Modifier by Role ##      
         
                     ## WARRIOR ##
         
         if self.role == "Warrior":                      
                 
            self.strenght = ran.randint(2,3)
            self.agility = ran.randint(1,2)
            self.armor = ran.randint(2,3)
            self.resistance = ran.randint(1,3)
            self.fpower = ran.randint(1,2)
                        
            if self.level > 1 and self.level <= 3:
                self.strenght += 1                           
            elif self.level > 3 and self.level <= 5:
                self.agility += 1          
                self.strenght += 1           
            elif self.level > 5 and self.level <= 7:
                self.armor += 1                     
                self.agility += 1          
                self.strenght += 1             
            elif self.level > 7 and self.level <= 9:
                self.resistance += 1
                self.armor += 1                     
                self.agility += 1          
                self.strenght += 1            
            elif self.level > 9 and self.level <= 12:
                self.fpower += 1
                self.resistance += 1
                self.armor += 1                     
                self.agility += 1          
                self.strenght += 1 

            self.defense = self.agility + self.armor
            self.mattack = self.strenght + self.agility
            self.rattack = self.agility + self.fpower
            self.life = int(self.armor + self.resistance) + 5               
            self.life += (self.level * 2)
            self.cp = int(self.level + self.strenght + self.agility + self.armor + self.resistance + self.fpower) * 10             
                                             
                ## ARCHER ##
                                                
         if self.role == "Archer":                      
                 
            self.strenght = ran.randint(1,2)
            self.agility = ran.randint(2,3)
            self.armor = ran.randint(1,3)
            self.resistance = ran.randint(1,2)
            self.fpower = ran.randint(2,3)
                        
            if self.level > 1 and self.level <= 3:
                self.agility += 1                           
            elif self.level > 3 and self.level <= 5:
                self.fpower += 1          
                self.agility += 1          
            elif self.level > 5 and self.level <= 7:
                self.resistance += 1                     
                self.fpower += 1          
                self.agility += 1                  
            elif self.level > 7 and self.level <= 9:
                self.armor += 1
                self.resistance += 1                     
                self.fpower += 1          
                self.agility += 1                
            elif self.level > 9 and self.level <= 12:
                self.strenght += 1
                self.armor += 1
                self.resistance += 1                     
                self.fpower += 1          
                self.agility += 1  
               
            self.defense = self.agility + self.armor
            self.mattack = self.strenght + self.agility
            self.rattack = self.agility + self.fpower
            self.life = int(self.armor + self.resistance) + 5               
            self.life += (self.level * 2)
            self.cp = int(self.level + self.strenght + self.agility + self.armor + self.resistance + self.fpower) * 10             
               
               ## NPC Sheet ##        
         
     def npcstatus(self):
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