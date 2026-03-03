![](#carla-architecture.webp)

CARLA 採用 Server-Client 架構，Server 端基於 [UE4](#UE4)，Client 端則是 [Python 函式庫](https://pypi.org/project/carla/)。

## Server

Server 端可以從 [GitHub Release](https://github.com/carla-simulator/carla/releases) 下載：

![](#download-carla.webp)

運行 Server 端：

```shell
./CarlaUE4.sh
```

## Client

安裝：

```shell
pip3 install carla
```

專案本身自帶了一些 Client [範例程式](https://github.com/carla-simulator/carla/tree/ue5-dev/PythonAPI/examples)，運行範例程式：

```shell
# Run generate Terminal A 
python PythonAPI/examples/generate_traffic.py  

# Terminal B
python PythonAPI/examples/manual_control.py  
```