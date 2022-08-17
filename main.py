import playerfunction as pfunc
import npcfunction as npcfunc

class Main:

             print("Welcome to LagaWorld")
             print("Let's create your Avatar, shall we?")
             player1 = pfunc.Char("","")
             pfunc.Char.playermenu(player1)
            
            
            ### TEST AREA ###
            
             human1 = npcfunc.Npc("Jack","Warrior",1)
             human2 = npcfunc.Npc("Garry","Warrior",5)
             human3 = npcfunc.Npc("John","Archer",7)
             human4 = npcfunc.Npc("Christy","Archer",3)
             print("")
             print("")
             npcfunc.Npc.npcstatus(human1)
             npcfunc.Npc.npcstatus(human2)
             npcfunc.Npc.npcstatus(human3)
             npcfunc.Npc.npcstatus(human4)
             print("")
             print("")
            
