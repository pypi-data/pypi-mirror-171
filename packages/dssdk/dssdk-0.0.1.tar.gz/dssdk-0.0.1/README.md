# Dataset python client

## 1、安装：

```
pip install dssdk

或指定版本

pip install dssdk==0.1.1
```

## 2、ApiClient

#### (1)、实例创建

```buildoutcfg
ApiClient(token: str, host=None):

token: token字符串
host: 接口服务地址，默认：api.diigii.com

```

##### 示例：

```
api = ApiClient('xxxx-xxxx-xxxx')
```