import math
import random

########################################
# SET THESE VARIABLES:
########################################

champ_desired_color = 'green' 
player_level = 6 

num_we_have_already = 3 # how many of the champ we already have
level_desired = 3 # what level we want the champ to be

contested = 5 # how many other players own of the champ
same_color_taken = 40 # how many of the same color have been taken. Ex: If we want a Zeri and someone has 3 Sejuanis, this would be 3 since both characters are purples.

rolls = 25 # how many rolls you have available


########################################
# The calculations. Don't touch anything below this line.
########################################

# odds of each color for each level
# Y axis is level, X axis is color
# These percentages come from: https://www.esportstales.com/teamfight-tactics/champion-pool-size-and-draw-chances
odds_by_level = [
    [1, 0, 0, 0, 0], # level 1
    [1, 0, 0, 0, 0], # level 2
    [.75, .25, 0, 0, 0], # level 3
    [.55, .30, .15, 0, 0], # level 4
    [.45, .33, .20, .02, 0], # level 5
    [.25, .40, .30, .05, 0], # level 6
    [.19, .30, .35, .15, .01], # level 7
    [.16, .20, .35, .25, .04], # level 8
    [.09, .15, .30, .30, .16] # level 9
]


# The number of characters in each color
color_size = [13, 13, 13, 12, 8]

# The number of each champ, based on color. For example, Cassiopeia is a white champ, so there are 29 of her in the pool.
cardinality_by_color = [29, 22, 18, 12, 10]


def get_odds_for_color(color, lvl):
    
    colors = ['white', 'green', 'blue', 'purple', 'gold']
    for i in range (0, 5):
        if color == colors[i]:
            return odds_by_level[lvl - 1][i], cardinality_by_color[i] * color_size[i], cardinality_by_color[i]
        

def main():

    # logistics
    trial_number = 10000
    trial_results = []
    hits_desired =  3 ** (level_desired - 1) - num_we_have_already
    
    refresh_count = 0
    hits = 0
    chance, total_pool, champ_range = get_odds_for_color(champ_desired_color, player_level)
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
        chance, total_pool, champ_range = get_odds_for_color(champ_desired_color, player_level)
        total_pool = total_pool - contested - num_we_have_already - same_color_taken
        champ_range = champ_range - num_we_have_already - contested
        


    ########################################
    # print results
    ########################################
    
    trial_results.sort(reverse=False)
    
    # if rolls is defined, give the percentage of trials that were less than or equal to the number of rolls
    if rolls != None:
        for i in range (0, trial_number):
            if trial_results[i] > rolls:
                print(f"Percent chance you got it within {rolls} rolls: " + str(100 * i / trial_number) + "%")
                break
    
    # the average 
    average = 0
    for i in range (0, trial_number):
        average = average + trial_results[i]
    average = average / trial_number
    print("Average: " + str(math.ceil(average)))
    
    # 10th percentile and 90th percentile
    print("90th percentile: " + str(trial_results[math.ceil(trial_number * .1)]))
    print("10th percentile: " + str(trial_results[math.ceil(trial_number * .9)]))


main()