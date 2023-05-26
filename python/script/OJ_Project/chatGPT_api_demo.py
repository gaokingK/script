import openai
# 全局取消证书验证

# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context




# Set the API key
openai.api_key = "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"

# Define the model and prompt
# model_engine = "text-davinci-003"
model_engine = "gpt-3.5-turbo"
prompt = "今天日期是多少"

# Generate a response
# completion = openai.Completion.create(
#     engine=model_engine,
#     prompt=prompt,
#     max_tokens=1024,
#     n=1,
#     stop=None,
#     temperature=0.5,
# )


# Get the response text
# message = completion.choices[0].text

# print(message)
content = "go.mod中的module 关键字指定的模块路径有什么用"
content = "谢谢"
content = "请给我一个prometheus.MustNewConstMetric的示例程序并给出注释"
content = """帮我解释下这段代码：
```go
package collector

import (
	"context"
	"database/sql"
	"fmt"

	"github.com/go-kit/log"
	"github.com/prometheus/client_golang/prometheus"
	"gopkg.in/alecthomas/kingpin.v2"
)

var (
	quantdoDBName = kingpin.Flag(
		"collect.quantdo.dbname",
		"Change the database name used by quantdo",
	).Default("qdam").String()
)

// const mysqlQuantdoSeatsQuery = `select seatstatus, count(*) as count  from qdam.t_oper_seat group by seatstatus`
const mysqlQuantdoSeatsQuery = `select seatid, seatstatus from %s.t_oper_seat limit 256;`

// Metric descriptors.
var (
	seatsStatusCounterDesc = prometheus.NewDesc(
		prometheus.BuildFQName("quantdo", "seatsstatus", "count"),
		"The number of each seat status.",
		[]string{"seatstatus"}, nil)

	// used to fecth seatids
	seatsStatusIndicatorDesc = prometheus.NewDesc(
		prometheus.BuildFQName("quantdo", "seatsstatus", "indicator"),
		"Current status for each seat.",
		[]string{"seatid", "seatstatus"}, nil)
)

	ch <- prometheus.MustNewConstMetric(seatsStatusIndicatorDesc, prometheus.GaugeValue, v, "2", status)
	ch <- prometheus.MustNewConstMetric(seatsStatusCounterDesc, prometheus.GaugeValue, float64(c0), "0")
```
"""

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": content}]
)

print(completion.choices[0].message.content)
print(completion.usage)

