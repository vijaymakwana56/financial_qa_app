import subprocess

def answer_question(query, data):
    # Prepare context
    context = ""
    if "text" in data:
        context = data["text"][:2000]  # limit size for small models
    elif "dataframe" in data:
        context = str(data["dataframe"][:50])  # first 50 rows

    # Call Ollama CLI with local model
    try:
        prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer clearly:"
        result = subprocess.run(
            ["ollama", "run", "llama2"],
            input=prompt.encode("utf-8"),
            capture_output=True
        )
        return result.stdout.decode("utf-8").strip()
    except Exception as e:
        return f"Error: {e}"
