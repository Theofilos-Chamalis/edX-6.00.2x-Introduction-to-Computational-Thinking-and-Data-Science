def plotQuizzes():
#  Please only use the following Pylab functions:
# show, plot, title, xlabel, ylabel, legend, figure, and hist.

    scores = []
    scores = generateScores(10000)

    pylab.hist(scores, range = (55,90), bins = 7)
#    pylab.hist(range(2500), scores)
    pylab.title('Distribution of Scores')    
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    pylab.legend()
    #pylab.figure()
    pylab.show()