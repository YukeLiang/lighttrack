#!/usr/bin/env python
import argparse
import sys

# torchlight
import torchlight
from torchlight import import_class

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Processor collection')

    # region register processor yapf: disable
    processors = dict()
    processors['processor_siamese_gcn'] = import_class('gcn_utils.processor_siamese_gcn.SGCN_Processor')
    #processors['processor_siamese_gcn_triplet'] = import_class('utils.processor_siamese_gcn_triplet.SGCN_Processor')
    #processors['processor_siamese_naive'] = import_class('utils.processor_siamese_naive.Naive_Processor')
    #endregion yapf: enable

    # add sub-parser
    subparsers = parser.add_subparsers(dest='processor')
    for k, p in processors.items():
        subparsers.add_parser(k, parents=[p.get_parser()])

    # read arguments
    arg = parser.parse_args()
    print(arg)
    print(arg.processor)
    # start
    Processor = processors[arg.processor]
    p = Processor(sys.argv[2:])

    p.start()
