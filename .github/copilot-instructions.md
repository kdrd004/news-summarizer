# Challenge 2 - Serverless News Summarizer

## Project Context

- **Type**: Full-stack web application (React + Vite frontend, AWS Lambda backend)
- **Frontend**: React + Vite with Axios and Bootstrap
- **Backend**: AWS Lambda (Python 3.9) with Hugging Face API integration
- **Deployment**: Frontend on Vercel, Backend on AWS

## Setup Progress

✅ **Completed**:
- Vite React project scaffolded in `frontend/`
- Summarizer component created with error handling
- Bootstrap styling integrated
- Backend Lambda function template created
- Environment configuration setup

## Current State

- **Frontend**: Ready for local development (`npm run dev`)
- **Backend**: Ready for AWS Lambda deployment
- **Integration**: Awaiting API Gateway URL from AWS

## Key Files

| File | Purpose |
|------|---------|
| `frontend/src/components/Summarizer.jsx` | Main React component with API integration |
| `frontend/.env` | Configuration (needs API URL) |
| `backend/lambda_function.py` | AWS Lambda handler |
| `backend/README.md` | Lambda deployment guide |

## Next Steps for User

1. **Deploy Backend to AWS Lambda**
   - Follow instructions in `backend/README.md`
   - Get API Gateway Invoke URL
   - Add Hugging Face token as Lambda env var

2. **Update Frontend Configuration**
   - Copy API URL to `frontend/.env`
   - Test with `npm run dev`

3. **Deploy Frontend to Vercel**
   - Push to GitHub
   - Import repo in Vercel
   - Set `VITE_API_URL` environment variable

## Available Commands

```bash
# Frontend development
cd frontend
npm run dev      # Start dev server (localhost:5173)
npm run build    # Build for production
npm run preview  # Preview production build

# Backend testing (local Python)
python lambda_function.py
```

## Important Notes

- ⚠️ Lambda function needs Hugging Face token in environment variables
- ⚠️ Article text is limited to first 1000 chars to stay under API limits
- ✅ CORS is enabled in API Gateway for cross-origin requests
- ✅ Error handling covers network, API, and parsing failures
