# SatyaTathya

## Project Description

- It is a single node blockchain made using python. It is mainly designed for our BBVS project (Election based voting system).
- Supports smart contract deployment and compiling.
- Compilation of contract is done using compiler API.
## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Technologies](#technologies)
- [Contributors](#contributors)

## Getting Started

- First clone the repo
```commandline
git clone https://github.com/NibanK/SatyaTathya.git
```
- Install all the requirements
```commandline
pip install -r requirements.txt
```

## Usage
- Add env as shown in env.example
- Run main.py (It will initialize the genesis block and run the server.)
- Now you can communicate using blockchian by:<br/>
1. **Check blockchain status:** Check status of the blockchain by making get request to <u>/status.</u>
2. **Mint block:** Add new block into blockchain. Post request to <u>/add_block</u>
```commandline
{
    "tx": "My first SatyaTathya transaction."
}
```
3. **Mint contract:** Mint contract into blockchain. Post request to <u>/add_contract</u>
```commandline
{ "tx":{
    "byte_code":"b'd\x00d\x01l\x00Z\x00d\x00d\x02l\x01m\x01Z\x01m\x02Z\x02\x01\x00d\x00d\x01l\x03Z\x03d\x00d\x01l\x04Z\x04d\x03d\x04\x84\x00Z\x05d9d\x06d\x07\x84\x01Z\x06d\x08d\t\x84\x00Z\x07d\nd\x0b\x84\x00Z\x08d\x0cd\r\x84\x00Z\td\x0ed\x0f\x84\x00Z\nd\x10d\x11\x84\x00Z\x0bd\x12d\x13\x84\x00Z\x0cd\x14d\x15\x84\x00Z\rd\x16d\x17\x84\x00Z\x0ed\x18d\x19\x84\x00Z\x0fd\x1ad\x1b\x84\x00Z\x10d\x1cd\x1d\x84\x00Z\x11e\x00\xa0\x12\xa1\x00d\x1ed\x1f\x84\x00\x83\x01Z\x13e\x13\xa0\x14\xa1\x00e\x00j\x15d d!d"d#\x8d\x03d$d%\x84\x00\x83\x01\x83\x01Z\x16d&d\'\x84\x00Z\x17e\x13\xa0\x14\xa1\x00d(d)\x84\x00\x83\x01Z\x18e\x13\xa0\x14\xa1\x00d*d+\x84\x00\x83\x01Z\x19e\x13\xa0\x14\xa1\x00d",
    "contract_data":""\"{    \\\"voters\\\": [        {            \\\"voter_id\\\": \\\"020\\\",            \\\"name\\\": \\\"nabin\\\",            \\\"voted_to\\\": [],            \\\"is_voted\\\": \\\"\\\"        },        {            \\\"voter_id\\\": \\\"020\\\",            \\\"name\\\": \\\"nabin\\\",            \\\"voted_to\\\": [],            \\\"is_voted\\\": \\\"\\\"        },        {            \\\"voter_id\\\": \\\"44\\\",            \\\"name\\\": \\\"sudeep\\\",            \\\"voted_to\\\": [                \\\"noone\\\",                \\\" everyone\\\",                \\\" someone\\\"            ],            \\\"is_voted\\\": \\\"true\\\"        }    ],    \\\"candidates\\\": [        {            \\\"candidate_id\\\": 12,            \\\"name\\\": \\\"sudeep\\\",            \\\"image_url\\\": \\\"jjl\\\",            \\\"post\\\": \\\"kkjkj\\\"        },        {            \\\"candidate_id\\\": 12,            \\\"name\\\": \\\"biamal\\\",            \\\"image_url\\\": \\\"jjl\\\",            \\\"post\\\": \\\"aabb\\\"        },        {            \\\"candidate_id\\\": \\\"12\\\",            \\\"name\\\": \\\"knkkn\\\",            \\\"image_url\\\": \\\"kj\\\",            \\\"post\\\": \\\"hjn\\\"        },        {            \\\"candidate_id\\\": \\\"12\\\",            \\\"name\\\": \\\"sdf\\\",            \\\"image_url\\\": \\\"dsf\\\",            \\\"post\\\": \\\"df\\\"        },        {            \\\"candidate_id\\\": \\\"12\\\",            \\\"name\\\": \\\"sdf\\\",            \\\"image_url\\\": \\\"sdf\\\",            \\\"post\\\": \\\"sdf\\\"        },        {            \\\"candidate_id\\\": \\\"12\\\",            \\\"name\\\": \\\"sdf\\\",            \\\"image_url\\\": \\\"sdf\\\",            \\\"post\\\": \\\"sdf\\\"        }    ],    \\\"results\\\": [],    \\\"election_name\\\": \\\"class_election\\\",    \\\"total_votes\\\": \\\" \\\",    \\\"voting_start_time\\\": \\\"2023-02-22 20:33:53.481790\\\",    \\\"voting_end_time\\\": \\\"2023-02-22 20:38:53.481790\\\"}\""
}
}
```
4. **Get all blocks:** Get all datas in blockchain. Get request to <u>/blocks</u>
5. **Get specific block:** Get particular block by blockhash. Get request to <u>/blocks/{block_hash}</u>
```commandline
   {
            "block_hash": "c0ed8908a5048b2ae48190056144efaad2a618704248a5f02b9617a8e0d5ac33",
            "prev_hash": "36b7762b4c2ed056bbd9b8987e7ca548aabb9c41d80ea189a84c7fb1d5e3c045",
            "timestamp": 1677660526.578213,
            "tx": {
                "metadata": "hi from postman"
            }
        }
```
## Technologies

- Python
- Redis cli (For storing node datas. And persisting datas on disk)
- Http server (For hosting port for request in blockchain)

## Contributors

- @NibanK (Blockchain, Redis db, server)
- @Sudeepkasichhwa (Hashing)
- @developer-prashant-999 (Wallet)


