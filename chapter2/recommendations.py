from math import sqrt

critics = {
    'Lisa Rose': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0,
    },
    'Gene Seymour': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 3.5,
    },
    'Michael Phillips': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener': 4.0,
    },
    'Claudia Puig': {
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'The Night Listener': 4.5,
        'Superman Returns': 4.0,
        'You, Me and Dupree': 2.5,
    },
    'Mick LaSalle': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0,
    },
    'Jack Matthews': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5,
    },
    'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0,
             'Superman Returns': 4.0},
}


def sim_distance(prefs, p1, p2):
    '''
    Using the Euclidean distance to get a distance-based
    similar score
    '''
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    # They have no rating in common
    if len(si) == 0:
        return 0

    sum_of_squares = sum(pow(prefs[p1][item] - prefs[p2][item], 2)
                         for item in prefs[p1] if item in prefs[p2])
    return 1 / (1 + sqrt(sum_of_squares))


def sim_pearson(prefs, p1, p2):
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    n = len(si)
    if n == 0:
        return 0

    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    sum1Square = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Square = sum([pow(prefs[p2][it], 2) for it in si])

    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    num1 = pSum - (sum1 * sum2 / n)
    num2 = sqrt((sum1Square - pow(sum1, 2) / n)
                * (sum2Square - pow(sum2, 2) / n))

    if num2 == 0:
        return 0

    return num1 / num2


if __name__ == '__main__':
    print(sim_distance(critics, 'Lisa Rose', 'Gene Seymour'))

    print(sim_pearson(critics, 'Lisa Rose', 'Gene Seymour'))
