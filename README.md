### 准备
    git clone https://github.com/llango/sha-bootstrap-flask.git
进入sha-bootstrap-flask 目录

    mv config_templates.py config.py
修改config.py 里面相关配置。
 
### 安装依赖
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    
### 运行
    python app.py runserver 

    # 如果要要指定端口加上 -p  便可。
    python app.py runserver -p 5000

### 效果图

截图如下
![首页截图](./screen/index.jpg)