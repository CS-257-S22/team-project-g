import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('County',type=str, nargs= 1,
                    help='The Name of the county to be looked up')
parser.add_argument('State',type=str, nargs= 1,
                    help='The Name of the state to be looked up')
parser.add_argument('StartDate',type=int, nargs=1,
                    help='The begining of the date range to look through')
parser.add_argument('EndDate',type=int, nargs=1,
                    help='THe end of the date range to look through')
parser.add_argument('-g','--graph',action='store_true',
    help= 'The flag to graph Data')

args = parser.parse_args()
print(args.graph)
