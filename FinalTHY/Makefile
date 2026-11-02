.PHONY: all install run lint test format help

all: install format lint test

help:
	@echo "可用目标："
	@echo "  make install  - 安装依赖"
	@echo "  make run      - 启动 Django 开发服务器"
	@echo "  make lint     - pylint 代码检查"
	@echo "  make test     - pytest 运行测试"
	@echo "  make format   - black 代码格式化"
	@echo "  make all      - install + format + lint + test"

install:
	pip install -r requirements.txt

run:
	python manage.py runserver 0.0.0.0:8000

lint:
	pylint --disable=all --enable=E,F diagnose config

test:
	pytest -v

format:
	black diagnose config templates
