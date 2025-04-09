"""
# 构建docker镜像
cd corgi
docker build -t corgi:latest .

# 运行docker容器
docker run \
    -v "$(pwd)/screenshots:/corgi/screenshots" \
    -v "$(pwd)/logs:/corgi/logs" \
    --name corgi \
    corgi:latest
运行过程的截图会放到 $(pwd)/screenshots/ 目录下


"""

print("hello world")
