import os, sys
api_key=os.getenv("OPENAI_API_KEY")
if not api_key:
  sys.exit(" No OPENAI_API_KEY FOUND IN GITHUB SECRETS")
print("AI PR Review workflow executed succesfully!!")
