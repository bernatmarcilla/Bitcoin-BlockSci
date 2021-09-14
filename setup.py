# 0. Setup 
# Import libraries 
import matplotlib.pyplot as plt
import matplotlib.ticker
import collections
import pandas as pd
import numpy as np
%matplotlib notebook

""" Initialize Blocksci """
import blocksci

### Create a Blockhain object
### parser_data_directory should be set to the data-directory which the blocksci_parser output
parser_data_directory = "/home/ubuntu/data/blocksci.conf"
chain = blocksci.Blockchain(parser_data_directory)




