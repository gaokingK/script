# 指针
通过指针，可以简化一些 C++ 编程任务的执行；还有一些任务，如动态内存分配，没有指针是无法执行的
- link
    - https://www.runoob.com/cplusplus/cpp-pointers.html

### 内存地址和指针
- 内存地址
    - 每一个变量都有一个内存位置，每一个内存位置都定义了可使用连字号（&）运算符访问的地址`cout << "var's addr is:"<< &var_name`
- 指针的声明与使用
    - 指针是一个变量，其值为另一个变量的地址.就像其他变量或常量一样，您必须在使用指针存储其他变量地址之前，对其进行声明。`type *var_name`
        - type 要和指向的变量类型一致
    - 所有指针的值的实际数据类型都是一个代表内存地址的长的十六进制数

```
#include<iostream>
using namespace std;
int main(){
    int a=123;

    //&a表示a在内存中的地址，也就是123在内存中的地址
    cout<<"a: "<<a<<endl<<"a's address："<<&a<<endl;

    //声明指针，指向a所在的地址
    int *p=&a;
    cout<<"p: "<<p<<endl;

    //使用指针，在p之前添加*表示p指向地址中的值
    cout<<"p's value: "<<*p<<endl;

    //同时p也是 一个变量，在内存中也有一个地址储存它，但其地址不是a的地址
    cout<<"p's address: "<<&p<<endl;

    //&p是一个内存地址，*&p表示 这个内存地址中存的值,在这里表示a的地址， 即p本身的值（*&p==p）
    cout<<"*&p: "<<*&p<<endl;

    //刚才我们已经知道*&p是a的地址，那么**&p就表示a的值（**&p==*p==a)
    cout<<"**&p: "<<**&p<<endl;
return 0;}
```
- 如果仔细观察会发现p和a的地址是连续的，间隔为4，这与int是4个字节的数据类型的事实相符合