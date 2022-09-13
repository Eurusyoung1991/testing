from web3 import Web3, HTTPProvider
w3 = Web3(HTTPProvider('https://eth-sepolia.unifra.io/v1/a97287e0a21d41e6bea7a8f7d035ae99/'))
# put_filter = w3.eth.filter({'fromBlock': 1439200
# , 'toBlock': 1439300
# , 'address': '0x272c31fC25E4e609CbCC9E7a9e6171b4B39feAca'})
# print(w3.eth.get_filter_changes(put_filter.filter_id))
# from web3 import Web3, HTTPProvider
# w3 = Web3(HTTPProvider('https://eth-sepolia.unifra.io/v1/a97287e0a21d41e6bea7a8f7d035ae99/'))
# print (w3.eth.gas_price)
# from web3 import Web3, HTTPProvider
# w3 = Web3(HTTPProvider('https://eth-mainnet.unifra.io/v1/de06bac5217b49c3af79fd3aeb06a87b/'))
# put_filter = w3.eth.filter({'fromBlock': 1000000, 'toBlock': 1000100, 'address': '0x6C8f2A135f6ed072DE4503Bd7C4999a1a17F824B'})
# print(w3.eth.get_filter_changes(put_filter.filter_id))
newBlockFilterId = w3.eth.filter('latest')
id=newBlockFilterId.filter_id
print(w3.eth.get_filter_changes(id))