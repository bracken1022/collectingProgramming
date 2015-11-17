#A repositery about collecting programming

## There are some exammples for collecting programming

### 1. EucliDean Distanse

this algorithm is explained in the sim_distance function

### 2. Person

this algorithm is explained in the sim_person function

### 3. find the most similar person

you can find the most similar person by topMatch function

### 4. find the recommandations for someone

then you can give the recommandations for someone. getRecommandations gives u the way how to
caculate the highest socre by other pepole marked.

### 5. find the most similar movies

Before we have found the most similar movies by pearson algorithm. Now we only change the dictionary
to a collection of movies. transformPrefs()

### 6. building the comparison dataset

Now you can build an dataset about the similarly movies. caculateSimilarItems()

##Result

    I:programCollectiveintelligence bracken$ python collectingPreference.py
    --------------------------------------
    0.356789172325
    --------------------------------------
    0.66382999766
    --------------------------------------
    0.28369790411
    --------------------------------------
    [(0.7313089605150479, 'Mick LaSalle'), (0.6800985414106765, 'Lisa Rose'), (0.663829997660041, 'Claudia Puig')]
    --------------------------------------
    [(3.0, 'The Night Listener'), (3.0, 'Lady in the Water')]
    --------------------------------------
    [(0.5208690303986359, 'You, Me and Dupree'), (0.2727272727272727, 'Lady in the water'), (0.10410646628417279, 'Lady in the Water'), (0.07725424859373682, 'Snakes on a Plane'), (-0.13227030733885184, 'The Night Listener')]
    --------------------------------------
    [(4.0, 'Michael Phillips'), (3.0, 'Jack Matthews')]
    --------------------------------------
    {'Lady in the Water': [(0.5, 'Just My Luck'), (0.4721359549995794, 'You, Me and Dupree'), (0.4, 'The Night Listener'), (0.4, 'Snakes on a Plane'), (0.3090169943749474, 'Superman Returns'), (0, 'Lady in the water')], 'Snakes on a Plane': [(0.4721359549995794, 'Lady in the water'), (0.4, 'Lady in the Water'), (0.32037724101704074, 'The Night Listener'), (0.3090169943749474, 'Superman Returns'), (0.2553967929896867, 'Just My Luck'), (0.1886378647726465, 'You, Me and Dupree')], 'Just My Luck': [(0.5, 'Lady in the Water'), (0.38742588672279304, 'Lady in the water'), (0.32037724101704074, 'You, Me and Dupree'), (0.2989350844248255, 'The Night Listener'), (0.2553967929896867, 'Snakes on a Plane'), (0.20799159651347807, 'Superman Returns')], 'Superman Returns': [(0.3090169943749474, 'Snakes on a Plane'), (0.3090169943749474, 'Lady in the water'), (0.3090169943749474, 'Lady in the Water'), (0.252650308587072, 'The Night Listener'), (0.20799159651347807, 'Just My Luck'), (0.1918253663634734, 'You, Me and Dupree')], 'The Night Listener': [(0.6666666666666666, 'Lady in the water'), (0.4, 'Lady in the Water'), (0.32037724101704074, 'Snakes on a Plane'), (0.2989350844248255, 'Just My Luck'), (0.29429805508554946, 'You, Me and Dupree'), (0.252650308587072, 'Superman Returns')], 'Lady in the water': [(0.6666666666666666, 'You, Me and Dupree'), (0.6666666666666666, 'The Night Listener'), (0.4721359549995794, 'Snakes on a Plane'), (0.38742588672279304, 'Just My Luck'), (0.3090169943749474, 'Superman Returns'), (0, 'Lady in the Water')], 'You, Me and Dupree': [(0.6666666666666666, 'Lady in the water'), (0.4721359549995794, 'Lady in the Water'), (0.32037724101704074, 'Just My Luck'), (0.29429805508554946, 'The Night Listener'), (0.1918253663634734, 'Superman Returns'), (0.1886378647726465, 'Snakes on a Plane')]}



