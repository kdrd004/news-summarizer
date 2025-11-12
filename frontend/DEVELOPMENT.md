# Frontend Development

## Start Development Server
```bash
cd frontend
npm run dev
```
Opens at http://localhost:5173

## Build for Production
```bash
npm run build
npm run preview
```

## Project Setup Complete ✅

Your Vite React frontend is ready with:
- ✅ Bootstrap CSS framework
- ✅ Axios for HTTP requests
- ✅ Summarizer component
- ✅ Error handling and loading states
- ✅ Responsive design

## Important: Configure API URL

Before running locally, update `frontend/.env`:

```env
VITE_API_URL=https://YOUR_API_GATEWAY_URL/summarize
```

Get this URL from your AWS Lambda API Gateway after deployment.
