#define the base class player
class Player:
    def play (self):
      print ("The player is playing cricket.")

#define the derived class batsman 
class batsman (player):
    def player (self):
      Print("The batsman is batting. ")

#define the derived class bowler 
class bowler (player):
     def play (self):
       print("The bowler is bowling.")

#create objects of batsman and bowler classes
batsman =batsman()
bowler= bowler ()

#call the play() class method for each object 
batsman . play()
bowler  .play ()