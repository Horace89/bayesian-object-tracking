#!/usr/bin/env python

import argparse, os
import numpy as np
import pickle
import random
import predict
import utils

# input and output directories
script_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(script_dir, '..', 'data/random')
output_dir = os.path.join(script_dir, '..', 'output')

parser = argparse.ArgumentParser("Generate object, options: ")

parser.add_argument('--frames', dest='frames', type=int, required=True,
    help='Number of input frames to process')
parser.add_argument('--predict', dest='predict_steps', type=int, default=2,
    help='Number of steps to predict at each frame')
parser.add_argument('--max_objects', dest='max_objects', type=int, default=15,
    help='Max number of objects in a frame')
parser.add_argument('--data', dest='data_dir', type=str, default=data_dir,
    help='Input data directory')
parser.add_argument('--output', dest='output_dir', type=str, default=output_dir,
    help='Output directory')
parser.add_argument('--log', dest='log_freq', type=int, default=1,
    help='Logging frequency')

# command line arguments
args = parser.parse_args()
if not os.path.exists(args.data_dir):
    print('Input data directory does not exist')
    exit(1)
if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)
assert(os.path.isdir(args.output_dir))

if __name__ == '__main__':
    kalman_basic = KalmanFilterBasic(args.data_dir, args.output_dir)
    klaman_basic.Run(50, 1)
