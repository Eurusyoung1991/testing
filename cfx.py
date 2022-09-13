from conflux_web3 import Web3, HTTPProvider

w3 = Web3(Web3.HTTPProvider("https://test.confluxrpc.com"))
print (w3.cfx.epoch_number)