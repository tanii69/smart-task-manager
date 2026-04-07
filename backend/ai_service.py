def suggest_priority(title):
    title = title.lower()

    if "exam" in title or "urgent" in title:
        return "High"
    elif "assignment" in title or "project" in title:
        return "Medium"
    else:
        return "Low"