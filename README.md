# HSK Chinese Segmenter & Level Annotation API Client

[![API Portal](https://img.shields.io/badge/API_Portal-Live-brightgreen)](http://47.100.50.47:8765/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**English** | [简体中文](README_CN.md)

Official lightweight API Client and SDK for the **HSK Chinese Word Segmentation & Level Annotation API**.

This repository provides Python and JavaScript SDKs to interact with the cloud-hosted HSK API service.

- **Live API Playground & Docs**: [http://47.100.50.47:8765/](http://47.100.50.47:8765/)
- **API Base URL**: `http://47.100.50.47:8765`

---

## 🚀 Quick Start

### 1. Python Usage

```python
from hsk_client import HskClient

# Initialize client with your API Key
client = HskClient(api_key="YOUR_API_KEY")

# Quick text segmentation with HSK levels
res = client.segment("周末，我和朋友参观了城市博物馆。")
print(res["result"])
# Output: 周末[3]，我[1]和[1/7-9]朋友[1]参观[4]了[1]城市[3]博物馆[5]。

# Detailed tokenization & metadata
data = client.analyze("今天天气很不错。")
for token in data["tokens"]:
    print(token["text"], token.get("display_level"), token.get("pinyin"))
```

---

### 2. cURL Usage

```bash
curl -X POST http://47.100.50.47:8765/api/segment \
     -H "X-API-Key: YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"text": "周末，我和朋友参观了城市博物馆。"}'
```

---

### 3. JavaScript / Fetch Usage

```javascript
fetch('http://47.100.50.47:8765/api/segment', {
  method: 'POST',
  headers: {
    'X-API-Key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ text: '周末，我和朋友参观了城市博物馆。' })
})
.then(res => res.json())
.then(data => console.log(data.result));
```

---

## 📡 API Specification

| Endpoint | Method | Auth Required | Description |
| :--- | :--- | :--- | :--- |
| `/api/health` | `GET` | No | Public service health check |
| `/api/segment` | `POST` | Yes (`X-API-Key`) | Returns text annotated with HSK levels like `Word[Level]` |
| `/api/analyze` | `POST` | Yes (`X-API-Key`) | Returns detailed tokens, POS, Pinyin, and difficulty metadata |

---

## 🛡️ Security & Protection Limits

- **Auth**: Protected API endpoints require an `X-API-Key` HTTP header. Never place keys in URLs or client-side source code.
- **Rate Limit**: 60 requests per minute per IP address.
- **Max Length**: 10,000 characters per request.

---

## 📄 License

MIT License.
