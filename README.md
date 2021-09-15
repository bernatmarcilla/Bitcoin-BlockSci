# Bitcoin-BlockSci


## 0. Setup 

#### Create a Blockhain object
#### parser_data_directory should be set to the data-directory which the blocksci_parser output


## 1. Basic stats

#### _How many blocks are there in the blockchain?_
CPU times: user 6 µs, sys: 7 µs, total: 13 µs

Wall time: 15 µs

653853

#### _What is the size of all serialized blocks in the blockchain?_ 
CPU times: user 658 ms, sys: 0 ns, total: 658 ms

Wall time: 657 ms

306258808815

#### _How many transactions are there in the blockchain?_
CPU times: user 783 ms, sys: 249 ms, total: 1.03 s

Wall time: 1.03 s

580137370

#### _How many transactions are there in the first 100 blocks of the blockchain? And in the last 100 blocks?_ 
There are 100 transactions in the first 100 blocks of the blockchain. 

There are 241676 transactions in the last 100 blocks of the blockchain. 


## 2. Basic queries 

#### _Which is the hash of the block with the most number of transactions?_ 
CPU times: user 833 ms, sys: 0 ns, total: 833 ms

Wall time: 832 ms

The block with the most number of transactions is at height 367853 and has 12239 transactions

Block hash: 00000000000000001080e6de32add416cd6cda29f35ec9bce694fea4b964c7be

#### _Which is the transaction in block 123456 with the most value in outputs?_ 
The transaction with the most value in outputs (block 123456) is 0 and has 5005000000 satoshis

Tx hash: 5b75086dafeede555fc8f9a810d8b10df57c46f9f176ccc3dd8d2fa20edd685b

#### _Which is the hash of the transaction whose output is spent by the input of the second transaction of block 200000?_ 
The second transacion of block 200000 have 2 inputs.

The hashes of the transactions whose outputs are the spent by these inputs are: 

7050b98c4215a00522ef90cfe13f45ddf2a4a199d348f377f56b0a47f5ee18e4

c410d173abbb7b0e4057d016cf67c100d3514e66d446b137cb021d6987982bbb

#### _Which is the hash of the transaction whose input spends the second output of the second transaction of block 200000?_
The hash of the transaction whose input spends the second output of the second transaction of block 200000 is:

1a40d11f1a8ac43c6e055549de0b323e4aa99dd7473b4aec85a7d4c044027807

#### _How many blocks do not have any fees at all_
CPU times: user 15.8 s, sys: 19.8 s, total: 35.6 s

Wall time: 3min 32s

There are 125287 blocks without paying any fees to the miner

#### _... and how many of them are older than height 125000_
CPU times: user 11.1 s, sys: 0 ns, total: 11.1 s

Wall time: 11.1 s

There are 125287 blocks without paying any fees to the miner

#### _Is there any miner that did not collect his/her full reward (block reward + fees)?_
There are 1123 miners that did not collected the full reward. 

#### _Is there any miner that did not even collect the block reward?_
There are 3 miners that did not collected the block reward.

## 3. Plots with block and transaction data 

#### _How many transactions per block are there?_
CPU times: user 1.08 s, sys: 35.6 ms, total: 1.11 s

Wall time: 1.11 s

![Transactions per Block](./plots/transactionsPerBlock.PNG "Transactions per Block")

#### _Which is the first block with more than one transaction?_
The first block with more than one transaction is at height 170

#### _Are blocks currently full?_
CPU times: user 1.16 s, sys: 14.2 ms, total: 1.17 s

Wall time: 1.17 s

![Full Blocks](./plots/fullBlocks.PNG "Full Blocks")

#### _How does difficulty evolve?_

![Difficulty Evolution](./plots/Difficulty.PNG "Difficulty Evolution")

#### _What kind of scripts are used in blocks?_

![Scripts used](./plots/scripts.PNG "Scripts used")

#### _What is the hash of the first transaction with a multisignature output?_
Block at height 164467 has the first multisig output

Transaction 60a20bd93aa49ab4b28d514ec10b06e1829ce6818ec06cd3aabd013ebcdc4bb1 has the first multisig ever

#### _A note on resampling: how much fees were paid by block?_

![Fees per Block](./plots/FeesPerBlock.PNG "Fees per Block")

#### _Generate two plots showing the fees per byte payed by each transaction in block 200000 and block 450000. Which block is paying the highest fees per byte?_

190.4945394306214

![Fees per Byte on block 200000](./plots/FeesPerByte200000.PNG "Fees per Byte on block 200000")

132.65440875227063

![Fees per Byte on block 450000](./plots/FeesPerByte450000.PNG "Fees per Byte on block 450000")
