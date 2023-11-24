# 时间序列预测算法
- prophet 时序预测模型 一个模型对应一个产品
- neural prophet predict 多时序预测模型、

## Prophet
- 根据趋势性、周期性、节假日、噪声者四种来根据历史数据来从这4个方面来预测未来某个时刻的数据
### link
- 官方文档：https://facebook.github.io/prophet/docs/quick_start.html
- https://zhuanlan.zhihu.com/p/457634985
- 原理简单介绍：https://juejin.cn/post/7053351173214404638
https://cloud.tencent.com/developer/article/1729825

### hello world
```py
import pandas as pd
from fbprophet import Prophet

# 读取数据 创建一个Pandas DataFrame对象，包含两列：ds（日期）和y（观测值）。确保日期列为Pandas的Datetime类型。
df = pd.read_csv('sales.csv')

# 导入Prophet并创建一个Prophet模型对象。
model = Prophet()

# 将数据集传递给模型并使用fit方法拟合模型。
model.fit(df)

# 使用make_future_dataframe方法创建一个包含要预测日期的DataFrame。
future = model.make_future_dataframe(periods=365)
# 使用predict方法对未来日期进行预测。
forecast = model.predict(future)

# 输出预测结果
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())
# 画图
fig1 = m.plot(forecast)
# 分类画图
fig2 = m.plot_components(forecast)
```
## NeuralProphet
基于python的一个开源的时间序列预测库，在prophet的基础上加入了神经网络对时间序列数据进行建模。
充分利用了PyTorch的梯度优化引擎来加快模型拟合的速度
引入了AR-Net来学习时间序列的自相关性

### link：
- https://zhuanlan.zhihu.com/p/339678462