# 变量
### link:
- https://learnku.com/docs/the-way-to-go/variable/3585
### 声明变量
- var identifier type
- 当一个变量被声明之后，系统自动赋予它该类型的零值：int 为 0，float 为 0.0，bool 为 false，string 为空字符串，指针为 nil
- 变量的命名规则遵循骆驼命名法，即首个单词小写，每个新单词的首字母大写;但如果你的全局变量希望能够被外部包所使用，则需要将首个单词的首字母也大写（第 4.2 节：可见性规则）。
- `:=` 快速声明变量，只能用在函数内部

### 声明并赋值
```go
var a int =5
//也可以
var a = 5
//当你想要给变量的类型并不是自动推断出的某种类型时，你还是需要显式指定变量的类型
var a int64 = 2
// 这种语法是错误的，因为并没有任何可以用来自动推断类型的依据
var a
// 快速声明变量，只能用在函数内部
a := 5
```

# 常量
- const 内的 iota是golang语言的常量计数器,只能在常量的表达式中使用，，即const内。
- iota在const关键字出现时将被重置为0(const内部的第一行之前)，const中每新增一行常量声明将使iota计数一次。
- 3 、"5" 也是常量

# 数组
- link：https://www.runoob.com/go/go-passing-arrays-to-functions.html
- 是同一种数据类型的固定长度的序列。一旦定义，长度不能变。以往认知的数组有很大不同。
- 数组是值类型，赋值和传参会复制整个数组，而不是指针。因此改变副本的值，不会改变本身的值。
- 数组的长度也是类型的一部分，所以[3]int 和 [5]int是不同的类型,所以说一个数组的类型时要带上长度 
- Go中，对于数组，我们更多的是使用切片（slice）而不是数组指针，因为切片更加灵活。
- 声明方式：
```cs
var identifer [len]type
var arr1 [5]int // arr1的类型是[5]int

// 由于数组是值类型，可以用new创建
var arr2 = new([5]int) // arr2的类型是*[5]int
(*arr2)[0]=1

//使用数组常量的方式创建
var arrAge = [5]int{18, 20, 15, 22, 16}
var arrLazy = [...]int{5, 6, 7, 8, 22}
var arrLazy = []int{5, 6, 7, 8, 22}
var arrKeyValue = [5]string{3: "Chris", 4: "Ron"}
var arrKeyValue = []string{3: "Chris", 4: "Ron"}

// 类型转换
data := []int{74, 59, 238, -784, 9845, 959, 905, 0, 0, 42, 7586, -5467984, 7586}
type array_name []int
a := IntArray(data) //conversion to type IntArray from package sort
//

# 可以把长度和类型写在等号右边
var balance = [5]float32{1000.0, 2.0, 3.4, 7.0, 50.0}
# 可以使用 ... 代替数组的长度，编译器会根据元素个数自行推断数组的长度 var b = [...]string{"hi"}
# 也可以不写 var b = []string{"hi"}
# 如果设置了数组的长度，我们还可以通过指定下标来初始化元素
//  将索引为 1 和 3 的元素初始化
balance := [5]float32{1:2.0,3:7.0}
```