import sys
import argparse
import os

from parse_urls import parse_urls
from generate_excel_files import download_excel_files
from generate_json_files import generate_json_files


def get_ifsc_code(out_dir, file_type="EXCEL", verbose=False):
    if out_dir and  not os.path.exists(out_dir):
        raise os.OSError("Output directory %s does not exists"%(out_dir))
    else:
        file_urls = parse_urls()
        download_excel_files(file_urls, out_dir, verbose)
        if file_type == 'JSON':
            generate_json_files(file_urls, out_dir, verbose)
    print "Done"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filetype", default="EXCEL", help="Output file type e.g. EXCEL/JSON")
    parser.add_argument("outdir", help="Output directory")
    parser.add_argument("-v", "--verbosity", help="Increase output verbosity",
                        action="store_true")
    args = parser.parse_args()
    file_type = args.filetype
    out_dir = args.outdir

    get_ifsc_code(out_dir, file_type, args.verbosity)

