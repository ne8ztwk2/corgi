#!/bin/bash

echo "安装 requirements.txt 中的依赖..."
pip install -r requirements.txt

echo "安装 Playwright 和相关浏览器依赖..."
playwright install --with-deps

echo "运行 pytest 测试..."
# pytest