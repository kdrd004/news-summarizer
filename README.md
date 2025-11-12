# 📰 Challenge 2 - Serverless News Summarizer

A full-stack application that summarizes news articles using React, Vite, AWS Lambda, and Hugging Face API.

## 📊 Status

✅ **Backend (AWS Lambda)**: Live and working  
✅ **Frontend (Local)**: Working at localhost:5173  
✅ **CORS**: Fixed and tested  
⏳ **Vercel Deployment**: Ready (see `DEPLOYMENT.md`)

---

## 🧠 Objective

Build a React + Vite frontend that:
1. Takes a news article URL as input
2. Sends it to an AWS Lambda backend
3. Lambda calls the Hugging Face Summarization API
4. Returns a short summary to the frontend

## ⚙️ Tech Stack

| Layer | Tool/Service | Purpose |
|-------|--------------|---------|
| **Frontend** | React + Vite | Fast, modern, Vercel-friendly |
| **HTTP Client** | Axios | API requests |
| **Backend** | AWS Lambda (Python 3.9) | Serverless compute |
| **API Gateway** | AWS API Gateway | Public HTTP endpoint |
| **NLP Model** | Hugging Face (facebook/bart-large-cnn) | Article summarization |
| **Hosting** | Vercel | Frontend deployment |

## 📁 Project Structure

```
challenge2_vite/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── Summarizer.jsx    # Main UI component
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── .env                       # Configuration (UPDATE WITH API URL)
│   └── .env.example
│
├── backend/
│   ├── lambda_function.py         # Lambda handler
│   ├── requirements.txt           # Python dependencies
│   └── README.md                  # Backend setup instructions
│
└── README.md (this file)
```

## 🚀 Quick Start

### 1️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173

### 2️⃣ Backend Setup (AWS Lambda)

See `backend/README.md` for detailed AWS Lambda deployment steps.

### 3️⃣ Configure Frontend with API URL

After deploying Lambda:
1. Copy the API Gateway Invoke URL
2. Update `frontend/.env`:
   ```
   VITE_API_URL=https://your-api-endpoint/summarize
   ```

## 🔑 Prerequisites

- **Node.js** 16+ (for frontend)
- **AWS Account** (for Lambda)
- **Hugging Face API Token** (get one free at https://huggingface.co/settings/tokens)
- **Python 3.9** (for local testing, not required for Lambda)

## 📝 Frontend Features

- ✅ Simple, clean UI with Bootstrap
- ✅ Real-time loading state
- ✅ Error handling with user-friendly messages
- ✅ Enter key support for quick submission
- ✅ Responsive design

## 🔧 Backend Features

- ✅ CORS enabled for cross-origin requests
- ✅ Error handling and logging
- ✅ Timeout protection
- ✅ Integration with Hugging Face API

## 🧪 Testing

### Test Frontend Locally
```bash
cd frontend
npm run dev
# Visit http://localhost:5173
# Note: Will fail without API_URL - that's expected before backend is deployed
```

### Test Lambda with cURL (after deployment)
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"url":"https://www.bbc.com/news/world-67125342"}' \
  https://YOUR_API_ENDPOINT
```

## 📦 Build & Deploy

### Frontend (Vercel)

```bash
# Push to GitHub first
git push origin main

# Go to https://vercel.com
# Import your repository
# Set environment variable: VITE_API_URL = <your-api-endpoint>
# Click Deploy
```

### Backend (AWS Lambda)

See `backend/README.md` for complete deployment guide.

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| "API URL not configured" | Update `frontend/.env` with your Lambda API Gateway URL |
| 401 Unauthorized from Hugging Face | Verify your HF token is correct and set in Lambda env vars |
| CORS error | Ensure API Gateway has CORS enabled (should be by default) |
| Timeout errors | The article fetch or HF API call is taking too long - try with a simpler URL |

## 📚 Learning Resources

- [Vite Documentation](https://vitejs.dev/)
- [AWS Lambda Python Guide](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html)
- [Hugging Face Inference API](https://huggingface.co/docs/api-inference/index)
- [Vercel Deployment](https://vercel.com/docs)

## ✅ Deliverables Checklist

- [ ] AWS Lambda live endpoint (POST)
- [ ] React frontend calling Lambda
- [ ] Uses Hugging Face model (facebook/bart-large-cnn)
- [ ] Deployed frontend on Vercel
- [ ] README documentation
- [ ] Code comments and structure
- [ ] Reflection/Learning notes

## 📖 Next Steps

1. **Deploy Lambda** → Get API URL
2. **Update Frontend .env** → Add API URL
3. **Test Locally** → Run `npm run dev`
4. **Deploy to Vercel** → Push to GitHub and import to Vercel
5. **Test Live** → Share link and test with real articles

## 📄 License

MIT

---

**Built with ❤️ for learning serverless architecture and NLP integration**
