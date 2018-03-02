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


# another if with return

def cylinder_surface_area(radius, height, has_top_and_bottom):
    side_area = height * 6.28 * radius
    if has_top_and_bottom:
        top_area = 3.14 * radius ** 2
        return  2 * top_area + side_area
    else:
        return side_area
call = cylinder_surface_area(2,4,True)
print(call)


# another if fuction with trurth
def which_prize(points):
    prize = None
    if points <= 50:
        prize = "a wooden rabbit"
    elif 151 <= points <= 180:
        prize = "a wafer-thin mint"
    elif points >= 181:
        prize = "a penguin"

    if prize:
        return "Congratulations! You have won " + prize + "!"
    else:
        return "Oh dear, no prize this time."


call = which_prize(185)
print(call)


#most difficult till now
def convert_to_numeric(score):
    converted_score = float(score)
    return converted_score


def sum_of_middle_three(score1, score2, score3, score4, score5):
    max_score = max(score1, score2, score3, score4, score5)
    min_score = min(score1, score2, score3, score4, score5)
    sum = score1 + score2 + score3 + score4 + score5 - max_score - min_score
    return sum


def score_to_rating_string(av_score):
    if av_score < 1:
        rating = "Terrible"
    elif av_score < 2:
        rating = "Bad"
    elif av_score < 3:
        rating = "OK"
    elif av_score < 4:
        rating = "Good"
    else:  # Using else at the end, every possible case gets caught
        rating = "Excellent"
    return rating


def scores_to_rating(score1, score2, score3, score4, score5):
    max_score = max(score1, score2, score3, score4, score5)
    min_score = min(score1, score2, score3, score4, score5)
    av_of_three_middle = (score1 + score2 + score3 + score4 + score5 - max_score - min_score) / 3
    if av_of_three_middle < 1:
        rating = "Terrible"
    elif av_of_three_middle < 2:
        rating = "Bad"
    elif av_of_three_middle < 3:
        rating = "OK"
    elif av_of_three_middle < 4:
        rating = "Good"
    else:  # Using else at the end, every possible case gets caught
        rating = "Excellent"
        return av_of_three_middle


call = scores_to_rating(1, 3, 5, 7, 9)
print(call)



#slicing list
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates)

first_half = eclipse_dates[:5]
print(first_half)

second_half = eclipse_dates[5:]
print(second_half)

#largest three from a list
def top_three(input_list):
    sorted_list = sorted(input_list,reverse = True)
    answer = sorted_list[:3]
    return answer
call =top_three([2,3,4,5,6,7,8])
print(call)

#one more may to do upper
def top_three(input_list):
    return sorted(input_list, reverse=True)[:3]
call =top_three([2,3,4,5,6,7,8])
print(call)




