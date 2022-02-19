from simpgenalg import geneticAlgorithm

def num_matching(lst):
    return sum([abs(val-indx) for indx, val in enumerate(lst)])

ga = geneticAlgorithm(function=num_matching,\
                      len=10, \
                      chr_max=10, \
                      chr_min=0, \
                      xov_op='onept',\
                      mut_op='uniform_mutation',\
                      mut_rate=0.1,\
                      xov_rate=0.8,
                      maximize=False,
                      cmpr_map_dist=False)

rslts = ga.run(n=2)

rslts.to_df().to_csv('results_test.csv')
