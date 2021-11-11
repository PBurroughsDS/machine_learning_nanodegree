##### Poisson Function ##### 
import numpy as np

def prob(input_tuple):
    # Splitting the tuple into the 4 input variables
    avg_h_scored,avg_a_scored, avg_h_conc, avg_a_conc = input_tuple
    
    # Averaging the home goals scored and the away goals conceded to give an expected number of goals the home / away team will score.
    home_goals = (avg_h_scored + avg_a_conc) / 2
    away_goals = (avg_a_scored + avg_h_conc) / 2
    
  
    
    # Return the probability of a game ending with 3+ goals
    return 1 - (
                # Game ends 0-0 
                (np.exp(-home_goals) * ( (home_goals**0) / 1)) * (np.exp(-away_goals) * ( (away_goals**0) / 1)) +
        
                # Game ends 1-0 
                (np.exp(-home_goals) * ( (home_goals**1) / 1)) * (np.exp(-away_goals) * ( (away_goals**0) / 1)) +
        
                # Game ends 0-1 
                (np.exp(-home_goals) * ( (home_goals**0) / 1)) * (np.exp(-away_goals) * ( (away_goals**1) / 1)) +
        
                # Game ends 1-1 
                (np.exp(-home_goals) * ( (home_goals**1) / 1)) * (np.exp(-away_goals) * ( (away_goals**1) / 1)) +
                
                # Game ends 2-0 
                (np.exp(-home_goals) * ( (home_goals**2) / 2)) * (np.exp(-away_goals) * ( (away_goals**0) / 1)) +
        
                # Game ends 0-2 
                (np.exp(-home_goals) * ( (home_goals**0) / 1)) * (np.exp(-away_goals) * ( (away_goals**2) / 2))
        
                )
    