from math import sqrt

critics = {
	'Lisa Rose': {
			'Lady in the water': 2.5, 
			'Snakes on a Plane': 3.5, 
			'Just My Luck': 3.0, 
			'Superman Returns': 3.5, 
			'You, Me and Dupree': 2.5, 
			'The Night Listerner': 3.0
	      	     },
	'Gene Seymour': {
	      		'Lady in the water': 3.0, 
			'Snakes on a Plane': 3.5,
			'Just My Luck': 1.5,
			'Superman Returns': 5.0,
			'The Night Lister': 3.0, 
			'You, Me and Dupree': 3.5
	      		},
	'Michael Phillips': 
		 	    {
			    'Lady in the Water': 2.5, 
			    'Snakes on a Plane': 3.0, 
			    'Superman Returns': 3.5,
			    'The Night Listerner': 4.0
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
			'The Night Listerner': 3.0,
			'You, Me and Dupree': 2.0
			},
	'Jack Matthews': 
	      		 {
			 'Lady in the Water': 3.0, 
			 'Snakes on a Plane': 4.0,
			 'The Night Listerner': 3.0,
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
    
    result = (sum_p1_mul_p2 - sumP1_mul_sumP2_div_n)/sqrt(sumPowP1_minus_powSumP1DivN * sumPowP2_minus_powSumP1DivN)

    return result


def topMatches(prefs, person, n = 5, similarity = sim_pearson):
    scores = [(similarity(prefs, person, other), other) for other in prefs if person != other]

    scores.sort()
    scores.reverse()
    return scores[0:n]
    

if __name__ == '__main__':
    print sim_distance(critics, 'Toby', 'Claudia Puig')
    print sim_pearson(critics, 'Toby', 'Claudia Puig')
    print sim_pearson(critics, 'Lisa Rose', 'Gene Seymour')

    print topMatches(critics, 'Toby', 3)

