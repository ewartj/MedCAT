from medcat.cdb import CDB
from medcat.cdb_maker import CDBMaker
from medcat.config import Config

# Specify cdb name and path to csvs
cdb_name = "cdb_name.dat"
csv_path_list = [" path to list of csvs here"]

# Create CDB
config = Config()
maker = CDBMaker(config)
cdb = maker.prepare_csvs(csv_path_list, full_build=True)
cdb.save(cdb_name)

# Load the newly created cdb:
cdb2 = CDB.load(cdb_name)
