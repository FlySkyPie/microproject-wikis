Volume 臨時容器是指在 K8s 中用來掛載 Volume 的臨時容器，可能用於資料遷移或是故障排除。

例如 `busybox` 可以提供一個用來 `kubectl exec` 的 Pod：

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: pinry
spec:
  replicas: 1
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      partition: 0
  template:
    spec:
      containers:
        - image: docker.io/library/busybox:latest
          name: busybox
          command:
            - sleep
            - "3600"
          volumeMounts:
            - mountPath: /data
              name: pinry-data
      restartPolicy: Always
      volumes:
        - name: pinry-data
          persistentVolumeClaim:
            claimName: pinry-data
```

又或是 `openssh-server` 可以提供 SSH 界面供其他工具遠端訪問：

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: openssh
spec:
  replicas: 1
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      partition: 0
  template:
    spec:
      containers:
        - image: docker.io/linuxserver/openssh-server:latest
          name: openssh
          env:
            - name: PASSWORD_ACCESS
              value: "true"
            - name: PGID
              value: "1000"
            - name: PUID
              value: "1000"
            - name: TZ
              value: Asia/Taipei
            - name: USER_PASSWORD
              value: password
          ports:
            - containerPort: 2222
              protocol: TCP
          volumeMounts:
            - mountPath: /config/data/media-data
              name: media-data

      restartPolicy: Always
      volumes:
        - name: media-data
          persistentVolumeClaim:
            claimName: media-data
```

