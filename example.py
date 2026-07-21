from hsk_client import HskClient

client = HskClient(api_key="hsk_sk_7f8a9b2c4e1d603a")

# 1. Health check
print("Health Check:", client.health_check())

# 2. Quick Segmentation
res = client.segment("我爱学习汉语，清华大学很好。")
print("Annotated Text:", res.get("result"))

# 3. Detailed Analysis
analysis = client.analyze("今天天气很不错。")
print("Tokens Count:", len(analysis.get("tokens", [])))
