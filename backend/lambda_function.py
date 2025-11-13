import json
import os
import urllib.request
import urllib.error
import ssl
import re

def cors_headers():
    """Return CORS headers for responses"""
    return {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Authorization",
        "Content-Type": "application/json"
    }


def lambda_handler(event, context):
    """
    AWS Lambda handler for news article summarization.
    
    Expected input (POST body):
    {
        "url": "https://example.com/article"
    }
    
    Returns:
    {
        "statusCode": 200,
        "body": {
            "summary": "..."
        }
    }
    """
    # Handle CORS preflight requests
    if event.get("requestContext", {}).get("http", {}).get("method") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": cors_headers(),
            "body": ""
        }
    
    try:
        body = json.loads(event.get("body", "{}"))
        url = body.get("url")
        
        if not url:
            return {
                "statusCode": 400,
                "headers": cors_headers(),
                "body": json.dumps({"error": "Missing URL"})
            }

        print(f"Fetching and cleaning article from: {url}")
        try:
            
            import urllib.parse

            # Use Jina AI proxy to extract clean article text automatically
            text_api_url = f"https://r.jina.ai/{url}"  # Jina AI proxy extracts readable text
            print(f"Fetching cleaned text from: {text_api_url}")
            req = urllib.request.Request(text_api_url, headers={"User-Agent": "Mozilla/5.0"})
            context_ssl = ssl.create_default_context()
            with urllib.request.urlopen(req, timeout=10, context=context_ssl) as resp:
                clean_text = resp.read().decode("utf-8", errors="ignore")
            article_text = re.sub(r"\s+", " ", clean_text).strip()[:1000]

        except Exception as e:
            print(f"Error fetching article: {e}")
            return {

                "statusCode": 400,
                "headers": cors_headers(),
                "body": json.dumps({"error": f"Failed to fetch article: {str(e)}"})
            }


        # Call Hugging Face Summarization API using urllib (no external deps)
        api_url = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"

        hf_token = os.environ.get("HUGGINGFACE_TOKEN")
        if not hf_token:
            return {
                "statusCode": 500,
                "headers": cors_headers(),
                "body": json.dumps({"error": "HUGGINGFACE_TOKEN not found in environment variables"})
            }

        payload = json.dumps({"inputs": article_text}).encode("utf-8")
        hf_req = urllib.request.Request(
            api_url,
            data=payload,
            headers={
                "Authorization": f"Bearer {hf_token}",
                "Content-Type": "application/json"
            },
            method="POST"
        )

        try:
            with urllib.request.urlopen(hf_req, timeout=30, context=ssl.create_default_context()) as hf_resp:
                resp_text = hf_resp.read().decode("utf-8", errors="ignore")
                data = json.loads(resp_text)
        except urllib.error.HTTPError as he:
            err_body = he.read().decode("utf-8", errors="ignore")
            print(f"Hugging Face HTTP error: {he.code} - {err_body}")
            return {
                "statusCode": 502,
                "headers": cors_headers(),
                "body": json.dumps({"error": f"Hugging Face API error: {he.code}", "details": err_body})
            }
        except Exception as e:
            print(f"Error calling Hugging Face API: {e}")
            return {
                "statusCode": 502,
                "headers": cors_headers(),
                "body": json.dumps({"error": f"Failed to call Hugging Face API: {str(e)}"})
            }

        # Parse response
        try:
            if isinstance(data, list) and len(data) > 0:
                summary = data[0].get("summary_text", "No summary returned")
            elif isinstance(data, dict):
                summary = data.get("summary_text", "No summary returned")
            else:
                summary = "No summary returned"
        except Exception as e:
            print(f"Error parsing HF response: {e}")
            summary = "No summary returned"

        return {
            "statusCode": 200,
            "headers": cors_headers(),
            "body": json.dumps({"summary": summary})
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "headers": cors_headers(),
            "body": json.dumps({"error": str(e)})
        }

AWS_SECRET_ACCESS_KEY = "AKIA1234567890ABCDEFGHI"

