from hsk_client import HskClient

client = HskClient(api_key="YOUR_API_KEY")

# 1. Health check
print("Health Check:", client.health_check())

# 2. Quick Segmentation
res = client.segment("周末，我和朋友参观了城市博物馆。")
print("Annotated Text:", res.get("result"))

# 3. Detailed Analysis
analysis = client.analyze("今天天气很不错。")
print("Tokens Count:", len(analysis.get("tokens", [])))
