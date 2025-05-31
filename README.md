# website
本人的python课程结课作业，一个基于Django web框架开发的简易学生信息管理系统，能实现对学生信息，课程信息，学生成绩的增删改查功能。

## 快速开始

### 1. 克隆项目  
```
git clone https://github.com/lasock/website.git
cd website
```

### 2. 安装依赖  
`pip install -r requirements.txt`

### 3. 初始化数据库  
`python manage.py migrate`

### 4. 创建管理员账号(可选)  
`python manage.py createsuperuser`

### 5. 运行开发服务器  
`python manage.py runserver`

## 项目结构
```
website/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── core/                  # 主应用
│   ├── migrations/        # 数据库迁移文件
│   ├── templates/         # HTML模板
│   ├── admin.py           # 后台管理配置
│   ├── apps.py
│   ├── models.py          # 数据模型
|   ├── forms.py           # 数据表单
│   ├── tests.py
│   ├── urls.py            # 应用路由
│   └── views.py           # 视图函数
└── guanlixitong/          # 项目配置
    ├── settings.py        # 项目设置
    ├── urls.py            # 主路由\
    ├── static/            # 静态数据
    ├── asgi.py
    └── wsgi.py

```

