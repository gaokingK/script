# 准备
### for window
最好还是
- link
    - 本文档参照vscode C/C++ extension 里的文档， 文档里有该扩展对不同编译器和平台的教程，这里选择的是MSVC，
    - MSVC教程： https://code.visualstudio.com/docs/cpp/config-msvc
- 问题
    - 不同的编译器会有区别吗？
    - 必须从dev prompt中进入吗？

- 检查相关的workload是否已经在visual stdio 中安装， 或者是否安装MSVC
- 从Developer Command Prompt （使用管理员可能会有问题，倒是build不成功）中启动vscode `code .`
    - 要从命令行或 VS Code 使用 MSVC，您必须从 Visual Studio 的开发人员命令提示符运行。 
    - 或者参考（ Run VS Code outside a Developer Command Prompt.）
- 创建 helloworld
    ```
    mkdir projects
    cd projects
    mkdir helloworld
    cd helloworld
    code .
    ```
    - 然后在vscode里添加文件，并保存
- build helloworld.cpp
    -  Terminal > Configure Default Build Task ，Choose cl.exe build active file 
    - active file就是当前显示的文件；This will create a tasks.json file in a .vscode folder and open it in the editor.
- Running the build
    - ctrl + shift + B
- 运行和调试略
    - 运行可以在右边的run

# 名词
- *.pdb *.obj是 c++输出，调试文件
- C++ with exception
  - 不知道和C++的标准异常有什么区别
- STL（Standard Template Library），即标准模板库
  - 自带的标准库
  - https://blog.csdn.net/tanqiuwei/article/details/7323374
# 简单尝试
- 目录在 Desktop/people_win_lab/script/c_c++/下

# namespace
c++引入了命名空间主要解决了同一个项目（是项目还是一个cpp）可能出现的重名现象，如函数或者变量重名
- link
    - https://www.cnblogs.com/uniqueliu/archive/2011/07/10/2102238.html
    - https://blog.csdn.net/qq_21033779/article/details/78921997 ------------no
- 问题
    - 像std这样的标准库函数都有哪些？
    - 头文件是什么意思
- using namespace xxx的作用
    - 主要解决重名的问题，把重名的分别放到命名空间里，使用的时候通过xxx::func_name来调用，
        
    - 能简化代码的写法
        - using namespace xxx 就表示释放命名空间xxx中间的东西。好处在于我们在程序里面就不用在每个函数的头上都加上xxx::来调用
        ```
        # 没有 using namespace std
        std::count
        ```
- 应该注意的地方
    - 虽然释放命名空间能简化带来代码的写法，但已释放的多个命名空间中若是有重名同类型的，会在编译的时候报错，但若是主函数中有同名的，编译时就会使用这个而不报错。
    ```
    # 因为main中有a， 程序就不会报错，但若是删除就会报错
    namespace ZhangSan
    {
        int a=10; //张三把10赋值给了变量a
    }
    namespace LiSi
    {
        int a=5; //李四把10赋值给了变量a
    }    
    void main()
    {
        int a=1;
        using namespace ZhangSan;
        using namespace LiSi;
        cout<<a<<endl;
    }
    ```
- std 标准空间，定义了所有标准库函数

# lstrcpy、strcpy
- strcpy是C运行时函数,是标准C提供的函数 ；lstrcpy是Windows   API 
- 而StrCpy仅仅是lstrcpy的调用而已,相当于lstrcpy 
- 在微软的开发环境里比方说VC开发windows程序，最好使用lstrcpy()，否则很多地方会出问题

# 数据类型和变量类型
- 问题
    - 变量类型和数据类型既然不等同，那他们的差别在哪里呢？

- 常量
    - const（constant） 声明常量使用的一种关键字
  
# typedef struct与struct的区别
- link
    - https://blog.csdn.net/m0_37973607/article/details/78900184
- struct定义了一个结构体，typedef struct 能简化结构体的使用方式
    ```c++
    # struct 的使用
    struct tagMyStruct
    { 
    　int iNum; 
    　long lLength; 
    };
    # tagMyStruct称为“tag”，即“标签”，实际上是一个临时名字，struct 关键字和tagMyStruct一起，构成了这个结构类型
    # 可以用struct tagMyStruct varName来定义变量，但要注意，使用tagMyStruct varName来定义变量是不对的，因为struct 和tagMyStruct合在一起才能表示一个结构类型。
    # 这样使用起来的时候就有点繁琐
    typedef struct tagMyStruct
    { 
    　int iNum;
    　long lLength;
    } MyStruct;
    # 而上面的语句完成了两个功能， 1.定义一个新的结构类型（和上面的一样）2. typedef为这个新的结构起了一个名字，叫MyStruct
    # 这样就可以用 MyStruct varName来定义变量， 等价于struct tagMyStruct varName
    ```
# extern
- link
    - https://blog.csdn.net/sruru/article/details/7951019
-  extern是一个关键字，它告诉编译器存在着一个变量或者一个函数. 这样就可以在当前文件的后面或者其它文件中定义

# 输入与输出
- 标准输出流（cout）
    - 预定义的对象 cout 是 iostream 类的一个实例。cout 对象"连接"到标准输出设备，通常是显示屏
    - cout 是与流插入运算符 << 结合使用的， 流插入运算符 << 在一个语句中可以多次使用， << 运算符被重载来输出内置类型；endl 用于在行末添加一个换行符。
        ```c++
        char str[] = "Hello C++";
        cout << "Value of str is : " << str << endl;
        # Value of str is : Hello C++
        ```
- 标准输入流（cin）
    - 预定义的对 象 cin 是 iostream 类的一个实例。cin 对象附属到标准输入设备，通常是键盘，
    - cin 是与流提取运算符 >> 结合使用的; 流提取运算符 >> 在一个语句中可以多次使用
        ```c++
        char name[50];
        cout << "请输入您的名称： ";
        cin >> name;
        cout << "您的名称是： " << name << endl;
        # cin >> name >> age; 相当于
        cin >> name;
        cin >> age;
        ```
- 日志流(clog)/错误流(cerr)
