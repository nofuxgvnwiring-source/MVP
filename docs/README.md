# AI Trading SaaS MVP

## Overview
A production-ready MVP platform hosted in GitHub Codespaces with a single command: `docker-compose up --build`.

### Architecture
- `backend/`: FastAPI service exposing auth, market, signals, user, and admin endpoints.
- `backend/app/workers/`: Background workers fetching Binance OHLCV candles and generating trading signals every minute.
- `frontend/`: Next.js + TypeScript + Tailwind user interface for login, dashboard, signals, and pricing.
- `postgres` and `redis` containers for persistence and caching.

## Running Locally
1. Start containers: `docker-compose up --build`
2. Open frontend: `http://localhost:3000`
3. Backend API: `http://localhost:8000`

## Codespaces
In GitHub Codespaces, run:

```bash
docker-compose up --build
```

Then use the forwarded ports for `3000` and `8000`.

## GitHub + Vercel Deployment

This project is ready for GitHub hosting and Vercel frontend deployment.

- Connect the repository to Vercel.
- Set the Root Directory to `frontend`.
- Configure `NEXT_PUBLIC_API_URL` in Vercel to point at your backend API.
- Use the included workflow at `.github/workflows/vercel-deploy.yml` for production deployment.

The frontend is built from `frontend/`, while the API backend is expected to be hosted separately.

## API Documentation
- `POST /auth/register` - create a new user
- `POST /auth/login` - login and receive JWT
- `GET /market/data` - historical OHLCV candles
- `GET /market/live` - latest price
- `GET /signals/latest` - latest trading signal
- `GET /signals/history` - historical signal list
- `GET /signals/stream` - WebSocket stream for live updates
- `GET /me` - authenticated user profile
- `GET /admin/stats` - admin statistics (pro users only)

## Environment Variables
- `DATABASE_URL`: PostgreSQL connection string
- `REDIS_URL`: Redis connection string
- `JWT_SECRET`: Secret key for JWT
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration
- `BINANCE_SYMBOL`: Symbol for market data (default `BTCUSDT`)
- `FREE_SIGNAL_DELAY_SECONDS`: Delay for free tier signals
- `NEXT_PUBLIC_API_URL`: Frontend API target
