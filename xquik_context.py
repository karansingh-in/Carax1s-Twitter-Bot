import json
import os
import urllib.parse
import urllib.request

XQUIK_SEARCH_URL = "https://xquik.com/api/v1/x/tweets/search"


def _context_limit():
    try:
        return int(os.getenv("XQUIK_CONTEXT_LIMIT", "2"))
    except ValueError:
        return 2


def fetch_xquik_context():
    api_key = os.getenv("XQUIK_API_KEY")
    query = os.getenv("XQUIK_SEARCH_QUERY")
    if not api_key or not query:
        return ""

    params = urllib.parse.urlencode({"q": query, "limit": max(1, min(_context_limit(), 5))})
    request = urllib.request.Request(
        f"{XQUIK_SEARCH_URL}?{params}",
        headers={"X-API-Key": api_key, "Accept": "application/json"},
        method="GET",
    )

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except (OSError, json.JSONDecodeError):
        return ""

    tweets = payload.get("data") or payload.get("tweets") or payload.get("results") or []
    snippets = []
    for tweet in tweets:
        if not isinstance(tweet, dict):
            continue
        text = str(tweet.get("text") or tweet.get("content") or "").strip()
        if text:
            snippets.append(" ".join(text.split()))
        if len(snippets) == 2:
            break

    if not snippets:
        return ""

    return "Source context: " + " | ".join(snippets)
