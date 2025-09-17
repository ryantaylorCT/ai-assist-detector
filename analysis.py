def analyze_audio(audio_bytes: bytes) -> dict:
    """Simple heuristic to analyze audio bytes and return a score and observations."""
    size = len(audio_bytes)
    # Assign a risk score based on file size thresholds (very naive)
    if size > 2_000_000:
        score = 0.8
        confidence = "High"
    elif size > 500_000:
        score = 0.5
        confidence = "Medium"
    else:
        score = 0.2
        confidence = "Low"

    return {
        "file_size": size,
        "score": score,
        "confidence": confidence,
        "observations": [f"File size is {size} bytes"]
    }
