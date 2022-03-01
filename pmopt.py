from simpgenalg.parameter_optimization import randomSearchOptimizer


def test_fxn(dct):
    sum = 0
    for item in dct.values():
        sum += item
    return sum

opt = randomSearchOptimizer(test_fxn)

opt.set_possible_parameters(x=list(range(1,10)), y=list(range(1,100)))

opt.run()

print(opt.to_df())
