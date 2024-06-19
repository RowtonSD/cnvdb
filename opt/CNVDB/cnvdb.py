# XLS/CSV file importer utility for IBM i DB2 databases
# To be run on IBM i OS only
# Library specified must have automatic journaling enabled (via STRJRNLIB)
# python39 recommend
# requires IBM i Access ODBC driver (see https://ibmi-oss-docs.readthedocs.io/en/latest/odbc/installation.html)

import sqlalchemy as sa                 # This is the sqlalchemy-ibmi WIP variant provided by IBM (https://github.com/IBM/sqlalchemy-ibmi/)
import pandas as pd                     # install python39-pandas via open source package management                    
import pymysql                          # Hanldes MySQL like connections
from argparse import ArgumentParser
import sys

# command line arguement handler
def create_parser():
    parser = ArgumentParser(description="File Details")
    parser.add_argument("--source_file", help="XLS or XLSX file to convert")
    parser.add_argument("--source_type", help="Type of file to convert: XLS or CSV")
    parser.add_argument("--source_user", help="Source DB User, if required")
    parser.add_argument("--source_pass", help="Source DB Password, if required")
    parser.add_argument("--source_host", help="Host for SQL server, if not IBM i")
    parser.add_argument("--source_rdb", help="Source Relational DB, if IBM i")
    parser.add_argument("--source_database", help="Library (Database) Name")
    parser.add_argument("--source_table", help="File (Table) Name")
    parser.add_argument("--destination_file", help="XLS or XLSX file to convert")
    parser.add_argument("--destination_type", help="Type of file to convert: XLS or CSV")
    parser.add_argument("--destination_user", help="Destination DB User, if required")
    parser.add_argument("--destination_pass", help="Destination DB Password, if required")
    parser.add_argument("--destination_host", help="Host for SQL server, if not IBM i")
    parser.add_argument("--destination_rdb", help="Destination Relational DB, if IBM i")
    parser.add_argument("--destination_database", help="Library (Database) Name")
    parser.add_argument("--destination_table", help="File (Table) Name")
    return parser

# Import command line arguements
args = create_parser().parse_args()

# import source
if args.source_type == 'XLS':
    df = pd.read_excel(args.source_file)
elif args.source_type == 'CSV':
    df = pd.read_csv(args.source_file)
elif args.source_type == 'SQL' or args.source_type == 'DB2':
    if args.source_type == 'SQL':
        connection_string = "mysql+pymysql://" + args.source_user + ":" + args.source_pass + "@" + args.source_host + "/" + args.source_database
    elif args.source_type == 'DB2':
        connection_string = "ibmi://" + args.source_user + ":" + args.source_pass + "@localhost/" + args.source_rdb
    engine = sa.create_engine(connection_string)    
    cnxn = engine.connect()
    sourceDB = args.source_database
    sourceTBL = args.source_table
    df = pd.read_sql("SELECT * FROM " + sourceDB.lower() + "." + sourceTBL.lower(), cnxn)

# Export dataframe
if args.destination_type == 'CSV':
    df = pd.to_csv(args.destination_file)
elif args.destination_type == 'XLS':
    df.to_excel(args.destination_file)
elif args.destination_type == 'DB2' or args.destination_type == 'SQL':
    if args.destination_type == 'SQL':
        connection_string = "mysql+pymysql://" + args.destination_user + ":" + args.destination_pass + "@" + args.destination_host + "/" + args.destination_database
    elif args.destination_type == 'DB2':
        connection_string = "ibmi://" + args.destination_user + ":" + args.destination_pass + "@localhost/" + args.destination_rdb
    engine_dest = sa.create_engine(connection_string)    
    cnxn_dest = engine_dest.connect()
    exportDB = args.destination_database
    exportTable = args.destination_table
    df.to_sql(exportTable.lower(),schema=exportDB.lower(),con=cnxn_dest,if_exists='replace')
