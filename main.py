""" 0. Setup """
""" Import libraries """
import matplotlib.pyplot as plt
import matplotlib.ticker
import collections
import pandas as pd
import numpy as np
%matplotlib notebook

""" Initialize Blocksci """
import blocksci

# Create a Blockhain object
# parser_data_directory should be set to the data-directory which the blocksci_parser output
parser_data_directory = "/home/ubuntu/data/blocksci.conf"
chain = blocksci.Blockchain(parser_data_directory)


""" 1. Basic stats """
""" How many blocks are there in the blockchain? """

# The number of blocks is the length of the chain
%time num_blocks = len(chain)
print(num_blocks)


""" What is the size of all serialized blocks in the blockchain? """

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


""" How many transactions are there in the blockchain? """

# The number of transactions of a block is the length of the block
# and the sum of transactions of each block is the total number of transactions in the chain
%time total_num_transactions = sum([len(block) for block in chain])
print(total_num_transactions)


""" How many transactions are there in the first 100 blocks of the blockchain? And in the last 100 blocks? """

first100blocksTRX = sum([len(block) for block in chain[:100]])
print('There are', first100blocksTRX, 'transactions in the first 100 blocks of the blockchain. ')
last100blockTRX = sum([len(block) for block in chain[len(chain)-100:]])
print('There are', last100blockTRX, 'transactions in the last 100 blocks of the blockchain. ')


""" 2. Basic queries """
""" Which is the hash of the block with the most number of transactions? """

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


""" Which is the transaction in block 123456 with the most value in outputs? """

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


""" Which is the hash of the transaction whose output is spent by the input of the second transaction of block 200000? """

block = chain[199999] #we take 199 999 because of index 0
inputs=block.txes[1].inputs

print('The second transacion of block 200000 have', len(inputs), 'inputs.')
print('The hashes of the transactions whose outputs are the spent by these inputs are: ')

for input in inputs:
    spentTxs = [input.spent_tx]
    for spentTX in spentTxs:
        txhash = spentTX.hash
    print(txhash)


""" How many blocks do not have any fees at all? """

# Get blocks without fees
%time blocks_without_fees = sum([1 for _ in chain.blocks.where(lambda bl: bl.fee == 0)])
# Show how many did we find
print("There are {} blocks without paying any fees to the miner".format(blocks_without_fees))


""" ... and how many of them are older than height 125000? """

%time blocks_without_fees_prev125K = sum([1 for _ in chain[125000:].where(lambda bl: bl.fee == 0)])
# Show how many did we find
print("There are {} blocks without paying any fees to the miner".format(blocks_without_fees))


""" Is there any miner that did not collect his/her full reward (block reward + fees)? """

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


"""  Is there any miner that did not even collect the block reward? """

miners=0

for block in chain[:]:
    halvingYear = int(block.height/210000)
    if (block.revenue < ((getHalving(halvingYear))*100000000)):
        miners += 1

print('There are', miners, 'miners that did not collected the block reward. ')


""" 3. Plots with block and transaction data """

""" How many transactions per block are there? """

# Get number of transactions per block
%time num_transactions = [(block.height, len(block)) for block in chain]

# Plot number of transactions vs block height
fig, ax = plt.subplots()
df_num_tx = pd.DataFrame(num_transactions, columns=["Height", "Num. of tx"])
ax.plot(df_num_tx["Height"], df_num_tx["Num. of tx"])
plt.xlabel("Block height")
_ = plt.ylabel("Number of tx.")

# We can use heights_to_dates to convert block heights into dates
df_num_tx_dates = chain.heights_to_dates(df_num_tx)

# Plot number of transactions vs date
fig, ax = plt.subplots()
ax.plot(df_num_tx_dates.index, df_num_tx_dates["Num. of tx"])
plt.tight_layout()
plt.xlabel("Year")
_ = plt.ylabel("Number of tx.")


""" Which is the first block with more than one transaction? """

for (height, num_tx) in num_transactions:
    if num_tx > 1:
        break
        
print("The first block with more than one transaction is at height {}".format(height))


""" Are blocks currently full? """

# Get block sizes
%time block_sizes = [(block.height, block.size_bytes) for block in chain]

# Plot block size vs block height
fig, ax = plt.subplots()
df_num_tx = pd.DataFrame(block_sizes, columns=["Height", "Block size (bytes)"])
ax.plot(df_num_tx["Height"], df_num_tx["Block size (bytes)"])
plt.xlabel("Block height")
plt.ylabel("Block size")
# Show an orange line on 80% of max. block size, red line on 90%
max_block_size = 1024*1024
ax.plot([0, num_blocks], [0.8*max_block_size, 0.8*max_block_size], "orange")
ax.plot([0, num_blocks], [0.9*max_block_size, 0.9*max_block_size], 'r')


""" How does difficulty evolve? """

# Get block difficulties
%time block_bits = [(block.height, block.bits) for block in chain[100000:110000]]

# Plot block difficulties versus height
fig, ax = plt.subplots()
df_bits = pd.DataFrame(block_bits, columns=["Height", "Bits"])
plt.scatter(df_bits["Height"], df_bits["Bits"], s=1)
plt.tight_layout()
plt.xlabel("Block height")
plt.ylabel("Bits")


""" What kind of scripts are used in blocks? """

# Get address type per block
%time net_coins_per_block = chain.map_blocks(lambda block: block.net_address_type_value())

# net_address_type_value() returns a dictionary for each block:
net_coins_per_block[400000]

# Fill non existing entries with 0 and convert satoshis to btc
df = pd.DataFrame(net_coins_per_block).fillna(0).cumsum()/1e8
# Convert block heights to dates
df = chain.heights_to_dates(df)
# Convert column names (e.g. pubkeyhash -> 'Pay to pubkey hash')
df = df.rename(columns={t:str(t) for t in df.columns})
# Resample weekly and plot
ax = df.resample("W").mean().plot()
ax.set_ylim(ymin=0)


""" What is the hash of the first transaction with a multisignature output? """

for i, b in enumerate(net_coins_per_block):
    if blocksci.address_type.multisig in b.keys():
        print("Block at height {} has the first multisig output".format(i))
        # Let's find the transaction that has it
        for tx in chain[i]:
            for out in tx.outs:
                if out.address_type == blocksci.address_type.multisig:
                    print("Transaction {} has the first multisig ever".format(tx.hash))
        break


""" A note on resampling: how much fees were paid by block? """

# Get fees per block
%time fees_per_block = [(block.time, block.fee) for block in chain]

# Load data into dataframe
df_fees_block = pd.DataFrame(fees_per_block, columns=["Date", "Fees per block"])
# Set dataframe index as date
df_fees_block.index = df_fees_block["Date"]
del df_fees_block["Date"]

# Resample?
# df_fees_block = df_fees_block.resample("w").mean()
# df_fees_block = df_fees_block.resample("m").mean()
df_fees_block.plot()
plt.tight_layout()


""" Generate two plots showing the fees per byte payed by each transaction in block 200000 and block 450000. Which block is paying the highest fees per byte? """

#block 200 000
#X axis -> transaction
#Y axis -> fees/byte
####OR 
# X = bytes
# Y = fees 
# points with area equal to nTrx

trx_feesByte = [((trx.fee/trx.base_size),trx.index) for trx in chain[199999]]

fig, ax = plt.subplots()
dftrx_feesByte = pd.DataFrame(trx_feesByte, columns=["Fees Per Byte", "Trx Index"])
ax.plot( dftrx_feesByte["Trx Index"],dftrx_feesByte["Fees Per Byte"])
plt.ylabel("Fees Per Byte")
plt.xlabel("Trx Index")
sumFeesByte = 0
nTrx = chain[199999].tx_count
for feesxByte in trx_feesByte:
    sumFeesByte += feesxByte[0]
# Show an orange line on average fees/byte
#print((sumFeesByte/nTrx))
med = sumFeesByte/nTrx
#ax.plot([0, num_blocks], [0.8*max_block_size, 0.8*max_block_size], "orange")
plt.axhline(y=med, color='r', linestyle='-')
print(med)


trx_feesByte2 = [((trx.fee/trx.base_size),trx.index) for trx in chain[449999]]

fig2, ax2 = plt.subplots()
df_num_tx = pd.DataFrame(trx_feesByte2, columns=["Fees Per Byte", "Trx Index"])
ax2.plot( df_num_tx["Trx Index"],df_num_tx["Fees Per Byte"])
plt.ylabel("Fees Per Byte")
plt.xlabel("Trx Index")
sumFeesByte2 = 0
nTrx2 = chain[449999].tx_count
for feesxByte2 in trx_feesByte2:
    sumFeesByte2 += feesxByte2[0]
# Show an orange line on average fees/byte
#print((sumFeesByte/nTrx))
med2 = sumFeesByte2/nTrx2
#ax.plot([0, num_blocks], [0.8*max_block_size, 0.8*max_block_size], "orange")
plt.axhline(y=med2, color='r', linestyle='-')
print(med2)




