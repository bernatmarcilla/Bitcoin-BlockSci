import matplotlib.pyplot as plt
import matplotlib.ticker
import collections
import pandas as pd
import numpy as np
%matplotlib notebook
from setup import parser_data_directory, chain

""" Initialize Blocksci """
import blocksci


# 2. Basic queries 

### Which is the hash of the block with the most number of transactions? 
%time num_transactions = [len(block) for block in chain]
# Get max. number of transactions
m = max(num_transactions)
# Get height of the block with the most transactions
height = num_transactions.index(m)
# Retrieve hash
h = chain[height].hash

print("The block with the most number of transactions is at height {} and has {} transactions". format(height, m))
print("Block hash: {}".format(h))

# An alternative, using numpy:
height = np.argmax(num_transactions)
m = len(chain[height])
h = chain[height].hash

print("The block with the most number of transactions is at height {} and has {} transactions". format(height, m))
print("Block hash: {}".format(h))


### Which is the transaction in block 123456 with the most value in outputs? 
# Get block
block = chain[123456]
# Get output amounts per transaction
outvalue_per_tx = [tx.output_value for tx in block]  # Select max amount
max_value = max(outvalue_per_tx)
tx_index = outvalue_per_tx.index(max_value)
# Retrieve hash
tx = block.txes[tx_index].hash
print("The transaction with the most value in outputs (block 123456) is {} and has {} satoshis". format(tx_index, max_value))
print("Tx hash: {}".format(tx))

# Converts satoshi to btc
def satoshis_to_btc(v):
    return v/10**8

max_value_btc = satoshis_to_btc(max_value)
print("The transaction with the most value in outputs (block 123456) has {} btc". format(max_value_btc))


### Which is the hash of the transaction whose output is spent by the input of the second transaction of block 200000? 
block = chain[199999] #we take 199 999 because of index 0
inputs=block.txes[1].inputs

print('The second transacion of block 200000 have', len(inputs), 'inputs.')
print('The hashes of the transactions whose outputs are the spent by these inputs are: ')

for input in inputs:
    spentTxs = [input.spent_tx]
    for spentTX in spentTxs:
        txhash = spentTX.hash
    print(txhash)


### How many blocks do not have any fees at all? 
# Get blocks without fees
%time blocks_without_fees = sum([1 for _ in chain.blocks.where(lambda bl: bl.fee == 0)])
# Show how many did we find
print("There are {} blocks without paying any fees to the miner".format(blocks_without_fees))


### ... and how many of them are older than height 125000? 
%time blocks_without_fees_prev125K = sum([1 for _ in chain[125000:].where(lambda bl: bl.fee == 0)])
# Show how many did we find
print("There are {} blocks without paying any fees to the miner".format(blocks_without_fees))


### Is there any miner that did not collect his/her full reward (block reward + fees)? 
#first transaction has no inputs and 
#generates the number of bitdcoins depending 
#on height and the difference betrween inputs/outputs that are fees
#look inputs and outputs

miners=0

def getHalving(year):
    halving=50
    for i in range(year):
        halving/=2
    return halving


for block in chain[:]:
    halvingYear = int(block.height/210000)
    if ((block.fee + ((getHalving(halvingYear)))*100000000) != block.revenue):
        miners += 1

print('There are', miners, 'miners that did not collected the full reward. ')


###  Is there any miner that did not even collect the block reward?

miners=0

for block in chain[:]:
    halvingYear = int(block.height/210000)
    if (block.revenue < ((getHalving(halvingYear))*100000000)):
        miners += 1

print('There are', miners, 'miners that did not collected the block reward. ')