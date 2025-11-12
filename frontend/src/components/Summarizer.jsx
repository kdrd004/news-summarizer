import React, { useState } from "react";

function Summarizer() {
  const [url, setUrl] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const summarize = async () => {
    if (!url) {
      setError("Please enter a news URL first!");
      return;
    }
    setError("");
    setLoading(true);
    setSummary("");

    try {
      const apiUrl = import.meta.env.VITE_API_URL;
      if (!apiUrl) {
        throw new Error("API URL not configured. Check .env file.");
      }

      const res = await fetch(apiUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ url })
      });

      if (!res.ok) {
        const errorData = await res.json();
        throw new Error(errorData.error || `HTTP ${res.status}: ${res.statusText}`);
      }

      const data = await res.json();
      setSummary(data.summary);
    } catch (err) {
      console.error(err);
      setError(err.message || "Failed to summarize article. Check console or verify the URL is accessible.");
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !loading) {
      summarize();
    }
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-8">
          <h1 className="mb-4 text-center">📰 News Summarizer</h1>
          
          <div className="card">
            <div className="card-body">
              <input
                type="text"
                className="form-control mb-3"
                placeholder="Paste a news article URL (e.g., https://www.bbc.com/news/...)"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                onKeyPress={handleKeyPress}
                disabled={loading}
              />
              <button
                className="btn btn-success btn-lg w-100"
                onClick={summarize}
                disabled={loading}
              >
                {loading ? (
                  <>
                    <span className="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
                    Summarizing...
                  </>
                ) : (
                  "📝 Summarize"
                )}
              </button>
            </div>
          </div>

          {error && (
            <div className="alert alert-danger mt-4 alert-dismissible fade show" role="alert">
              <strong>Error:</strong> {error}
              <button
                type="button"
                className="btn-close"
                onClick={() => setError("")}
              ></button>
            </div>
          )}

          {summary && (
            <div className="alert alert-info mt-4" role="alert">
              <h5>Summary:</h5>
              <p className="mb-0">{summary}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default Summarizer;
