# logRobocon
调车日志系统，基于python3.5.1-Django1.9.5

## 2016年04月28日
### updates:
>* 创建工程，添加app:blog(未配置)/userGroup(配置了模型与视图)

### blueprint:
>* 一个方便易用的调车日志系统，日后加入自动生成日志功能。

## 2016年05月04日
### updates:
>* 完成了登陆系统
>* 调整了目录，删除了冗余结构。

### blueprint:
>* 应当把自动生成日志作为核心业务。


## 目录树结构：
<pre>
.
├── assets
│   ├── css
│   │   ├── bootstrap.min.css
│   │   ├── bootstrap-theme.min.css
│   │   └── style.css
│   ├── img
│   │   └── 13.jpg
│   └── js
│       ├── bootstrap.min.js
│       ├── jquery.min.js
│       └── scripts.js
├── db.sqlite3
├── LICENSE
├── logRobocon
│   ├── apps
│   │   ├── blog
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── __init__.py
│   │   │   ├── migrations
│   │   │   │   ├── 0001_initial.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── __pycache__
│   │   │   │       ├── 0001_initial.cpython-35.pyc
│   │   │   │       └── __init__.cpython-35.pyc
│   │   │   ├── models.py
│   │   │   ├── __pycache__
│   │   │   │   ├── admin.cpython-35.pyc
│   │   │   │   ├── __init__.cpython-35.pyc
│   │   │   │   ├── models.cpython-35.pyc
│   │   │   │   ├── urls.cpython-35.pyc
│   │   │   │   └── views.cpython-35.pyc
│   │   │   ├── templates
│   │   │   │   ├── base-after.html
│   │   │   │   ├── base-before.html
│   │   │   │   ├── index-after.html
│   │   │   │   ├── index-before.html
│   │   │   │   ├── login.html
│   │   │   │   └── register.html
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-35.pyc
│   ├── __init__.py
│   ├── libs
│   │   ├── formsModel.py
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── forms.cpython-35.pyc
│   │       ├── formsModel.cpython-35.pyc
│   │       └── __init__.cpython-35.pyc
│   ├── __pycache__
│   │   ├── __init__.cpython-35.pyc
│   │   ├── settings.cpython-35.pyc
│   │   ├── urls.cpython-35.pyc
│   │   └── wsgi.cpython-35.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── logRobocon.xmind
├── manage.py
├── README.md
├── requirements
│   ├── common.txt
│   ├── dev.txt
│   └── prod.txt
├── requirements.txt
└── static
    ├── admin
    │   ├── css
    │   │   ├── base.css
    │   │   ├── changelists.css
    │   │   ├── dashboard.css
    │   │   ├── fonts.css
    │   │   ├── forms.css
    │   │   ├── login.css
    │   │   ├── rtl.css
    │   │   └── widgets.css
    │   ├── fonts
    │   │   ├── LICENSE.txt
    │   │   ├── README.txt
    │   │   ├── Roboto-Bold-webfont.woff
    │   │   ├── Roboto-Light-webfont.woff
    │   │   └── Roboto-Regular-webfont.woff
    │   ├── img
    │   │   ├── calendar-icons.svg
    │   │   ├── gis
    │   │   │   ├── move_vertex_off.svg
    │   │   │   └── move_vertex_on.svg
    │   │   ├── icon-addlink.svg
    │   │   ├── icon-alert.svg
    │   │   ├── icon-calendar.svg
    │   │   ├── icon-changelink.svg
    │   │   ├── icon-clock.svg
    │   │   ├── icon-deletelink.svg
    │   │   ├── icon-no.svg
    │   │   ├── icon-unknown-alt.svg
    │   │   ├── icon-unknown.svg
    │   │   ├── icon-yes.svg
    │   │   ├── inline-delete.svg
    │   │   ├── LICENSE
    │   │   ├── README.txt
    │   │   ├── search.svg
    │   │   ├── selector-icons.svg
    │   │   ├── sorting-icons.svg
    │   │   ├── tooltag-add.svg
    │   │   └── tooltag-arrowright.svg
    │   └── js
    │       ├── actions.js
    │       ├── actions.min.js
    │       ├── admin
    │       │   ├── DateTimeShortcuts.js
    │       │   └── RelatedObjectLookups.js
    │       ├── calendar.js
    │       ├── collapse.js
    │       ├── collapse.min.js
    │       ├── core.js
    │       ├── inlines.js
    │       ├── inlines.min.js
    │       ├── jquery.init.js
    │       ├── prepopulate.js
    │       ├── prepopulate.min.js
    │       ├── SelectBox.js
    │       ├── SelectFilter2.js
    │       ├── timeparse.js
    │       ├── urlify.js
    │       └── vendor
    │           ├── jquery
    │           │   ├── jquery.js
    │           │   ├── jquery.min.js
    │           │   └── LICENSE-JQUERY.txt
    │           └── xregexp
    │               ├── LICENSE-XREGEXP.txt
    │               └── xregexp.min.js
    ├── css
    │   ├── bootstrap.min.css
    │   ├── bootstrap-theme.min.css
    │   └── style.css
    ├── img
    │   └── 13.jpg
    └── js
        ├── bootstrap.min.js
        ├── jquery.min.js
        └── scripts.js

</pre>