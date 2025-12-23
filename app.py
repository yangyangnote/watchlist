from flask import Flask, url_for
from markupsafe import escape

# 这句是从 flask 包里导入 Flask 类
app = Flask(__name__)
# app 网站入口
# 就像在说“用当前这个文件（模块)的名字/帮我建一个 Web 应用对象


# 当浏览器访问根路径 /时，调用下面这个函数
@app.route("/")
@app.route("/index")
@app.route("/home")
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route("/user/<name>")
def user_page(name):
    return f"User: {escape(name)}"


@app.route("/test")
def test_url_for():
    # 下面是一些调用示例（访问 http://localhost:5000/test 后在命令行窗口查看输出的 URL）：
    print(url_for("hello"))  # 生成 hello 视图函数对应的 URL，将会输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for("user_page", name="greyli"))  # 输出：/user/greyli
    print(url_for("user_page", name="peter"))  # 输出：/user/peter
    print(url_for("test_url_for"))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for("test_url_for", num=2))  # 输出：/test?num=2
    return "Test page"
