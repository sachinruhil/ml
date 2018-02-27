def cylinder_volume(height,radius):
    pi = 3.14
    return height * pi * radius**2

volume = cylinder_volume(10,3)
print(volume)



# another
def readable_timedelta(days):
    """Print the number of weeks and days in a number of days."""
    #to get the number of weeks we use integer division
    weeks = days // 7
    #to get the number of days that remain we use %, the modulus operator
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)
answer = readable_timedelta(10)
print(answer)

#another
#if function
def which_prize(x):
    if x in range(0, 51):
        return ("Congratulations! you have won a wooden rabbit")
    elif x in range(51, 151):
        return ("Oh dear, no prize this time.")
    elif x in range(151, 181):
        return ("Congratulations! you have won a wafer-thin mint")
    elif x in range(181, 201):
        return ("Congratulations! you have won a penguin")


message = which_prize(55)
print(message)
