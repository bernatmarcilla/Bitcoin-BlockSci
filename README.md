# Bitcoin-BlockSci


## 0. Setup 

#### Create a Blockhain object
#### parser_data_directory should be set to the data-directory which the blocksci_parser output


## 1. Basic stats

#### How many blocks are there in the blockchain? 
CPU times: user 6 µs, sys: 7 µs, total: 13 µs
Wall time: 15 µs
653853

#### What is the size of all serialized blocks in the blockchain? 
CPU times: user 658 ms, sys: 0 ns, total: 658 ms
Wall time: 657 ms
306258808815

#### How many transactions are there in the blockchain? 
CPU times: user 783 ms, sys: 249 ms, total: 1.03 s
Wall time: 1.03 s
580137370

#### How many transactions are there in the first 100 blocks of the blockchain? And in the last 100 blocks? 
There are 100 transactions in the first 100 blocks of the blockchain. 
There are 241676 transactions in the last 100 blocks of the blockchain. 


## 2. Basic queries 

#### Which is the hash of the block with the most number of transactions? 
CPU times: user 833 ms, sys: 0 ns, total: 833 ms
Wall time: 832 ms
The block with the most number of transactions is at height 367853 and has 12239 transactions
Block hash: 00000000000000001080e6de32add416cd6cda29f35ec9bce694fea4b964c7be

#### Which is the transaction in block 123456 with the most value in outputs? 
The transaction with the most value in outputs (block 123456) is 0 and has 5005000000 satoshis
Tx hash: 5b75086dafeede555fc8f9a810d8b10df57c46f9f176ccc3dd8d2fa20edd685b

#### Which is the hash of the transaction whose output is spent by the input of the second transaction of block 200000? 
The second transacion of block 200000 have 2 inputs.
The hashes of the transactions whose outputs are the spent by these inputs are: 
7050b98c4215a00522ef90cfe13f45ddf2a4a199d348f377f56b0a47f5ee18e4
c410d173abbb7b0e4057d016cf67c100d3514e66d446b137cb021d6987982bbb

### Which is the hash of the transaction whose input spends the second output of the second transaction of block 200000?
The hash of the transaction whose input spends the second output of the second transaction of block 200000 is:
1a40d11f1a8ac43c6e055549de0b323e4aa99dd7473b4aec85a7d4c044027807

#### How many blocks do not have any fees at all? 
CPU times: user 15.8 s, sys: 19.8 s, total: 35.6 s
Wall time: 3min 32s
There are 125287 blocks without paying any fees to the miner

#### ... and how many of them are older than height 125000? 
CPU times: user 11.1 s, sys: 0 ns, total: 11.1 s
Wall time: 11.1 s
There are 125287 blocks without paying any fees to the miner

#### ### Is there any miner that did not collect his/her full reward (block reward + fees)?
There are 1123 miners that did not collected the full reward. 

####  Is there any miner that did not even collect the block reward?
There are 3 miners that did not collected the block reward.

## 3. Plots with block and transaction data 

#### How many transactions per block are there? 
CPU times: user 1.08 s, sys: 35.6 ms, total: 1.11 s
Wall time: 1.11 s

#### Which is the first block with more than one transaction? 
The first block with more than one transaction is at height 170

#### Are blocks currently full? 
#### How does difficulty evolve? 
#### What kind of scripts are used in blocks? 
#### What is the hash of the first transaction with a multisignature output? 
Block at height 164467 has the first multisig output
Transaction 60a20bd93aa49ab4b28d514ec10b06e1829ce6818ec06cd3aabd013ebcdc4bb1 has the first multisig ever

#### A note on resampling: how much fees were paid by block?


#### Generate two plots showing the fees per byte payed by each transaction in block 200000 and block 450000. Which block is paying the highest fees per byte?
190.4945394306214

132.65440875227063
