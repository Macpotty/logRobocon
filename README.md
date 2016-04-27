# logRobocon
调车日志系统，基于python3.5.1-Django1.9.5

## 2016年04月28日
### updates:
* 创建工程，添加app:blog(未配置)/userGroup(配置了模型与视图)

### blueprint:
* 一个方便易用的调车日志系统，日后加入自动生成日志功能。





## 目录树结构：
<pre>
├── db.sqlite3
├── LICENSE
├── logRobocon
│   ├── apps
│   │   ├── blog
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── __init__.py
│   │   │   ├── migrations
│   │   │   │   ├── __init__.py
│   │   │   │   └── __pycache__
│   │   │   │       └── __init__.cpython-35.pyc
│   │   │   ├── models.py
│   │   │   ├── __pycache__
│   │   │   │   ├── admin.cpython-35.pyc
│   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   └── models.cpython-35.pyc
│   │   │   ├── tests.py
│   │   │   └── views.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-35.pyc
│   ├── __init__.py
│   ├── libs
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   └── __init__.cpython-35.pyc
│   │   └── userGroup
│   │       ├── admin.py
│   │       ├── apps.py
│   │       ├── __init__.py
│   │       ├── migrations
│   │       │   ├── 0001_initial.py
│   │       │   ├── __init__.py
│   │       │   └── __pycache__
│   │       │       ├── 0001_initial.cpython-35.pyc
│   │       │       └── __init__.cpython-35.pyc
│   │       ├── models.py
│   │       ├── __pycache__
│   │       │   ├── admin.cpython-35.pyc
│   │       │   ├── __init__.cpython-35.pyc
│   │       │   └── models.cpython-35.pyc
│   │       ├── templates
│   │       │   └── login.html
│   │       ├── tests.py
│   │       ├── urls.py
│   │       └── views.py
│   ├── __pycache__
│   │   ├── __init__.cpython-35.pyc
│   │   ├── settings.cpython-35.pyc
│   │   └── urls.cpython-35.pyc
│   ├── settings.py
│   ├── urls.py
│   ├── webContents
│   │   ├── css
│   │   │   ├── bootstrap.min.css
│   │   │   ├── bootstrap-theme.min.css
│   │   │   └── style.css
│   │   └── js
│   │       ├── bootstrap.min.js
│   │       ├── jquery.min.js
│   │       └── scripts.js
│   └── wsgi.py
├── manage.py
├── README.md
├── requirements
│   ├── common.txt
│   ├── dev.txt
│   └── prod.txt
└── requirements.txt
</pre>