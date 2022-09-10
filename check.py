import requests
import json
import threading
from html import unescape
import time
from filecmp import cmp
def json_config_write_file(url, filepath, headers, payloads):
    status = 0
    try:
        resp_status = requests.request(
            "GET", url, headers=headers, data=payloads)
        status = resp_status.status_code
        resp_status_dict = json.loads(resp_status.text)
    except requests.exceptions.RequestException as e:
        print(e)
        return "failed,network error"
    if status == 200:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(
                unescape(str(json.dumps(resp_status_dict, indent=4, separators=(',', ':')))))
        return filepath
    else:
        return "network error"


if __name__ == '__main__':
    dict = {
        "getNFTs": {"url": "https://cfx-core.unifra.io/v1/cf455a9802364d88b8f87b5273d9ddbb/getNFTs?owner=0x19241022053a3e2236c48E86B62957C8654B65a1"},
        "getNFTMetadata": {"url": "https://cfx-core.unifra.io/v1/cf455a9802364d88b8f87b5273d9ddbb/getNFTMetadata?contractAddress=cfx:acff8dvjv6pys2ws19dhx753h1h00sum6yhu3m188h&tokenId=0x2713"},
        "getContractMetadata": {"url": "https://cfx-core.unifra.io/v1/cf455a9802364d88b8f87b5273d9ddbb/getContractMetadata?contractAddress=cfx:acff8dvjv6pys2ws19dhx753h1h00sum6yhu3m188h"},
        "getNFTsForCollection": {"url": "https://cfx-core.unifra.io/v1/cf455a9802364d88b8f87b5273d9ddbb/getNFTsForCollection?contractAddress=cfx:acff8dvjv6pys2ws19dhx753h1h00sum6yhu3m188h"},
        "getOwnersForToken": {"url": "https://cfx-core.unifra.io/v1/cf455a9802364d88b8f87b5273d9ddbb/getOwnersForToken?contractAddress=cfx:acff8dvjv6pys2ws19dhx753h1h00sum6yhu3m188h&tokenId=1021"},
        "getOwnersForCollection": {"url": "https://cfx-core.unifra.io/v1/cf455a9802364d88b8f87b5273d9ddbb/getOwnersForCollection?contractAddress=cfx:acff8dvjv6pys2ws19dhx753h1h00sum6yhu3m188h"}
    }
    file_path = "test.txt"
    headers = {'Content-Type': 'application/json'}
    payloads = {}
    flag = 0
    def work():
        for key, value in dict.items():
            title = key
            file_path1 = "test_"+title+"_1_"+".txt"
            file_path2 = "test_"+title+"_2_"+".txt"
            url = value.get("url")
            print(url)
            threads=[threading.Thread(target = json_config_write_file,args=(url,file_path1,headers,payloads)),
                threading.Thread(target = json_config_write_file,args=(url,file_path2,headers,payloads))]
            for i in threads:
                i.start()
                print(time.time())
            try :
                statu = cmp(file_path1,file_path2)
                if statu : print (title+"高度一致")
                else : 
                    print(title + "不一致") 
                    flag+=1
            except IOError:
                print("ioerror")
            print("-------------------------------------------")
    for i in range(30):
        work()
    print(flag)    
