K3s 內建 OCI 從鏡像站拉取的功能，須在 `/etc/rancher/k3s/registries.yaml` 中設定，範例如下：

```yaml
mirrors:
  quay.io:
    endpoint:
      - http://harbor.arachne/v2/quay-proxy
  docker.io:
    endpoint:
      - http://harbor.arachne/v2/docker-hub-proxy
  ghcr.io:
    endpoint:
      - http://harbor.arachne/v2/ghcr-proxy
  mcr.microsoft.com:
    endpoint:
      - http://harbor.arachne/v2/microsoft-proxy
```