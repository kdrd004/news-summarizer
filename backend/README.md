# AWS Lambda Backend - News Summarizer

## Setup Instructions

1. **Create Lambda Function**
   - Go to AWS Console → Lambda → Create Function
   - Name: `news-summarizer`
   - Runtime: `Python 3.9`
   - Click "Create Function"

2. **Deploy Code**
   - Paste the contents of `lambda_function.py` into the Lambda editor
   - Click "Deploy"

3. **Add Hugging Face API Token**
   - Get your token from https://huggingface.co/settings/tokens
   - In Lambda: Configuration → Environment variables
   - Add: `HUGGINGFACE_TOKEN = <your-token>`
   - Update `lambda_function.py` to use `os.environ.get("HUGGINGFACE_TOKEN")`

4. **Add API Gateway Trigger**
   - Function Overview → Add trigger
   - Service: API Gateway
   - Create new API
   - HTTP API
   - Security: Open
   - Click "Add"
   - Copy the Invoke URL

5. **Test with cURL**
   ```bash
   curl -X POST -H "Content-Type: application/json" \
   -d '{"url":"https://www.bbc.com/news/world-12345"}' \
   https://YOUR_API_ENDPOINT/default/news-summarizer
   ```

## Environment Variables

| Variable | Value | Notes |
|----------|-------|-------|
| `HUGGINGFACE_TOKEN` | Your HF API token | Required for Hugging Face API calls |

## Dependencies

See `requirements.txt` for Python dependencies. AWS Lambda includes `requests` by default in most runtimes.

## Troubleshooting

- **401 Unauthorized**: Check your Hugging Face token is correct
- **Timeout**: Try with a smaller article (< 1000 chars)
- **CORS errors**: Verify API Gateway has proper CORS headers
