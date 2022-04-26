from wsgiref.simple_server import make_server
import requests
# 导入编写的application函数
def application(environ, start_response):
    resp = requests.get('http://192.168.0.110/money/index.php?m=User&a=index')
    start_response('200 OK', [('Content-Type', 'text/html')])
    
    return [resp.content]

# 创建一个服务器，IP地址为空，端口是8000，传入函数application

httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
