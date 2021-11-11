### A function to display whether or not the poisson model gave a TP , TN , FP , FN 

def prediction_outcome(input_tuple):
    poisson_prob_3plus, ft_total_goals = input_tuple
    
    if poisson_prob_3plus >= 0.5 and ft_total_goals > 2:
        return 'TP'
    elif poisson_prob_3plus < 0.5 and ft_total_goals <= 2:
        return 'TN'
    elif poisson_prob_3plus >= 0.5 and ft_total_goals <= 2:
        return 'FP'
    else:
        return 'FN'