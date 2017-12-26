import os, re
from datetime import datetime

# 导入Fabric API:
from fabric.api import *

# 服务器登录用户名:
env.user = 'ubuntu'
# 服务器地址，可以有多个，依次部署:
env.hosts = ['13.230.246.216']

def pack():

    local('python3 setup.py sdist --formats=gztar', capture=False)

def deploy():

    # 之处发布产品的名称和版本
    dist = local('python3 setup.py --fullname', capture=True).strip()
    # 将代码归档上传到服务器当中的临时文件夹内
    put('dist/%s.tar.gz' % dist, '/tmp/yourapplication.tar.gz')
    # 创建一个文件夹，进入这个文件夹，然后将我们的归档解压到那里
    run('mkdir /tmp/yourapplication')
    with cd('/tmp/yourapplication'):
        run('tar xzf /tmp/yourapplication.tar.gz')
        # 使用我们虚拟环境下的 Python 解释器安装我们的包
        run('/var/www/yourapplication/env/bin/python setup.py install')
    # 现在我们的代码已经部署成功了，可以删除这个文件夹了
    run('rm -rf /tmp/yourapplication /tmp/yourapplication.tar.gz')
    # 最终生成 .wsgi 文件，以便于 mod_wsgi 重新加载应用程序
    run('touch /var/www/yourapplication.wsgi')