'''A useful little utility that reads PDF files and merges them in order.

Last modified 22 Feb 2025
'''

import argparse

import PyPDF2


def get_args() -> argparse.Namespace:
    '''Parse the command line arguments to this script.'''
    parser = argparse.ArgumentParser(
        description='Utility script for merging multiple PDF files together',
        epilog='The input PDFs will be concatenated in the order provided',
    )
    parser.add_argument(
        'pdfs',
        nargs='+',
        help='list of one or more PDF files to read in',
    )
    parser.add_argument(
        '-o', '--outfile',
        default='merged.pdf',
        help='name for the new merged PDF file (default %(default)s)',
    )
    return parser.parse_args()


def merge_pdfs(pdfs: list[str], outfile: str) -> None:
    '''Merge all PDF files in pdfs and save as outfile.'''
    merger = PyPDF2.PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)
    with open(outfile, 'wb') as new_file:
        merger.write(new_file)
    merger.close()


# Note: this block also runs if executed as a module with 'python -m'
if __name__ == '__main__':
    args = get_args()
    merge_pdfs(args.pdfs, args.outfile)
    print(f'Merged PDF saved as {args.outfile}')
