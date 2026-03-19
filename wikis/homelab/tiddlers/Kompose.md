- https://github.com/kubernetes/kompose
  - 10.5k ⭐

一個用於將 `docker-compose.yaml` 轉換成 K8s YAML 的工具，但是不完全可靠，例如：該工具無法區分 `Deployment` 和 `StatefulSets` 所有 `service` 都會被轉換成 `Deployment`。

使用：

```shell
kompose convert -f compose.yaml
```