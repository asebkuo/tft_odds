import math
import random


def get_odds_for_color(color, lvl):
    
    if (color == "blue"):
        if (lvl == 7):
            return .35, 234, 18
    
    if (color == 'purple'):
        if (lvl == 8):
            return .25, 168, 14

def main():

    # set these:
    color, player_level = 'purple', 8
    
    num_we_have_already = 3 # how many of the champ we already have
    hits_desired = 6 # how many of the char we want
    
    contested = 3 # how many other players own of the champ
    same_color_taken = 0 # how many of the same color have been taken. Ex: If we want a Zeri and someone has 3 Sejuanis, this would be 3 since both characters are purples.
    


    # logistics
    trial_number = 10000
    trial_results = []
    refresh_count = 0
    hits = 0
    chance, total_pool, champ_range = get_odds_for_color(color, player_level)
    total_pool = total_pool - contested - num_we_have_already - same_color_taken
    champ_range = champ_range - num_we_have_already - contested


    for i in range (0, trial_number):


        while hits < hits_desired:

            refresh_count = refresh_count + 1

            # slot is correct
            for i in range (0, 5):
                right_color = random.randrange(100)

                # champ is correct
                if (right_color < 100 * chance):
                    champ = random.randrange(total_pool - hits)
                    if champ < champ_range:
                        hits = hits + 1
                        champ_range = champ_range - 1

        trial_results.append(refresh_count)
        
        # reset counts
        refresh_count = 0
        hits = 0
        chance, total_pool, champ_range = get_odds_for_color(color, player_level)
        total_pool = total_pool - contested - num_we_have_already - same_color_taken
        champ_range = champ_range - num_we_have_already - contested
        

    # print the average 
    average = 0
    for i in range (0, trial_number):
        average = average + trial_results[i]
    average = average / trial_number
    print("Average: " + str(math.ceil(average)))
    #print(trial_results)
    
    # print 10th percentile and 90th percentile
    trial_results.sort()
    print("90th percentile: " + str(trial_results[math.ceil(trial_number * .1)]))
    print("10th percentile: " + str(trial_results[math.ceil(trial_number * .9)]))


main()