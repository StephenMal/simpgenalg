from simpgenalg import geneticAlgorithm
#from dashtest import generationViewer


def num_matching(lst):
    return sum([abs(val-indx) for indx, val in enumerate(lst)])

vga_params = dict(function=num_matching,\
                  n_gens=200,\
                  num_genes=10, \
                  dtype=int, \
                  max=10, \
                  min=0, \
                  xov_op='uniform_crossover',\
                  mut_op='uniform_mutation',\
                  mut_rate=0.1,\
                  xov_rate=0.8,
                  maximize=False,
                  cmpr_map_dist=False)

bsga_params = dict(function=num_matching,\
                   representation='binary',\
                   n_gens=200,\
                   num_genes=10, \
                   gene_size=4, \
                   xov_op='twopt',\
                   mut_op='uniform_mutation',\
                   mut_rate=0.1,\
                   xov_rate=0.8,
                   maximize=False,
                   cmpr_map_dist=False)

var_pga_params = dict(function=num_matching,\
                  representation='proportional',\
                  map_fxn=3,\
                  min=0,
                  max=10,
                  n_noncoding_chars=1,\
                  lenmin=30,
                  lenmax=300,
                  n_gens=200,\
                  num_genes=10, \
                  xov_op='homologous_onept',\
                  mut_op='uniform_mutation',\
                  homology_threshold=0,\
                  window_size=5,\
                  mut_rate=0.1,\
                  xov_rate=0.8,
                  maximize=False,
                  cmpr_map_dist=False)


pga_params = dict(function=num_matching,\
                  representation='proportional',\
                  map_fxn=3,\
                  min=0,
                  max=10,
                  n_noncoding_chars=1,\
                  len=100,
                  n_gens=200,\
                  num_genes=10, \
                  xov_op='homologous_onept',\
                  mut_op='uniform_mutation',\
                  homology_threshold=0.5,\
                  window_size=5,\
                  mut_rate=0.1,\
                  xov_rate=0.8,
                  maximize=False,
                  cmpr_map_dist=False)


ga = geneticAlgorithm(**pga_params)

rslts = ga.run(n=1)

dataframes = rslts.to_df()
dataframes[0].to_csv('indvs.csv')
dataframes[1].to_csv('pops.csv')
#generationViewer(indvs='indvs.csv', stats='pops.csv', debug=True)
'''


from simpgenalg.representations.vector import vectorRepresentation

test1 = vectorRepresentation(lenLim=(10,10), dtype=int, min=0, max=1)
test2 = vectorRepresentation(lenLim=(10,10), dtype=int, min=0, max=1)

#test1.set_fit(10)
#test2.set_fit(200)
print(test1 < test2)
'''
