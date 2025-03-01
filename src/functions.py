import pandas as pd
import httpx
import requests
from typing import List
from fastapi import HTTPException
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

API = os.getenv("GITHUB_API_URL")

async def fetch_paginated_data(username: str) -> List[dict]:
    all_repos = []
    page = 1

    async with httpx.AsyncClient() as client:
        while True:
            # Making request with pagination
            response = requests.get(API.format(username=username), params={"page": page, "per_page": 30})
            
            if response.status_code == 403 and "X-RateLimit-Remaining" in response.headers:
                reset_time = int(response.headers.get("X-RateLimit-Reset", 0))
                sleep_time = max(reset_time - asyncio.get_event_loop().time(), 0)

                print(f"Rate limit exceeded. Sleeping for {sleep_time:.2f} seconds...")
                await asyncio.sleep(sleep_time + 1)  # Adding 1 second buffer
                continue  # Retry the request

            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail="Error fetching data from GitHub")
            
            repos = response.json()
            
            if not repos:
                break

            all_repos.extend(repos)
            page += 1
    
    return all_repos

def write_to_csv(data: List[dict], filename: str):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)