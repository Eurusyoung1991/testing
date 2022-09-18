# Installation Instructions: https://web3py.readthedocs.io/en/latest/quickstart.html#installation

from web3 import Web3, HTTPProvider

#Replace with your Alchemy API key:
apiKey = "demo"

# Initialize a Web3.py instance
web3 = Web3(Web3.HTTPProvider('https://eth-mainnet.unifra.io/v1/de06bac5217b49c3af79fd3aeb06a87b'))

# Query the blockchain (replace example parameters)
logs = web3.eth.get_logs({
  'fromBlock': 1000000, 
  'toBlock': 1000100, 
  'address': '0x86Bb8D2bc9FeE4Dc6bB47f71bB4353fd88Ac8f57'
  }) 

# Print the output to console
print(logs)
