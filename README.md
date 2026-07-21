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
client = HskClient(api_key="hsk_sk_7f8a9b2c4e1d603a")

# Quick text segmentation with HSK levels
res = client.segment("我爱学习汉语，清华大学很好。")
print(res["result"])
# Output: 我[1]爱[1]学习[1]汉语[1]，清华大学[未收录]很好[1/2/4/5]。

# Detailed tokenization & metadata
data = client.analyze("今天天气很不错。")
for token in data["tokens"]:
    print(token["text"], token.get("display_level"), token.get("pinyin"))
```

---

### 2. cURL Usage

```bash
curl -X POST http://47.100.50.47:8765/api/segment \
     -H "X-API-Key: hsk_sk_7f8a9b2c4e1d603a" \
     -H "Content-Type: application/json" \
     -d '{"text": "我爱学习汉语。"}'
```

---

### 3. JavaScript / Fetch Usage

```javascript
fetch('http://47.100.50.47:8765/api/segment', {
  method: 'POST',
  headers: {
    'X-API-Key': 'hsk_sk_7f8a9b2c4e1d603a',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ text: '我爱学习汉语。' })
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

- **Auth**: Requires `X-API-Key` HTTP Header or `api_key` query parameter.
- **Rate Limit**: 60 requests per minute per IP address.
- **Max Length**: 10,000 characters per request.

---

## 📄 License

MIT License.
