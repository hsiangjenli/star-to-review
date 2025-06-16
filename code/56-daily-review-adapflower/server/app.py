import flwr as fl
from flwr.server.strategy import FedAvg
from flwr.server.client_proxy import ClientProxy
from typing import List, Tuple, Dict
from prometheus_client import start_http_server, Gauge

# Prometheus metrics
LOSS_GAUGE = Gauge('fl_loss', 'Average loss in each round')
CLIENT_COUNT_GAUGE = Gauge('fl_client_count', 'Number of clients per round')
CLIENT_ID_GAUGE = Gauge('fl_client_id', 'Client present in round', ['client_id'])

class PrometheusStrategy(FedAvg):
    def aggregate_evaluate(self, server_round, results, failures):
        client_ids = [client.cid for client, _ in results]
        # Flower >=1.8.0: results 是 (client, EvaluateRes) tuple
        losses = [res.loss for _, res in results]
        avg_loss = sum(losses) / len(losses) if losses else 0.0
        LOSS_GAUGE.set(avg_loss)
        CLIENT_COUNT_GAUGE.set(len(client_ids))
        CLIENT_ID_GAUGE.clear()
        for cid in client_ids:
            CLIENT_ID_GAUGE.labels(client_id=cid).set(1)
        print(f"[Prometheus] Round {server_round}: clients={client_ids}, avg_loss={avg_loss}")
        return super().aggregate_evaluate(server_round, results, failures)

import time

if __name__ == "__main__":
    # 啟動 Prometheus metrics server
    start_http_server(8000)
    print("Prometheus metrics server started on port 8000")
    strategy = PrometheusStrategy()
    fl.server.start_server(server_address="0.0.0.0:8080", config=fl.server.ServerConfig(num_rounds=200), strategy=strategy)
    # 訓練結束後保持 metrics endpoint 存活
    print("Training finished. Keeping metrics endpoint alive for Prometheus scrape.")
    while True:
        time.sleep(60)
