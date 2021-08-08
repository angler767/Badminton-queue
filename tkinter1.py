from tkinter.constants import END
import tkinter.messagebox
import tkinter as tk


window = tk.Tk()
window.title("Grange Badminton GUI")
label = tk.Label(window, text = "Grange Badminton GUI").pack()
#title

myList = []
#list print function
def printList(list):
      print("")
      for player in list:
            print(player.name, player.skill)
            

    
entry = tk.Entry()
entry = tk.Entry(fg="black", width=50)
entry.pack()
name = entry.get()

entry1 = tk.Entry()
entry1 = tk.Entry(fg="black", width=50)
entry1.pack()
skill = entry1.get()

class Player:
    def __init__(self, name, skill):
        self.name= name
        self.skill = int(skill)
  
#addingplayertolist
def updateDisplay():
      text = ""
      for player in myList:
        text = text + (player.name + ", " + str(player.skill) + "\n")

      if len(myList) >= 1:
        text = text[:-1]
        queue_display.set(text)


def add_player(name, skill, list):
      new_Player = Player(name,skill)
      list.append(new_Player)
      for i in range(0, len(myList)-3, 4):
        if validateTeams(Team(myList[i],myList[i+1]), Team(myList[i+2], myList[i+3]))==False:
            tkinter.messagebox.showinfo(title=None, message="Match not compatible")
      updateDisplay()
      entry.delete(0,END)
      entry1.delete(0,END)



#inputbutton
button = tk.Button(window, text = "Input Name and Level", command = lambda:add_player(entry.get(), entry1.get(), myList))
button.pack()

#Team Structure

class Team:
    def __init__ (self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.skill_sum = player1.skill+player2.skill
        



def validateTeams(team1, team2):
   if team1.skill_sum > (team2.skill_sum + 2):
       return False
   elif team2.skill_sum> (team1.skill_sum + 2):
        return False
   else: 
        return True
#errors begin


def finish_game(list):
    if len(list)>4:
     del list[:4]
     for i in range(0, len(myList)-4, 4):
        if validateTeams(Team(myList[i],myList[i+1]), Team(myList[i+2], myList[i+3]))==False:
          tkinter.messagebox.showinfo(title=None, message="Match not compatible")
     updateDisplay()
  
     
#queue 

#finishgamebutton
button = tk.Button(window, text = "Game Finished", command = lambda:finish_game(myList))
button.pack()

queue_display = tk.StringVar()

label2 = tk.Label(window, textvariable = queue_display).pack()

window.mainloop()