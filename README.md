# FinalTHY - Linux 实验故障智能诊断系统

网络操作系统（Linux）期末考试 · 田昊阳 · 240200600

## 项目功能

基于 AI 的 Linux 实验故障智能诊断系统。学生粘贴报错日志，自动定位根因，返回修复命令和原理解释。

## 技术栈

后端：Django 4.2 LTS (Python 3.11)
模板：Django 原生模板引擎
部署：Nginx 反向代理 + Django runserver
工具链：Makefile + black + pylint + pytest

## 目录结构

FinalTHY/
├── config/           Django 项目配置
├── diagnose/         AI 诊断 APP
├── templates/        index.html
├── manage.py
├── Makefile
├── requirements.txt
└── README.md

## 本地启动

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
浏览器访问 http://localhost:8000/index

## 云主机部署

git clone https://github.com/540087104/FinalTHY.git
cd FinalTHY
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Nginx 反代配置 /etc/nginx/conf.d/django.conf:
server {
    listen 80;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
nginx -t && systemctl reload nginx

python manage.py runserver 0.0.0.0:8000 &
公网访问: http://47.106.163.69/index

## Makefile 命令说明

make install - 安装依赖
make run - 启动开发服务器
make format - black 代码格式化
make lint - pylint 代码检查
make test - pytest 运行测试

## 身份信息

学号：240200600
姓名：田昊阳
hostname：tianhaoyang
云主机公网 IP：47.106.163.69
GitHub 仓库：https://github.com/540087104/FinalTHY
