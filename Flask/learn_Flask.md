# Flask app 方法 
- app.route()

## 钩子函数
- link
  - https://zhuanlan.zhihu.com/p/48141683
钩子函数可以分为两层说明，第一层是 app 层，第二层则是 blueprint 层
### app层的钩子函数
- app.before_request # 在每次请求前都会执行，如果有return 则会作为这次请求的返回
```
app = Flask(__name__)

@app.before_request
def before_request():
    print('before request started')
    return "" 
```
- app.before_first_request 
  - 仅在第一次请求的时候去调用这个函数，比如初始化加载一次性的数据。和 before_request 不同的是, 它的非空返回值会被忽略。 会比before_request 先执行

- after_request
  - 在每次请求结束后运行
  - 带有一个参数，用来接收response_class，一个响应对象，一般用来统一修改响应的内容，比如修改响应头。
- app.teardown_request 
  - 在每次请求结束调用，不管是否出现异常,
  - 需要一个参数，这个参数用来接收异常，当然没有异常的情况下这个参数的值为 None,
  - 一般它用来释放程序所占用的资源，比如释放数据库连接
  - fter_request 先执行。从Flask 0.7开始，如果出现未处理的异常，after_request 将不会被执行,而这个将正常运行并接收异常
### blueprint层的钩子函数
```
user = Blueprint("user", __name__)

@user.before_app_request 每次请求前都会做
@user.before_request 只有user路由的每次请求前才会做
def check_login():
    user_service.check_permission()
```

# Flask HTTP方法
### 不同的HTTP方法代表了从指定URL中获取数据的不同方法
    |   |   |
    |:-:|---|
    |GET|将数据发送到服务器，不加密|
    |HEAD|和GET一样，但是没有响应体|
    |POST|提交表单数据，但是服务器不缓存响应|
    |PUT|用上传的内容替换目标资源的当前表示|
    |DELETE|删除由URL给出的当前资源的所有当前表示|

### 不同方法获取参数
- request.get_data() # 获取body里的参数
- request.get_json() 只能获取json格式参数， # 请求头Content-Type: application/json
    ```python
    # 请求体中有个表格
    @app.route('/login',methods = ['POST', 'GET'])
    def login():
        if request.method == 'POST':
            user = request.form['nm']
            return redirect(url_for('success',name = user))
        else:
            user = request.args.get('nm')
            # user = request.args.get("nm", type=bool)# 只有字符串为空才会是False 请求参数传递bool布尔值
            return redirect(url_for('success',name = user))
    ```

# Flask 模板
### 为什么要使用模板
    - 在处理最简单的请求时，视图函数的主要作用是生成请求的响应，这里视图函数的功能大致分为两类：逻辑处理和数据展示
    - 但是在大型业务中，把逻辑处理和展示内容放在一起，会极大的增加代码开发的难度和加重维护的复杂性。
    - 模板就是通过占位符实现动态内容的响应文本，其中占位符通过向模板引擎报告来从视图函数返回的数据中填充
    - 通过使用模板，视图函数就可以集中在业务逻辑和数据处理，而将数据结果的展示转移到模板，从而降低耦合度，是代码结构更清晰
### Flask模板的基本使用
    ```python
    @app.route('/')
    def index():
        # 往模板中传入的数据
        my_str = 'Hello Word'
        my_int = 10
        my_array = [3, 4, 2, 1, 7, 9]
        my_dict = {
            'name': 'xiaoming',
            'age': 18
        }
        return render_template('hello.html',
                            my_str=my_str,
                            my_int=my_int,
                            my_array=my_array,
                            my_dict=my_dict
                            )

    ```
  - hello.html 
    ```html
    <br />{{ my_str }}
    ```
### 其他用法
    ```python
    <script type = "text/javascript" 
        src = "{{ url_for('static', filename = 'hello.js') }}" ></script>
    ```
# Flask g/session/request
## g(global)
- 保存的内容在一个请求的生命周期中可以全局使用
- g能存储dict吗 可以
```
from flask import g
g.account = xxx
# 获取
print(g.accout)
uid = g.get("uid", None)
```
# Flask request对象
### request 代表来自客户网页端的数据作为全局请求对象发送到服务器
    |||
    |--|--|
    |Form|包含表单参数和其值的键值对|
    |args|解析查询字符串，是URl？号之后的一部分|
    |Cookies|保存cookie名称和值的一个字典对象|
    |files|与上传文件有关的一个数据|
    |method|当前请求方法|
### Form 属性
    Form 属性包含表单参数和值的键值对
    ```html
    <form action="http://localhost:5000/result"" method="POST">
     <p>Name <input type = "text" name = "Name" /></p>
     <p>Physics <input type = "text" name = "Physics" /></p>
    </form>

    # 另一个模板中
    <table border = 1>
    {% for key, value in result.items() %}
    <tr>
       <th> {{ key }} </th>
       <td> {{ value }}</td>
    </tr>
    {% endfor %}
    ```
# Flask cookies
- Request对象包含cookie的属性，他是所有cookie变量及其对应值的字典对象，cookie还储存网站的到期时间，路径和域名
### 对cookie的处理步骤
    设置cookie
    ```python
    resp = make_response("success")   # 设置响应体
    resp.set_cookie("w3cshool", "w3cshool", max_age=3600)
    ```
    获取cookie
    ```python
    cookie_1 = request.cookies.get("w3cshool")
    ```
    删除cookie(让cookie过期)
    ```python
    resp = make_response("this is fake delete")
    resp.delete_cookie("w3cschool")
    ```
# Flask 会话
- 会话保存在服务器上
- 每个客户端的会话会分配到一个会话ID， 会话ID存储在Cookie
- session允许在不同的请求之间储存消息
- session 也是一个字典对象，包含会话变量和关联值的键值对，这个对象相当于使用密钥加密的cookie，用户可以看到，但是如果没有密钥就没法修改他
- 需要应用程序定义一个**SECRET_KEY** 因为服务器对会话数据以加密方式对其进行了签名。
    `app.secret_key = 'any random string’`
### 对session的处理步骤
    设置一个密钥
    `app.secret_key = "xxxx"`
    设置一个'username'会话变量
    `session['username']='admin'`
    释放某一个session变量
    `session.pop('username', None)`

# Flask 重定向、状态码、错误
- 重定向 
    ```python
    redirect(location, statuscode, response)
    # statuscode 发送到浏览器， 默认是302
    # response 用于实例化响应
    ```
- 错误
    ```python
    abort(code)
    # 出错时直接调用
    ```

# Flask 消息闪现
- flash()方法，将消息传递给下一个请求，该请求通常是一个template
    ```python
    flash(message, category)
    # category: error, info, warning
    ```
- 在Template中接受消息
    ```python
    get_flashed_message(with_categories, category_filter)
    # 均为可选
    # 例子
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            {% for message in messages %}
                {{ message }}
            {% endfor %}
        {% endif %}
    {% endwith %}
    ```
- 使用参数传递消息
    ```python
    return render_template('login.html', error = error)
    # template中
    {% if error %}
        <p><strong>Error</strong>: {{ error }}</p>
    {% endif %}
    ```
# Flask 文件上传
- 一些配置
    |||
    |--|--|
    |`app.config['UPLOAD_FOLDER']`|定义上传文件夹的路径|
    |`app.config['MAX_CONTENT_PATH']`|指定要上传文件的最大Bytes|
- 需要一个表单， 表单<code>enctype</code>属性为<code>multipart/form-data</code>
    ```html
    <form action = "http://localhost:5000/uploader" method = "POST" 
         enctype = "multipart/form-data">
        <input type = "file" name = "file" />
        <input type = "submit"/>
    </form>
    ```
- 处理
    ```python
    # 获取文件对象
    f = request.files['file']
    # 建议获取文件名的方式
    f_name = secure_filename(f.filename)
    # save
    f.save(f_name)
    ```
    上传的文件会先保存在服务器上的临时位置，然后将其保存到实际位置

# Flask WTF
- WTForms 是一个灵活的表单，渲染和验证库，Flask-WTF为这个库提供了一个简单的接口，使我们可以在Python脚本中定义表单字段，并使用HTML模板进行渲染，还可以将验证应用于WTF字段
- 安装Flask-WTF扩展
    `pip install flask-WTF`
- 定义表单字段
    flask-WTF包含一个<code>Form</code>类，必须使用该类作为用户定义表单的父类
    定义的字段在渲染时会自动转为等效的HTML标签
    ```python
    class ContactForm(Form):
        name = TextField("Name of Student")
    # 会自动创建CSRF令牌的隐藏字段
    ```
- 使用验证器
    HTML本身无法验证用户的输入， 而WTForms包含的验证器类，可以对表单字段应用验证
    ```python
    email = TextField("Email", [validators.Required("Please enter your email."),
                                validators.Email("Not a valid eamil")])
    # 内容未通过验证器，表单对象的validate()将验证表单数据内容并抛出验证错误 Error消息将会发送到Template
    {%for message in form.email.errors %}
        {{message}}
    {% endfor %}
    ```
# Flask SQLAlchemy
### SQLAlchemy 是一个强大的ORMapper， 为开发人员提供了SQL的全部功能和灵活性。Flask-SQLAlchemy 是Flask扩展，用来提供Flask对SQLAlchemy的支持
    `pip install flask-sqlalchemy`
### 初始化
    ```python
    from flask-sqlchemy import SQLAlchemy
    # 创建一个Flask应用程序对象并设置要使用数据库的URI
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
    ```
### 使用Flask应用程序对象作为参数创建一个SQLAlchemy对象，该对象包含：用于ORM操作的函数， 一个父Model类，使用父Model类来声明用户定义的模型
    ```python
    db = SQLAlchemy(app)
    #创建students模型
    class Students(db.Model):
        id = db.Column('student_id', db.Integer, primary_key = True)
        pass

    # 不应该是模型类的方法吗？
    def __init__(self, name, city, ignore):
        self.name = name
        pass
    ```
### 使用creat_all()方法创建/使用 URI中指定的数据库
    `db.create_all()`
### SQLAlchemy 的Session 对象管理ORM对象的所有持久化操作
    - db.session.add(student)
    - db.session.delete()
    - db.session.query.all()
    - db.session.query.filter_by(condition).all()
    - 通过调用commit()方法来提交记录
    - db.session.commit()

