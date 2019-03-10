import glob
import argparse
import pdb

def parse_args():
    parser = argparse.argumentParser()
    parser.add_argument("function", type=str, help="The only one is zeroPad")
    parser.add_argument("input_file", type=str, help="The directory or file to read from")
    parser.add_argument("output_file", type=str, help="The directory or file to write to")
    parser.add_argument("start_ind", type=int, help="The index to start at in the filename, can be negative")
    parser.add_argument("stop_ind", type=int, help="The index to stop at in the filename, can be negative (exclusive)")
    args = parser.parse_args()
    return args

def getAllInDir(dir_filename):
    if not dir_filename[-1] =="/":
        dir_filename+="/"
    all_files = glob.glob("{}*".format(dir_filename))
    return all_files


def zeroPad(input_file, output_file, start_ind, stop_ind, length=9):
    pdb.set_trace()
    files = getAllInDir(input_file)
    def to_num(string, start, stop):
        return int(string[start, stop])
    files = sorted(input_file, lambda x: to_num(x, start_ind, stop_ind))


if __name__ == "__main__":
    args = parse_args()
    if args.function == "zeroPad":
        zeroPad(args.input_file, args.output_file, args.start_ind, args.stop_ind)
    else:
        raise ValueError("Function was {} which isn't implement".format(args.function))

