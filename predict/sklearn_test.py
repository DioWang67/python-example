# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import r2_score

# # 載入股票價格數據
# data = pd.read_csv('stock_data.csv')  # 假設股價數據保存在stock_data.csv中

# # 分離特徵和標籤
# X = data[['RSI', 'Price']].values
# y = data['NextPrice'].values

# # 切割數據集為訓練集和測試集
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # 建立線性回歸模型
# model = LinearRegression()
# model.fit(X_train, y_train)

# # 在測試集上進行預測
# y_pred = model.predict(X_test)

# # 計算R平方值作為模型準確性指標
# r_squared = r2_score(y_test, y_pred)
# print("Model R-squared:", r_squared)

# # 進行單筆預測
# new_data = np.array([[78, 162]])  # 輸入新的RSI和股價值
# prediction = model.predict(new_data)
# print("Predicted Next Price:", prediction[0])



# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import r2_score

# # 載入股票價格數據
# data = pd.read_csv('stock_data.csv')  # 假設股價數據保存在stock_data.csv中

# # 分離特徵和標籤
# X = data[['RSI', 'Price', 'MACD', 'K', 'D', 'J']].values
# y = data['NextPrice'].values

# # 切割數據集為訓練集和測試集
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # 建立線性回歸模型
# model = LinearRegression()
# model.fit(X_train, y_train)

# # 在測試集上進行預測
# y_pred = model.predict(X_test)

# # 計算R平方值作為模型準確性指標
# r_squared = r2_score(y_test, y_pred)
# print("Model R-squared:", r_squared)

# # 進行單筆預測
# new_data = np.array([[63, 150, 3.7, 72, 62, 82]])  # 輸入新的RSI、股價、MACD和KDJ值
# prediction = model.predict(new_data)
# print("Predicted Next Price:", prediction[0])

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 假設這裡是您的歷史股價數據，包含KDJ、RSI和當日收盤價，以及下一日的收盤價
data = {
    'KDJ': [77.1, 68.2, 47.83, 44.59],
    'RSI': [68.9, 70.3, 56.1, 60.4],
    'Close_Price': [35.7, 35.95, 34.65, 35.3],
    #'Next_Day_Close_Price': [59.21, 68.9, 70.3, 70.3]  # 下一日的收盤價（用於訓練，這裡假設已知）
}

df = pd.DataFrame(data)

# 將特徵X和目標y拆分
X = df[['KDJ', 'RSI']]
y = df['Close_Price']

# 建立線性回歸模型
model = LinearRegression()

# 訓練模型
model.fit(X, y)

# 預測明日收盤價
new_data = np.array([[37.39, 55.86]])  # 使用最後一筆數據來預測明日收盤價
predicted_price = model.predict(new_data)
print("預測的明日收盤價：", predicted_price)

