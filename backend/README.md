# Backend Deployment

This backend is a FastAPI service that can be deployed as a Docker container.

## Deploy on Render

1. Create a Render account and connect your GitHub repository.
2. Add a new Web Service.
3. Select `Docker` as the environment.
4. Set the repository to `https://github.com/nofuxgvnwiring-source/MVP` and branch `main`.
5. Set the Dockerfile path to `backend/Dockerfile`.
6. Add required environment variables:
   - `DATABASE_URL`
   - `REDIS_URL`
   - `JWT_SECRET`
   - `BINANCE_SYMBOL`
   - `FREE_SIGNAL_DELAY_SECONDS`
7. Optionally add a managed PostgreSQL and Redis service, then use their connection strings.
8. Set the health check path to `/health`.

Once deployed, use the public Render URL as `NEXT_PUBLIC_API_URL` in your frontend deployment.

## Deploy on Railway

1. Create a Railway project and connect this GitHub repository.
2. Add a service using the `backend` directory and Dockerfile.
3. Add the same environment variables as above.
4. Add PostgreSQL and Redis plugins or use external providers.
5. After deployment, copy the backend service URL and use it in frontend settings.
