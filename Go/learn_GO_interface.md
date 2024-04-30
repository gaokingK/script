# 定义接口
```go
// 接口名一般以er结束
type inf_name interface {
    // 定义这个接口的方法集
    method1(param_list) return_type
    ...
}
```
# 类型实现接口
- 如果某个类型实现接口中的方法集就认为该类型实现了该接口
```go
// 定义类型
type struct1 struct{
    property1 int
}
// 实现接口中的方法
function (p struct1) method1(param_list) return_type{
    //do something
}
```

### 接口的方法
- 定义接口的方法，这些方法可以让实现接口的类型去调用
```go
func intf_method1(data intf_name) {
    //do something
}
// 让接口去调用
var1 := struct1{property1_value}
intf_method1(var1)
```