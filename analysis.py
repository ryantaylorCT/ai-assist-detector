def analyze_audio(audio_bytes: bytes) -> dict:
    """
    Analyze audio bytes and return a risk score, confidence level,
    and observations based on simple heuristics.
    """
    size = len(audio_bytes)

    # Determine risk score, confidence and observations based on size thresholds
    if size >= 2_000_000:
        score = 0.9
        confidence = "High"
        observations = [
            "Large audio file suggests long conversation or potential pauses.",
            "Extended pauses or delays might indicate use of AI assistance.",
            "Content appears verbose; could be reading off a script or AI output.",
            "Potentially inconsistent speech rate across segments.",
            "Check for overly generic phrasing or spikes in jargon density."
        ]
    elif size >= 1_000_000:
        score = 0.6
        confidence = "Medium"
        observations = [
            "Moderate audio length; some pauses may be present.",
            "Look for occasional delays before answers.",
            "Language may contain a mix of specific and generic phrasing.",
            "Watch for segments that suddenly become more sophisticated.",
            "Overall risk is moderate based on size alone."
        ]
    else:
        score = 0.3
        confidence = "Low"
        observations = [
            "Shorter audio suggests fewer opportunities for AI assistance.",
            "Minimal evidence of long pauses based on file size.",
            "Likely concise responses with less verbosity.",
            "Less chance of sudden spikes in jargon density.",
            "Overall risk is low based on file size."
        ]

    return {
        "file_size": size,
        "risk_score": round(score, 2),
        "confidence": confidence,
        "observations": observations
    }

    #size = len(audio_bytes)
    # Assign a risk score based on file size thresholds (very naive)
   ## if size > 2_000_000:
    }

    def analyze_audio(audio_bytes: bytes) -> dict:
    """
    Analyze audio bytes and return a risk score, confidence level,
    and observations based on simple heuristics.
    """
    size = len(audio_bytes)
    if size >= 2_000_000:
        score = 0.9
        confidence = "High"
        observations = [
            "Large audio file suggests long conversation or potential pauses.",
            "Extended pauses or delays might indicate use of AI assistance.",
            "Content appears verbose; could be reading off a script or AI output.",
            "Potentially inconsistent speech rate across segments.",
            "Check for overly generic phrasing or spikes in jargon density."
        ]
    elif size >= 1_000_000:
        score = 0.6
        confidence = "Medium"
        observations = [
            "Moderate audio length; some pauses may be present.",
            "Look for occasional delays before answers.",
            "Language may contain a mix of specific and generic phrasing.",
            "Watch for segments that suddenly become more sophisticated.",
            "Overall risk is moderate based on size alone."
        ]
    else:
        score = 0.3
        confidence = "Low"
        observations = [
            "Shorter audio suggests fewer opportunities for AI assistance.",
            "Minimal evidence of long pauses based on file size.",
            "Likely concise responses with less verbosity.",
            "Less chance of sudden spikes in jargon density.",
            "Overall risk is low based on file size."
        ]
    return {
        "file_size": size,
        "risk_score": round(score, 2),
        "confidence": confidence,
        "observations": observations
    }
