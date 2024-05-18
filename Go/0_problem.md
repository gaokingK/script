### go mod tidy 
```
[root@iZuf68h0usx91bux03msu1Z procexporter]# go mod tidy                                                                                   │mod  sumdb
go: finding module for package gopkg.in/alecthomas/kingpin.v2                                                                              │[root@iZuf68h0usx91bux03msu1Z gopath]# ls pkg/mod/
go: finding module for package github.com/prometheus/client_golang/prometheus                                                              │cache  github.com  gopkg.in
go: finding module for package github.com/prometheus/client_golang/prometheus/promhttp                                                     │[root@iZuf68h0usx91bux03msu1Z gopath]# ls pkg/mod/github.com/
go: finding module for package github.com/go-kit/log                                                                                       │go-kit  prometheus
go: found github.com/go-kit/log in github.com/go-kit/log v0.2.1                                                                            │[root@iZuf68h0usx91bux03msu1Z gopath]# grep kingpin.v2 -r .
go: found github.com/prometheus/client_golang/prometheus in github.com/prometheus/client_golang v1.15.1                                    │./src/github.com/prometheus/quantdo_mysqld_exporter_patch/quantdo_seat.go:      "gopkg.in/alecthomas/kingpin.v2"
go: found github.com/prometheus/client_golang/prometheus/promhttp in github.com/prometheus/client_golang v1.15.1                           │./src/procexporter/quantdo_seat.go:     "gopkg.in/alecthomas/kingpin.v2"
go: found gopkg.in/alecthomas/kingpin.v2 in gopkg.in/alecthomas/kingpin.v2 v2.3.2                                                          │./src/go.sum:gopkg.in/alecthomas/kingpin.v2 v2.2.6/go.mod h1:FMv+mEhP44yOT+4EoQTLFTRgOQ1FBLkstjWtayDeSgw=
go: procexporter imports                                                                                                                   │./pkg/mod/gopkg.in/alecthomas/kingpin.v2@v2.3.2/doc.go://     import "github.com/alecthomas/kingpin/v2"
        gopkg.in/alecthomas/kingpin.v2: gopkg.in/alecthomas/kingpin.v2@v2.3.2: parsing go.mod:                                             │./pkg/mod/gopkg.in/alecthomas/kingpin.v2@v2.3.2/go.mod:module github.com/alecthomas/kingpin/v2
        module declares its path as: github.com/alecthomas/kingpin/v2                                                                      │./pkg/mod/gopkg.in/alecthomas/kingpin.v2@v2.3.2/README.md:    $ go get github.com/alecthomas/kingpin/v2
                but was required as: gopkg.in/alecthomas/kingpin.v2
# 解决这个module declares its path as xxx, but was required as:xxxx https://blog.csdn.net/liuqun0319/article/details/104054313
vim go mod 
# 添加
replace github.com/alecthomas/kingpin/v2 => gopkg.in/alecthomas/kingpin.v2 v2.3.2 // indirect
replace gopkg.in/alecthomas/kingpin.v2 => github.com/alecthomas/kingpin/v2 v2.3.2 // indirect
```
### found packages procexporter (cgroup.go) and collector (quantdo_seat.go) in /root/j_go/monitor/gopath/src/procexporter
原因是在同一个folder存在多个package, 则加载失败. 即使是main, 也一样

### used for two different module paths 
```cs
// 解决办法https://blog.csdn.net/oscarun/article/details/105321846
go mod edit -replace=github.com/alecthomas/kingpin/v2@v2.3.2=gopkg.in/alecthomas/kingpin.v2@v2.3.2 //这时go.mod里会增加一行然后再手动增加一行,结果是下面这样子
replace (
        github.com/alecthomas/kingpin/v2 v2.3.2 => gopkg.in/alecthomas/kingpin.v2 v2.3.2 
        gopkg.in/alecthomas/kingpin.v2 v2.3.2 => github.com/alecthomas/kingpin/v2 v2.3.2
)
// 正确的回显
[root@iZuf68h0usx91bux03msu1Z mysqld_exporter]# go get github.com/prometheus/mysqld_exporter                                                
go: added gopkg.in/alecthomas/kingpin.v2 v2.3.2 
```
