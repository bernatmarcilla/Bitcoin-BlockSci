# Bitcoin-BlockSci


# 0. Setup 

### Create a Blockhain object
### parser_data_directory should be set to the data-directory which the blocksci_parser output


# 1. Basic stats

### How many blocks are there in the blockchain? 
### What is the size of all serialized blocks in the blockchain? 
### How many transactions are there in the blockchain? 
### How many transactions are there in the first 100 blocks of the blockchain? And in the last 100 blocks? 


# 2. Basic queries 

### Which is the hash of the block with the most number of transactions? 
### Which is the transaction in block 123456 with the most value in outputs? 
### Which is the hash of the transaction whose output is spent by the input of the second transaction of block 200000? 
### How many blocks do not have any fees at all? 
### ... and how many of them are older than height 125000? 
###  Is there any miner that did not even collect the block reward?


# 3. Plots with block and transaction data 

### How many transactions per block are there? 
### Which is the first block with more than one transaction? 
### Are blocks currently full? 
### How does difficulty evolve? 
### What kind of scripts are used in blocks? 
### What is the hash of the first transaction with a multisignature output? 
### A note on resampling: how much fees were paid by block?
### Generate two plots showing the fees per byte payed by each transaction in block 200000 and block 450000. Which block is paying the highest fees per byte?
