# spring-boot-client-python
> 仅学习使用

### 启动应用
```
git clone git@github.com:suxiaobai/spring-boot-client-python.git
cd spring-boot-client-python
pip install -r requires.txt
python spring-boot-client.py
```

### 获取配置
```
curl  http://127.0.0.1:5000/env
```

### 修改配置 spring-boot-client.py
```
EnableAutoConfiguration(app, name="Kefu", \
    profile="WebhookCallback-47.3", label="master", \
    config_server="http://kefu-app1:18888")
```

EnableAutoConfiguration 接收 4个参数

|参数序号 | 参数名称 | 备注 | 
| ------ | ------ | ---- |
| 1 | app | flask app |
| 2 | name | 对应 spring clond 中的 SPRING_CLOUD_CONFIG_NAME | 
| 3 | profile | 对应 spring clond 中的 SPRING_CLOUD_CONFIG_PROFILE | 
| 4 | label | 对应 spring clond 中的 SPRING_CLOUD_CONFIG_LABEL | 
| 5 | config_server | 对应 spring clond 中的 SPRING_CLOUD_CONFIG_URI | 

从 Spring Cloud ConfigServer 获取配置的完整 URL 路径为:
```
SPRING_CLOUD_CONFIG_URI/SPRING_CLOUD_CONFIG_NAME/SPRING_CLOUD_CONFIG_PROFILE/SPRING_CLOUD_CONFIG_LABEL
```
