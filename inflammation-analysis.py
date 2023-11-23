#!/usr/bin/env python3
"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""

import argparse
import os
import numpy as np

from inflammation import models, views
from inflammation.compute_data import analyse_data, JSONDataSource, CSVDataSource


def main(args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    InFiles = args.infiles
    if not isinstance(InFiles, list):
        in_files = [args.infiles]

    
    if args.full_data_analysis:
        _, extension = os.path.splitext(InFiles[0])
        if extension == '.json':
            data_source = JSONDataSource(os.path.dirname(InFiles[0]))
        elif extension == '.csv':
            data_source = CSVDataSource(os.path.dirname(InFiles[0]))
        else:
            raise ValueError(f'Unsupported file format: {extension}')
        data_result=analyse_data(data_source)
        graph_data = {
                        'standard deviation by day': data_result,
                    }
        views.visualize(graph_data)
        return



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic patient inflammation data management system')

    parser.add_argument(
        'infiles',
        nargs='+',
        help='Input CSV(s) containing inflammation series for each patient')

    parser.add_argument('--full-data-analysis', 
                        action='store_true', 
                        dest='full_data_analysis')

    args = parser.parse_args()
    

    main(args)
