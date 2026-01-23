# X (Twitter) Posts & Videos Analytics API

A production-ready FastAPI backend for extracting public tweet and video analytics for X (Twitter). Optimized for RapidAPI monetization and easy deployment on Railway.

## Features
- **Public Metadata Only**: Compliance with platform terms.
- **RapidAPI Ready**: Built-in header authentication for `X-RapidAPI-Key`.
- **Monetization Focused**: Structured endpoints for various analytics services.
- **Railway Optimized**: Ready for instant deployment.

## Project Structure
```
twitter-analytics-api/
├── main.py
├── requirements.txt
└── README.md
```

## Setup Locally

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the API**:
   ```bash
   uvicorn main:app --reload
   ```

3. **Access Documentation**:
   Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the interactive Swagger UI.

## Deployment to Railway

1. **Push to GitHub**:
   Initialize a git repo and push it to your GitHub account.

2. **Connect to Railway**:
   - Go to [Railway.app](https://railway.app).
   - Create a New Project -> Deploy from GitHub.
   - Select your repository.

3. **Configure Start Command**:
   Railway should automatically detect the FastAPI app, but if needed, set the start command to:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

## RapidAPI Integration

When listing on RapidAPI, ensure you:
1. Configure your endpoints to match the paths in `main.py`.
2. Map the `X-RapidAPI-Key` header to be sent with every request.

## Endpoints

- `GET /`: Health check.
- `POST /twitter/tweet/analytics`: Detailed tweet metrics.
- `POST /twitter/video/analytics`: Video-specific performance data.
- `POST /twitter/hashtag/insights`: Hashtag trend and popularity data.

---
*Disclaimer: This API is for public data analytics and insights only.*
