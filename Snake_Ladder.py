import random

class Board_entity:                     #Parent Class
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_start(self):         #return snake head or ladder top
        return self.start
    
    def get_end(self):        #return snake tail or ladder bottom
        return self.end

class snake(Board_entity):                #Inherit
    def bite(self, player_position):
        if player_position == self.start:
            print(f"""Bitten by a snake at " {self.start} ", New position " {self.end} ". """)
            return self.end
        return player_position
 
class ladder(Board_entity):             #Inherit
    def climb(self, player_position):
        if player_position == self.end:
            print(f"""Climbed a ladder at " {self.end} ", New position " {self.start} ".""")
            return self.start
        return player_position

class MainGame:
    def __init__(self, players):
        self.players = players
        self.winner = None         #initially no winner
        self.board = 100
        self.position = {}
        self.snakes, self.ladders = self.snake_ladder_position()

        for i in range(1, self.players+1):
            self.position[f"Player {i}"] = 1

    def snake_ladder_position(self):

        snakes = {}     #to store snake no as key and its head, tail object pair as value
        ladders = {}    #to store ladder no as ket and its top, bottom object pair as value

        used_pos = []  #used position by snakes and ladder to ensure they wont get used again

        for i in range(1, 7):
            while True:
                head_tail_top_bottom = list({random.randint(15, 98), random.randint(5, 85), random.randint(15, 98), random.randint(5, 85)})   #generate 4 unique no within given range

                if len(head_tail_top_bottom) == 4:   #checks if no repeation in head_tail_top_bottm
                    if head_tail_top_bottom[0] - head_tail_top_bottom[1] > 10 and head_tail_top_bottom[2] - head_tail_top_bottom[3] > 10:   #checks diff of minimun 10 block
                        if head_tail_top_bottom[2] > 90 and head_tail_top_bottom[3] < 40:  #make sure ladder less than 40 bottom wont go more than 90 block
                            continue
                        
                        #check that values are not used repeatadly and than added in used_pos to check again in next iteration
                        if head_tail_top_bottom[0] not in used_pos and head_tail_top_bottom[1] not in used_pos and head_tail_top_bottom[2] not in used_pos and head_tail_top_bottom[3] not in used_pos: 
                            used_pos.extend(head_tail_top_bottom)
                            break

            snakes[f"Snake {i}"] = snake(head_tail_top_bottom[0], head_tail_top_bottom[1])

            ladders[f"ladder {i}"] = ladder(head_tail_top_bottom[2], head_tail_top_bottom[3])

        return snakes, ladders
    
    def show_snake_ladder_positions(self):        #Display snake and ladder positions
        print("\nSnakes:")
        for name, position in self.snakes.items():
            print(f"{name}: Head at {position.get_start()}, Tail at {position.get_end()}")
    
        print("\nLadders:")
        for name, position in self.ladders.items():
            print(f"{name}: Bottom at {position.get_end()}, Top at {position.get_start()}")

    def player_move(self, player):

        current_position = self.position[player]

        roll_dice = random.randint(1, 6)
        print(f" ==> {roll_dice}")

        if roll_dice <= (self.board - current_position):
            current_position += roll_dice

        print(f"""{player}'s New position is " {current_position} ".""")

        for snake_position in self.snakes.values():
            current_position = snake_position.bite(current_position)

        for ladder_position in self.ladders.values():
            current_position = ladder_position.climb(current_position)

        if current_position == self.board:
            self.winner = player
            print(f"\nWinner of the game is {player}. Congratulations.")

        self.position[player] = current_position

    def play(self):
        while not self.winner:
            for player in self.position:
                input(f"""\n{player}'s turn, position " {self.position[player]} ". Press Enter to roll dice""")
                self.player_move(player)
                if self.winner:
                    break
            
def run_game():
    print("Welcome to Snake & Ladder Game!")
    while True:
        try:
            player_no = int(input("\nEnter No. of Players [2:4] : "))
            if player_no < 2:
                print("\nMinimum 2 players required to start the game.")
            elif player_no > 4:
                print("\nMaximun 4 players allowed to play only.")
            else:
                start = MainGame(player_no)
                start.show_snake_ladder_positions()
                start.play()
                break
        except ValueError:
            print("\nPlease enter a valid number.")

if __name__ == "__main__":
    run_game()