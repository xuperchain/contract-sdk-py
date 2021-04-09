contract-sdk-py 是 [XuperChain](https://github.com/xuperchain/xuperchain) 的官方python 合约SDK，使用前请先在本地运行最新的XuperChain，并确保开启 native 合约支持

要求 python 版本为 python3.6+ 

1. 安装 python 合约 SDK

```bash

    git clone https://github.com/xuperchain/contract-sdk-py.git
    cd contract-sdk-py
    pip install -r requirements.txt
    python3 setup.py install 
```
        

2. 部署和调用第一个 python 合约

``` bash
    ./xchain-cli native deploy --account XC1111111111111111@xuper --fee 15587517 --runtime py  -a '{"creator":"xchain"}' --cname counter <PATH_TO_CONTRACT_SDK_PY>/example/counter/counter.py 
    ./xchain-cli native invoke --method Increase -a '{"key":"xchain"}' counter --fee 10
    ./xchain-cli native invoke --method  Get -a '{"key":"xchain"}' counter --fee 10
``` 
       
    
    
