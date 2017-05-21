#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

    pred_diff = []

    for pred, net_worth in zip(predictions, net_worths):
        pred_diff.append(abs(net_worth - pred ))

    pred_diff.sort(reverse=True)

    min_pred = pred_diff[10]

    for pred, net_worth, age in zip(predictions, net_worths, ages):
        if abs(net_worth - pred) <= min_pred:
            diff = []
            diff.append(age)
            diff.append(net_worth)
            diff.append(abs(net_worth - pred))

            cleaned_data.append(diff)

    return cleaned_data

