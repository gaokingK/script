# 定义函数
```
func (st *struct_name) func_name(parm1 parm1_type, ...) return1_type {

}
```
- 方法所属的类型可以是指针类型，也可以是值类型，关键看是否需要修改这个类型的一些属性

# 参数
- `...` 在Go语言中，...运算符的出现在类型之前，表示该函数接受不定数量的参数，这样的参数在Go中被称为可变参数（Variadic parameters）。它让你传递任意数量的参数给函数。
- 函数classifier定义的时候使用了...interface{}，这意味着它可以接收任意数量的参数，而且这些参数可以是任何类型，因为interface{}是Go中所有类型的空接口，所以任何值都实现了interface{}。
这里有一个使用可变参数的例子：
```go
func classifier(items ...interface{}) {
    for i, x := range items {
        switch x.(type) {
        case bool:
            fmt.Printf("Param #%d is a bool\n", i)
        case float64:
            fmt.Printf("Param #%d is a float64\n", i)
        case int, int64:
            fmt.Printf("Param #%d is an int\n", i)
        case nil:
            fmt.Printf("Param #%d is a nil\n", i)
        case string:
            fmt.Printf("Param #%d is a string\n", i)
        default:
            fmt.Printf("Param #%d is unknown\n", i)
        }
    }
}

func main() {
    classifier(13, "hello", 9.15, true)
}
# classifier函数可以接受任何类型和数量的参数。在函数内部，使用了类型断言的switch语句来确定每个参数的类型，并打印出对应的消息。
```