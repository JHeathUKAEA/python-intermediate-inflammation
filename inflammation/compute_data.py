"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views


def analyse_data(data_holder):
    """Calculate the standard deviation by day between datasets

    Gets all the inflammation csvs within a directory, works out the mean
    inflammation value for each day across all datasets, then graphs the
    standard deviation of these means."""
    daily_standard_deviation =daily_std_dev_calc(data_holder.load_data())

    return(daily_standard_deviation)

class CSVDataSource:
    def __init__(self,data_dir):
        """initialise with the data directory you want to read"""
        self.data_dir=data_dir
        return
    def load_data(self):
        """Returns all suitable inflammation .csv files from a given directory"""
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation csv's found in path {self.data_dir}")
        data_files = map(models.load_csv, data_file_paths)
        return(data_files)

class JSONDataSource:
    def __init__(self,data_dir):
        """initialise with the data directory containig JSONs you want to read"""
        self.data_dir=data_dir
        return
    def load_data(self):
        """Returns all suitable inflammation .json files from a given directory"""
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'inflammation*.json'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation json's found in path {self.data_dir}")
        data_files = map(models.load_json, data_file_paths)
        return (data_files)


def load_data(data_dir):
    """Returns all suitable inflammation .csv files from a given directory"""
    data_file_paths = glob.glob(os.path.join(data_dir, 'inflammation*.csv'))
    if len(data_file_paths) == 0:
        raise ValueError(f"No inflammation csv's found in path {data_dir}")
    data_files = map(models.load_csv, data_file_paths)
    return (data_files)

def daily_std_dev_calc(data):
    """Function to take in patient daily inflammation data and calculate the daily
    inflammation standard deviation.
    """
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))
    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    return(daily_standard_deviation)

