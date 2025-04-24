
from googleapiclient.discovery import build
import os

# Set up your API key and Custom Search Engine ID
api_key = "YOUR_GOOGLE_API_KEY"
cse_id = "YOUR_CSE_ID"

def google_search(query):
    # Build the service
    service = build("customsearch", "v1", developerKey=api_key)
    
    # Perform the search
    res = service.cse().list(q=query, cx=cse_id).execute()
    
    if 'items' in res:
        for item in res['items']:
            print(f"Title: {item['title']}")
            print(f"Link: {item['link']}")
            print(f"Snippet: {item['snippet']}
")
    else:
        print("No results found")

def ai_answer(command):
    # Logic to check if the command should be processed by Google
    if command.lower().startswith("search"):
        query = command[7:]  # Extract the query after "search"
        google_search(query)
    else:
        print("Command not recognized. Try 'search <query>'.")

# Example usage:
if __name__ == "__main__":
    command = input("Enter a command: ")
    ai_answer(command)
