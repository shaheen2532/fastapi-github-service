from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_api_key
from logger import logger
from functions import fetch_paginated_data, write_to_csv


router = APIRouter()

@router.get("/fetch_repos/{username}/{per_page}/{page}", dependencies=[Depends(get_api_key)])
async def fetch_repos(username: str, per_page: int, page: int):
    try:
        # Fetching paginated data
        repos_data = await fetch_paginated_data(username, per_page, page)
        
        # Writing data to CSV
        write_to_csv(repos_data, f"{username}_repos.csv")
        
        return {"message": f"Data for {username} fetched and written to CSV."}
    
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))