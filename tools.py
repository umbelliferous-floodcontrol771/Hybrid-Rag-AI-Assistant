import wikipedia


def wikipedia_tool(query):

    try:
        summary = wikipedia.summary(query, sentences=3)
        return summary
    except:
        return "Wikipedia could not find relevant information."