import requests
from web3 import Web3, HTTPProvider
w3 = Web3(HTTPProvider('https://eth-sepolia.unifra.io/v1/a97287e0a21d41e6bea7a8f7d035ae99/'))

try:
  signed_txn = w3.eth.account.sign_transaction(dict(
    nonce=w3.eth.get_transaction_count("0x015AE442e6997B397B497d11Bb03404d18cE8407"),
    maxFeePerGas=3000000000,
    maxPriorityFeePerGas=2000000000,
    gas=100000,
    to='0x03710d048ED9FEb4eD09431a14C3BeF538281F36',
    value=50000,
    data=b'',
    type=2,
    chainId=11155111,
  ),
  "761514c1508eeb95db6fc3f37ff63910598ba85136e25a2e4eb54f9c0b9cdaab",
)
  txHash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
  print(w3.toHex(txHash))
except requests.exceptions.HTTPError as e:
  print("________________________")
  print(e)
    # return "failed,network error"

    # try:
    #     resp_status = requests.request(
    #         "GET", url, headers=headers, data=payloads)
    #     status = resp_status.status_code
    #     resp_status_dict = json.loads(resp_status.text)
    # except requests.exceptions.RequestException as e:
    #     print(e)
    #     return "failed,network error"