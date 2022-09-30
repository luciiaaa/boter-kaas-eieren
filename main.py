from bke import MLAgent, is_winner, opponent, start



class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
   
 
my_agent = MyAgent()
start(player_o=my_agent)

def main ():
  print("Kies je spel")
  print()

  choice = input("""
                    A: Tegen een ander speler
                    B: Makkelijk spel
                    C: Moeilijk spel
                    D: Plot de grafiek
                    E: Train de tegenstander
                    
                    
                    Maak een keuze: """)
  if choice == "A" or choice == "a":
    AnderSpeler()
  elif choice == "B" or choice == "b":
    MakkelijkSpel()
  elif choice == "C" or choice == "c":
    MoelijkSpel()
  elif choice == "D" or choice == "d":
    Grafiek()
  elif choice == "E" or choice == "e":
    TrainOnly()
  else:
    print("kies tussen A, B, C of D")
    print("probeer opnieuw")
    main()

