import os
import flwr as fl
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 隨機產生訓練資料
NUM_SAMPLES = 100
NUM_FEATURES = 2
np.random.seed(42)
X_train = np.random.rand(NUM_SAMPLES, NUM_FEATURES)
true_coef = np.array([1.5, -2.0])
y_train = X_train @ true_coef + np.random.randn(NUM_SAMPLES) * 0.1
X_test = np.random.rand(NUM_SAMPLES, NUM_FEATURES)
y_test = X_test @ true_coef + np.random.randn(NUM_SAMPLES) * 0.1

class SklearnClient(fl.client.NumPyClient):
    def __init__(self, cid):
        self.cid = cid
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)

    def get_parameters(self, config):
        # 取得模型參數（coef_ 與 intercept_）
        return [self.model.coef_, np.array([self.model.intercept_])]

    def set_parameters(self, parameters):
        # 設定模型參數
        self.model.coef_ = parameters[0]
        self.model.intercept_ = parameters[1][0]

    def fit(self, parameters, config):
        self.set_parameters(parameters)
        self.model.fit(X_train, y_train)
        return self.get_parameters(config), len(X_train), {}

    def evaluate(self, parameters, config):
        self.set_parameters(parameters)
        preds = self.model.predict(X_test)
        loss = mean_squared_error(y_test, preds)
        return float(loss), len(X_test), {"mse": float(loss)}

if __name__ == "__main__":
    server_address = os.environ.get("SERVER_ADDRESS", "fl-server:8080")
    cid = os.environ.get("CLIENT_ID", "client")
    fl.client.start_numpy_client(server_address=server_address, client=SklearnClient(cid))
