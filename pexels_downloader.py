import os
import requests
import threading
from dotenv import load_dotenv
from urllib.parse import urlparse
import argparse

# Load environment variables
load_dotenv()
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

if not PEXELS_API_KEY:
    print("Error: PEXELS_API_KEY is not set in the environment.")
    exit(1)

API_BASE_URL = "https://api.pexels.com/v1"
OUTPUT_FOLDER = "downloads"
CONCURRENCY_LIMIT = 5

def fetch_photos(collection_id, page=1, per_page=80):
    """Fetch photos from a Pexels collection."""
    url = f"{API_BASE_URL}/collections/{collection_id}"
    headers = {"Authorization": PEXELS_API_KEY}
    params = {"page": page, "per_page": per_page}

    print(f"Fetching photos from {url} with page={page}, per_page={per_page}...")
    response = requests.get(url, headers=headers, params=params)
    print(f"HTTP Status Code: {response.status_code}")
    if response.status_code != 200:
        print("Error fetching photos:", response.text)
        return None

    return response.json()

def download_image(image_url, output_folder):
    """Download an image from the URL to the output folder."""
    try:
        print(f"Downloading image: {image_url}")
        response = requests.get(image_url, stream=True)
        if response.status_code != 200:
            print(f"Error downloading {image_url}: HTTP {response.status_code}")
            return

        parsed_url = urlparse(image_url)
        filename = os.path.basename(parsed_url.path)
        file_path = os.path.join(output_folder, filename)

        with open(file_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Error downloading {image_url}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Download images from a Pexels collection.")
    parser.add_argument("collection_id", help="The Pexels collection ID")
    parser.add_argument("--output", default=OUTPUT_FOLDER, help="Output folder for images")
    parser.add_argument("--concurrency", type=int, default=CONCURRENCY_LIMIT, help="Number of concurrent downloads")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    print("Fetching photos from the collection...")
    data = fetch_photos(args.collection_id)
    if not data or "media" not in data:  # Updated key name
        print("No photos found or API error.")
        return

    media_items = data["media"]
    print(f"Found {len(media_items)} items in the collection.")

    sem = threading.Semaphore(args.concurrency)
    threads = []

    for item in media_items:
        if item["type"].lower() != "photo":  # Ensure it's a photo
            print(f"Skipping non-photo item: {item}")
            continue

        image_url = item["src"]["original"]  # Use the original size

        def worker(url=image_url):
            with sem:
                download_image(url, args.output)

        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All downloads completed.")

if __name__ == "__main__":
    main()
