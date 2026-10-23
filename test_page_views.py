import json
from supabase import create_client

with open("config.public.json") as f:
    config = json.load(f)

supabase = create_client(
    config["SUPABASE_URL"],
    config["SUPABASE_ANON_KEY"]
)

result = (
    supabase
    .table("sentence_embeddings")
    .select("id, title, speaker, text")
    .limit(10)
    .execute()
)

print(f"Retrieved {len(result.data)} sentence embeddings:")
for row in result.data:
    print(row)