from web3 import Web3, HTTPProvider
w3 = Web3(HTTPProvider('https://eth-sepolia.unifra.io/v1/a97287e0a21d41e6bea7a8f7d035ae99/'))
newBlockFilterId = w3.eth.filter('latest')
print(newBlockFilterId.filter_id)