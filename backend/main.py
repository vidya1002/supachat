from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Enable CORS (so frontend can connect)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🧠 Simple NL → SQL logic (for later use)
def generate_sql(query: str):
    query = query.lower()

    if "top trending topics" in query:
        return """
        SELECT topic, SUM(views) as total_views
        FROM articles
        GROUP BY topic
        ORDER BY total_views DESC;
        """

    elif "compare engagement" in query:
        return """
        SELECT topic, AVG(likes) as avg_likes
        FROM articles
        GROUP BY topic;
        """

    elif "daily views" in query:
        return """
        SELECT DATE(created_at), SUM(views)
        FROM articles
        GROUP BY DATE(created_at)
        ORDER BY DATE(created_at);
        """

    return "SELECT * FROM articles LIMIT 5;"


# ✅ API: Query endpoint (dummy response for now)
from pydantic import BaseModel

class QueryRequest(BaseModel):
    user_query: str


@app.post("/query")
def query_db(request: QueryRequest):
    sql = generate_sql(request.user_query)

    return {
        "query": request.user_query,
        "generated_sql": sql,
        "data": [
            {"message": "Backend is working 🚀"},
            {"note": "Database will be connected next step"}
        ]
    }


# ✅ Health check endpoint
@app.get("/health")
def health():
    return {"status": "ok"}