"""HSK Segmenter & Level Annotation API Python Client SDK"""

from __future__ import annotations
import requests
from typing import Dict, Any

class HskClient:
    def __init__(self, api_key: str = "hsk_sk_7f8a9b2c4e1d603a", base_url: str = "http://47.100.50.47:8765") -> None:
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "X-API-Key": self.api_key,
            "Content-Type": "application/json"
        }

    def health_check(self) -> Dict[str, Any]:
        """Check API server status."""
        res = requests.get(f"{self.base_url}/api/health")
        res.raise_for_status()
        return res.json()

    def segment(self, text: str) -> Dict[str, Any]:
        """Quick segment & annotate HSK levels for input text."""
        res = requests.post(f"{self.base_url}/api/segment", json={"text": text}, headers=self.headers)
        res.raise_for_status()
        return res.json()

    def analyze(self, text: str) -> Dict[str, Any]:
        """Get detailed tokenization, HSK levels, Pinyin, and POS metadata."""
        res = requests.post(f"{self.base_url}/api/analyze", json={"text": text}, headers=self.headers)
        res.raise_for_status()
        return res.json()
