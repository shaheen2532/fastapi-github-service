# FastAPI Paginated API Service

## Overview
This FastAPI application fetches paginated data from APIs that support paging (e.g., GitHub API) and writes the collected data to a CSV file. It handles rate limiting efficiently using asynchronous requests with `httpx`.

Keep in mind, that the github API url is IP-restricted to 60 requests per hour for an IP Address. Rate limiting does help.

## Features
✅ FastAPI backend with **asynchronous HTTP requests** using `httpx`  
✅ Fetches **paginated API data** efficiently  
✅ **Rate Limit Handling** with `asyncio.sleep()` and slowapi   
✅ **CORS Configured** to allow frontend origin  
✅ **Saves API data to CSV** for further analysis  

## Installation
### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/fastapi-api-fetcher.git
```

### **2. Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

## Running the Server
Start the FastAPI server with:
```bash
uvicorn main:app --reload
```

## API Endpoints
### **Fetch Repositories from GitHub (Paginated)**
#### **Endpoint:**
```http
GET /fetch_repos/{username}/{per_page}/{page}
```
#### **Example Request:**
```bash
curl -X GET "http://127.0.0.1:8000/fetch_repos/octocat/2/1" -H "X-API-KEY: your_api_key"
```
#### **Example Response:**
```json
{
    "message": "Data for octocat fetched and saved to octocat_repos.csv.",
    }
}

Data should be saved to a .csv file in the same directory
```

## Configuration & Security
### **CORS Configuration** (Allows all origins)
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
For production, replace `"*"` with specific frontend origins.


## Future Enhancements
- ✅ Support for multiple APIs (e.g., Twitter API)
- ✅ Store data in a database instead of CSV
- ✅ Implement authentication for secure access

## License
This project is open-source and available under the MIT License.
