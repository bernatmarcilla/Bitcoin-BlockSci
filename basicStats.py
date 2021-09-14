import matplotlib.pyplot as plt
import matplotlib.ticker
import collections
import pandas as pd
import numpy as np
%matplotlib notebook
from setup import parser_data_directory, chain

""" Initialize Blocksci """
import blocksci


# 1. Basic stats
### How many blocks are there in the blockchain? 

# The number of blocks is the length of the chain
%time num_blocks = len(chain)
print(num_blocks)


### What is the size of all serialized blocks in the blockchain? 

# The size of the chain is the sum of the sizes of the blocks 
%time blockchain_size = sum([block.size_bytes for block in chain])
print(blockchain_size)

# Using the fluent interface is faster:
# https://citp.github.io/BlockSci/fluent-interface.html
%time blockchain_size = sum([b for b in chain.blocks.select(lambda b: b.size_bytes)])
print(blockchain_size)

# Convert sizes in bytes to gigabytes for readability
def bytes_to_gb(s):
    return s/1024**3

print(bytes_to_gb(blockchain_size))


### How many transactions are there in the blockchain? 

# The number of transactions of a block is the length of the block
# and the sum of transactions of each block is the total number of transactions in the chain
%time total_num_transactions = sum([len(block) for block in chain])
print(total_num_transactions)


### How many transactions are there in the first 100 blocks of the blockchain? And in the last 100 blocks? 

first100blocksTRX = sum([len(block) for block in chain[:100]])
print('There are', first100blocksTRX, 'transactions in the first 100 blocks of the blockchain. ')
last100blockTRX = sum([len(block) for block in chain[len(chain)-100:]])
print('There are', last100blockTRX, 'transactions in the last 100 blocks of the blockchain. ')