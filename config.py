import os

# Set verbosity level: 0: progress, 1: progress+status, 2: progress+status+state, 3: progress+status+state+stdout+stderr
verbosity = 2
stdev = 0.22

# Paths
path_to_leela = './bots/leela/leela_0110_linux_x64'
checkpoint_dir = './.leela_checkpoints'
skip_checkpoints = False

# Logs, set None if you don't need them (!)
path_to_log = './leela.log'

# Set time for main line and variations analysis
analyze_time = 10
variations_time = 10

# Set desired threshold for displaying analysis and exploring suggested variations
analyze_threshold = 0.05
variations_threshold = 0.05

# Set variations depth and width
nodes_per_variation = 7
nodes_threshold = 0.15  # Default is 0.15 (experimental)
num_to_show = 10

# Set range of moves to analyze
analyze_start = 0
analyze_end = float('inf')

# For leela setting, review its docs
leela_settings = ['--gtp', '--noponder']
