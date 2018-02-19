from operator import itemgetter
import math
from scipy import stats


def ci_lower_bound(positive_ratings, total_ratings, confidence):
    """
    Following http://www.evanmiller.org/how-not-to-sort-by-average-rating.html#changes
    :return: the lower bound of the confidence interval
    """
    n = total_ratings
    z = stats.norm.ppf(1 - (1 - confidence) / 2)
    p_hat = 1.0 * positive_ratings / n
    result = (
        (
            p_hat + z * z / (2 * n)
            - z * math.sqrt(
                (p_hat * (1 - p_hat) + z * z / (4 * n)) / n
            )
        ) / (1 + z * z / n)
    )
    return result


def ratingscore(arg1, arg2):
    length = arg1 + arg2
    score = '%.3f' % (arg1/length)
    return score


def rater(listoflists):
    someList = []
    for x in listoflists:
        newList = []
        for y in x:
            if y[:-1].isdigit() == False:
                newList.append(y)
            elif 'K' in y:
                y = float(y[:-1] + '0'*3)
                newList.append(y)
            elif 'M' in y:
                y = float(y[:-1] + '0'*6)
                newList.append(y)
            else:
                y = float(y)
                newList.append(y)
        someList.append(newList)
    ratedList = [[x[0], ci_lower_bound(x[1], x[1] + x[2], .95)] for x in someList]
    ratedList.sort(key=itemgetter(1), reverse=True)
    return ratedList[0:5]


testList = [['Higher We Go (Intro)', '11K', '352'], ['Migos - Supastars (Audio)', '84K', '2K'], ['Narcos', '31K', '870'], ['BBO (Bad Bitches Only)', '13K', '272'], ['Auto Pilot', '8K', '215'], ['Walk It Talk It', '43K', '1K'], ['Emoji A Chain', '8K', '207'], ['CC', '5K', '120'], ['Migos - Stir Fry (Audio)', '161K', '6K'], ['Too Much Jewelry', '8K', '158'], ['Gang Gang', '16K', '462'], [
    'White Sand', '9K', '186'], ['Crown the Kings', '4K', '86'], ['Flooded', '5K', '137'], ['Beast', '11K', '275'], ['Open It Up', '5K', '102'], ['Migos, Nicki Minaj, Cardi B - MotorSport (Official)', '1M', '90K'], ["Movin' Too Fast", '6K', '87'], ['Work Hard', '4K', '87'], ['Notice Me', '23K', '473'], ['Too Playa', '10K', '270'], ['Made Men', '6K', '124'], ['Top Down On Da NAWF', '4K', '95']]

print(rater(testList))
