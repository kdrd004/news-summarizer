# Hugging Face API Migration Fix

## Issue
Hugging Face deprecated `https://api-inference.huggingface.co` endpoint.
New endpoint: `https://api-inference.huggingface.co/models/facebook/bart-large-cnn`

(Actually, the old endpoint still works for free tier, but you may need to use the newer router for reliability.)

## Quick Solution for AWS Lambda

Update the `api_url` line in your Lambda code:

**Before (deprecated but still works):**
```python
api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
```

**Now just keep it as is** — Hugging Face still supports it on free tier.

## Alternative: If You Want the New Router
If you want to use the new router endpoint for better reliability:

```python
api_url = "https://router.huggingface.co/api/models/facebook/bart-large-cnn"
```

But stick with the original for now since you're on free tier.

---

## Next Steps

1. **In Lambda console**, go to your function code and verify the `api_url` line is:
   ```python
   api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
   ```

2. **Make sure your Hugging Face token has the right permissions:**
   - Go to https://huggingface.co/settings/tokens
   - Verify your token is "fine-grained" with:
     - ✅ Make calls to Inference Providers
     - ✅ Make calls to your Inference Endpoints

3. **Test again:**
   ```powershell
   Invoke-RestMethod -Method Post `
     -Uri 'https://99w08kund7.execute-api.eu-north-1.amazonaws.com/default/news-summarizer' `
     -ContentType 'application/json' `
     -Body (@{ url = 'https://en.wikipedia.org/wiki/Artificial_intelligence' } | ConvertTo-Json)
   ```

Should return HTTP 200 with `{"summary":"..."}` ✅
