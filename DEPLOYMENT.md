# 🚀 Deployment Guide

## Frontend (Vercel)

### Prerequisites
- GitHub account
- Vercel account (free tier works great)
- Your code pushed to GitHub

### Steps

1. **Push to GitHub**
   ```bash
   cd challenge2_vite
   git add .
   git commit -m "Ready for deployment"
   git push
   ```

2. **Go to Vercel**: https://vercel.com/new

3. **Import Repository**
   - Click "Import Project"
   - Select your GitHub repo (e.g., `challenge2-news-summarizer`)
   - Click "Import"

4. **Configure**
   - **Root Directory**: `frontend`
   - **Framework Preset**: `Vite`
   - **Build Command**: `npm run build` (default)
   - **Output Directory**: `dist` (default)

5. **Add Environment Variables**
   - Click "Environment Variables"
   - Add:
     ```
     Name: VITE_API_URL
     Value: https://99w08kund7.execute-api.eu-north-1.amazonaws.com/default/news-summarizer
     ```
   - Click "Deploy"

6. **Done!**
   - Vercel will build and deploy
   - You'll get a live URL like: `https://challenge2-news-summarizer.vercel.app`
   - Share this link!

---

## Backend (AWS Lambda) — Already Deployed ✅

Your Lambda function and API Gateway are already live:
- **Lambda**: `news-summarizer` (Python 3.9)
- **API Gateway**: `https://99w08kund7.execute-api.eu-north-1.amazonaws.com/default/news-summarizer`
- **CORS**: ✅ Configured

### To update Lambda code later:
1. Edit `backend/lambda_function.py` locally
2. Copy the code to AWS Lambda console
3. Click "Deploy"

---

## Testing the Live App

Once deployed to Vercel:
1. Open your Vercel URL
2. Paste a news article URL (e.g., Wikipedia article)
3. Click "Summarize"
4. See the summary appear below

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Build fails on Vercel | Check that Root Directory is set to `frontend` |
| CORS errors in prod | Verify `VITE_API_URL` env var is set correctly in Vercel |
| Blank page | Check browser console (F12) for errors |
| Lambda timeout | Some articles take time to fetch; Hugging Face may be slow |

---

## Optional: Set up automatic deploys

Vercel automatically redeploys when you push to main. To disable:
- Go to Vercel project settings → Git → uncheck "Production Deployments"

---

## Next Steps After Deployment

1. **Share the live link** with others
2. **Test with different URLs** (Wikipedia, news sites, blogs)
3. **Monitor costs**:
   - Vercel free tier: ✅ (generous)
   - AWS Lambda free tier: ✅ (1M requests/month)
   - Hugging Face free tier: ✅ (rate-limited but fine for learning)

Enjoy! 🎉
