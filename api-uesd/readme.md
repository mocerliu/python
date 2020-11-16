#### api测试的框架
flask + sqlalchemy + mysql  
#### 使用说明
配置mysql连接  
生成models  
```cmd
sqlacodegen mysql+pymysql://root:root@127.0.0.1:3306/test > models.py
```
是情况手动为model添加__init__ 和 __repr__  
运行run.py