from web3 import Web3, HTTPProvider
w3 = Web3(HTTPProvider('https://eth-sepolia.unifra.io/v1/a97287e0a21d41e6bea7a8f7d035ae99/'))
put_filter = w3.eth.filter({'fromBlock': 1439200
, 'toBlock': 1439300
, 'address': '0x272c31fC25E4e609CbCC9E7a9e6171b4B39feAca'})
print(put_filter.filter_id)
print(w3.eth.get_filter_logs(put_filter.filter_id))

# from web3 import Web3, HTTPProvider
# w3 = Web3(HTTPProvider('https://eth-sepolia.unifra.io/v1/a97287e0a21d41e6bea7a8f7d035ae99/'))
# put_filter = w3.eth.filter({'fromBlock': 1439200
# , 'toBlock': 1439300
# , 'address': '0x272c31fC25E4e609CbCC9E7a9e6171b4B39feAca'})
# print(w3.eth.get_filter_changes(put_filter.filter_id))