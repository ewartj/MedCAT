# TODO: create a deid CDB from the deid terminology

from medcat.cdb import CDB
from medcat.cat import CAT
from medcat.utils.vocab import Vocab
from medcat.prepare_cdb import PrepareCDB
import os
import pandas as pd

vocab_dat =  # vocab path
cdb_csv =  # deid terminology path

deid_csv = pd.read_csv(cdb_csv)

vocab = Vocab()
vocab.load_dict(vocab_dat)
prep = PrepareCDB(vocab=vocab)
csv_paths = [cdb_csv]
cdb = prep.prepare_csvs(csv_paths)

cdb.save_dict('./medcat_models/snomed_cdb.dat')