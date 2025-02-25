class Meta(type):
    def __new__(cls, name, bases, attrs):
        # 在类创建时添加add方法，该方法直接调用append
        print(f'__new__ {name} {bases} {attrs}')
        attrs['add'] = lambda s, x : print("addddddd")
        return super().__new__(cls, name, bases, attrs)
    def add(cls):
        print("55555")

# MyList类使用Meta作为元类
class MyList(metaclass=Meta):
    # 定义自己的add方法，打印并添加value+2
    def __init__(self, v):
        self.v=v

    # def add(self, value):
    #     print(f'add {value}')
        # return self.v + value
    


class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        # 注意此处的作用
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

def test():
    for i in range(1000000*1000000):
        a = 11111 * 1111
    return a

if __name__ == "__main__":
    u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
    print(u.id)
    from  multiprocessing import Process
    p_list = []
    for i in range(3):
        p = Process(target=test, args=())
        p_list.append(p)
        p.start()
    for p in p_list:
        # p.start()
        p.join()
    
    # 创建MyList实例并调用add方法
    # l = MyList(3)
    # l.add(1)
