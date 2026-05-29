# AI Trading Signal SaaS MVP

A complete production-ready MVP for a trading signal platform built with FastAPI, PostgreSQL, Redis, Next.js, and TailwindCSS.

## Run locally

1. Start the full stack:

```bash
docker-compose up --build
```

2. Open the frontend at `http://localhost:3000`
3. The backend API is available at `http://localhost:8000`

## Architecture

- `backend/`: FastAPI API and background workers for market data and signal generation.
- `frontend/`: Next.js dashboard, auth, pricing, and signal history.
- `postgres`: Persistent market and signal database.
- `redis`: Stores the latest signal for live updates.

## API endpoints

- `POST /auth/register`
- `POST /auth/login`
- `GET /market/data`
- `GET /market/live`
- `GET /signals/latest`
- `GET /signals/history`
- `GET /signals/stream` (WebSocket)
- `GET /me`
- `GET /admin/stats`

## Environment variables

- `DATABASE_URL` - PostgreSQL connection string
- `REDIS_URL` - Redis connection string
- `JWT_SECRET` - JWT signing secret
- `ACCESS_TOKEN_EXPIRE_MINUTES` - Token lifetime in minutes
- `BINANCE_SYMBOL` - Market symbol used for signals
- `FREE_SIGNAL_DELAY_SECONDS` - Delay applied to free tier signals
- `NEXT_PUBLIC_API_URL` - Frontend API URL

## GitHub Codespaces

Run the same command in Codespaces:

```bash
docker-compose up --build
```

Then use forwarded ports for `3000` and `8000`.

## GitHub + Vercel Deployment

This repo is ready to host on GitHub and deploy the frontend on Vercel.

1. Connect the repository `https://github.com/nofuxgvnwiring-source/MVP` to Vercel.
2. Configure the project root directory as `frontend`.
3. Add the environment variable `NEXT_PUBLIC_API_URL` in Vercel to point to your backend host.
4. Push to `main` to trigger deployment.

A GitHub Actions workflow is included at `.github/workflows/vercel-deploy.yml` for Vercel production deploys.

For an online backend, deploy the API separately using a container host such as Render or Railway. This repository includes `render.yaml` for Render and `backend/README.md` with deployment instructions.

> Note: The backend is still designed to run separately. For production, host the backend API on a stable host and set `NEXT_PUBLIC_API_URL` accordingly.
