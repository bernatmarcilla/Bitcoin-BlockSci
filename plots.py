import matplotlib.pyplot as plt
import matplotlib.ticker
import collections
import pandas as pd
import numpy as np
%matplotlib notebook
from setup import parser_data_directory, chain

""" Initialize Blocksci """
import blocksci


# 3. Plots with block and transaction data 

### How many transactions per block are there? 

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


### Which is the first block with more than one transaction? 

for (height, num_tx) in num_transactions:
    if num_tx > 1:
        break
        
print("The first block with more than one transaction is at height {}".format(height))


### Are blocks currently full? 

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


### How does difficulty evolve? 

# Get block difficulties
%time block_bits = [(block.height, block.bits) for block in chain[100000:110000]]

# Plot block difficulties versus height
fig, ax = plt.subplots()
df_bits = pd.DataFrame(block_bits, columns=["Height", "Bits"])
plt.scatter(df_bits["Height"], df_bits["Bits"], s=1)
plt.tight_layout()
plt.xlabel("Block height")
plt.ylabel("Bits")


### What kind of scripts are used in blocks? 

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


### What is the hash of the first transaction with a multisignature output? 

for i, b in enumerate(net_coins_per_block):
    if blocksci.address_type.multisig in b.keys():
        print("Block at height {} has the first multisig output".format(i))
        # Let's find the transaction that has it
        for tx in chain[i]:
            for out in tx.outs:
                if out.address_type == blocksci.address_type.multisig:
                    print("Transaction {} has the first multisig ever".format(tx.hash))
        break


### A note on resampling: how much fees were paid by block?

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


### Generate two plots showing the fees per byte payed by each transaction in block 200000 and block 450000. Which block is paying the highest fees per byte? 

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
