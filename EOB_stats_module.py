import math
def mean(vals):
    average = sum(vals) / len(vals)
    return average
def variance(vals):
    avg = mean(vals)
    total = 0
    for i in vals:
        x = (i - avg)**2
        total += x
    calc = total / len(vals)
    return calc

def standard_deviation(vals):
    avg = mean(vals)
    total = 0
    for i in vals:
        total += (i - avg)**2
    sd = math.sqrt(total/len(vals))
    return sd

def standard_error(vals):
    sd = standard_deviation(vals)
    se = sd/math.sqrt(len(vals))
    return se
def zscore(vals, new):
    avg = mean(vals)
    sd = standard_deviation(vals)
    try:
        z = (new - avg)/sd
    except ZeroDivisionError:
        z = 0
    return z

def summary(vals):
    pass
    avg = mean(vals)
    var = variance(vals)
    sd = standard_deviation(vals)
    se = standard_error(vals)
    return f'Summary Statistics:\nThe mean of your data is {avg:.2f}\nThe variance of your data is {var:.2f}\nThe standard deviation of your data is {sd:.2f}\nThe standard error of your data is {se:.2f} '

def menu():
    print("Menu:")
    print("(1) Calculate the mean")
    print("(2) Calculate the variance")
    print("(3) Calculate the standard deviation")
    print("(4) Calculate the standard error")
    print("(5) Calculate the Z-score for a new observation")
    print("(6) Print summary statistics")
    print("(q) Quit program\n")
    print("Please select one of the options above")