from math import sqrt

critics = {
	'Lisa Rose': {
			'Lady in the water': 2.5, 
			'Snakes on a Plane': 3.5, 
			'Just My Luck': 3.0, 
			'Superman Returns': 3.5, 
			'You, Me and Dupree': 2.5, 
			'The Night Listener': 3.0
	      	     },
	'Gene Seymour': {
	      		'Lady in the water': 3.0, 
			'Snakes on a Plane': 3.5,
			'Just My Luck': 1.5,
			'Superman Returns': 5.0,
			'The Night Listener': 3.0, 
			'You, Me and Dupree': 3.5
	      		},
	'Michael Phillips': 
		 	    {
			    'Lady in the Water': 2.5, 
			    'Snakes on a Plane': 3.0, 
			    'Superman Returns': 3.5,
			    'The Night Listener': 4.0
		 	    },
	'Claudia Puig': 
		 	{
			'Snakes on a Plane': 3.5, 
			'Just My Luck': 3.0,
			'The Night Listener': 4.5,
			'Superman Returns': 4.0,
			'You, Me and Dupree': 2.5
			},
	'Mick LaSalle':
			{
			'Lady in the Water': 3.0, 
			'Snakes on a Plane': 4.0,
			'Just My Luck': 2.0,
			'Superman Returns': 3.0, 
			'The Night Listener': 3.0,
			'You, Me and Dupree': 2.0
			},
	'Jack Matthews': 
	      		 {
			 'Lady in the Water': 3.0, 
			 'Snakes on a Plane': 4.0,
			 'The Night Listener': 3.0,
			 'Superman Returns': 5.0,
			 'You, Me and Dupree': 3.5
			 },
	'Toby':
			{
			'Snakes on a Plane': 4.5,
			'You, Me and Dupree': 1.0,
			'Superman Returns': 4.0
			}
	}

def sim_distance(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    if len(si) == 0:
        return 0

    distance = [pow(prefs[person1][item] - prefs[person2][item], 2) for item in prefs[person1] if item in prefs[person2]]
    sum_of_squares = sum(distance)

    return 1 / (1 + sqrt(sum_of_squares))


def sim_pearson(prefs, person1, person2):
    person1_movie = prefs[person1]
    person2_movie = prefs[person2]

    si = {}
    for item in person1_movie:
        if item in person2_movie:
            si[item] = 1

    n = len(si)
    if 0 == n: return 0

    sum_p1_mul_p2 = sum([person1_movie[item] * person2_movie[item] for item in si])
    sumP1_mul_sumP2_div_n = sum([person1_movie[it] for it in si]) * sum([person2_movie[it] for it in si]) / n

    sumPowP1_minus_powSumP1DivN = sum([pow(person1_movie[it], 2) for it in si]) - pow(sum([person1_movie[it] for it in si]), 2)/n
    sumPowP2_minus_powSumP1DivN = sum([pow(person2_movie[it], 2) for it in si]) - pow(sum([person2_movie[it] for it in si]), 2)/n

    result = (sum_p1_mul_p2 - sumP1_mul_sumP2_div_n)/(1 + sqrt(sumPowP1_minus_powSumP1DivN * sumPowP2_minus_powSumP1DivN))

    return result


def topMatches(prefs, person, n = 5, similarity = sim_pearson):
    scores = [(similarity(prefs, person, other), other) for other in prefs if person != other]

    scores.sort()
    scores.reverse()
    return scores[0:n]
    

def getRecommendations(prefs, person, similarity = sim_pearson):
    totals = {}
    simSums = {}

    for other in prefs:
        if other == person: continue
        
        sim = similarity(prefs, person, other)
        if sim <= 0: continue
        
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item] == 0:
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                simSums.setdefault(item, 0)
                simSums[item] += sim

        rankings = [(total/simSums[item], item) for item, total in totals.items()]

        rankings.sort()
        rankings.reverse()
        return rankings

def transformPrefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})

            result[item][person] = prefs[person][item]

    return result

movies = transformPrefs(critics)

def printDivision():
    print '--------------------------------------'

if __name__ == '__main__':
    printDivision()
    print sim_distance(critics, 'Toby', 'Claudia Puig')
    printDivision()
    print sim_pearson(critics, 'Toby', 'Claudia Puig')
    printDivision()
    print sim_pearson(critics, 'Lisa Rose', 'Gene Seymour')
    printDivision()

    print topMatches(critics, 'Toby', 3)
    printDivision()

    print getRecommendations(critics, 'Toby')
    printDivision()

    print topMatches(movies, 'Superman Returns')
    printDivision()
    print getRecommendations(movies, 'Just My Luck')
    printDivision()


