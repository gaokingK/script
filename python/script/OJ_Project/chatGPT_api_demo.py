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
content = """bash 怎么设置像tch一样的自动补齐,如果有多个候选项时，可以使用tab键循环显示匹配列表中的项目"""

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": content}]
)

print(completion.choices[0].message.content)
print(completion.usage)

