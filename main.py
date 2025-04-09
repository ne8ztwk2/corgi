"""


# 构建docker镜像,构建过程会下载依赖
cd corgi
docker build -t corgi:latest .

# 运行docker容器,映射当前目录下的 screenshots 和 logs 目录到容器内
# 测试环境
docker run \
    -d \
    --rm \
    -v "$(pwd)/screenshots:/corgi/screenshots" \
    -v "$(pwd)/logs:/corgi/logs" \
    --name corgi \
    corgi:latest


# 调试环境
docker run \
    -it \
    --rm \
    -v "$(pwd)/screenshots:/corgi/screenshots" \
    -v "$(pwd)/logs:/corgi/logs" \
    --name corgi \
    corgi:latest \
    /bin/bash

    
"""
