/**
 * HSK Segmenter API Node.js / Browser SDK
 */

class HskClient {
  constructor(apiKey, baseUrl = 'http://47.100.50.47:8765') {
    if (!apiKey || !apiKey.trim()) {
      throw new Error('apiKey must not be empty');
    }
    this.apiKey = apiKey;
    this.baseUrl = baseUrl.replace(/\/$/, '');
  }

  async healthCheck() {
    const res = await fetch(`${this.baseUrl}/api/health`);
    return await res.json();
  }

  async segment(text) {
    const res = await fetch(`${this.baseUrl}/api/segment`, {
      method: 'POST',
      headers: {
        'X-API-Key': this.apiKey,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text })
    });
    return await res.json();
  }

  async analyze(text) {
    const res = await fetch(`${this.baseUrl}/api/analyze`, {
      method: 'POST',
      headers: {
        'X-API-Key': this.apiKey,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text })
    });
    return await res.json();
  }
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = HskClient;
}
