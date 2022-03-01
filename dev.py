
from simpgenalg.representations.floating import floatingBinaryChromo, floatingRepresentation

tst = floatingRepresentation(num_genes=5,\
                             dtype=int,\
                             gene_size=4,\
                             len=20)
print('start', tst.start_tag)
print('start', tst.end_tag)
print('g_id_len', tst.gene_id_len)
print('gene_ids', tst.gene_ids)


print(tst.get_chromo().to_list())
print(tst.get_mapped())
