# Pexels Image Downloader

A simple command-line tool to download images from a Pexels collection using the Pexels API. This tool allows you to specify a collection ID and download images concurrently.

## Setup Instructions

### Prerequisites
1. Python 3.x
2. `requests` library for HTTP requests.
3. `python-dotenv` for managing environment variables.

### Installation

1. **Clone the Repository** (or download the script):
    ```
    git clone https://github.com/ygohel18/pexels-downloader.git
    cd pexels-downloader
    ```

2. **Install Dependencies**:
- Install the required Python packages using `pip`:
  ```
  pip install -r requirements.txt
  ```

3. **Create a `.env` File**:
- Create a `.env` file in the project directory with your Pexels API key:
  ```
  PEXELS_API_KEY=your_api_key_here
  ```

- You can get your API key from [Pexels API](https://www.pexels.com/api/).

### Configuration
- The script uses the `.env` file to load the API key.
- By default, the images will be downloaded to a folder named `downloads`. You can specify a different folder using the `--output` flag.
- You can control the number of concurrent downloads with the `--concurrency` flag.

## Usage

To download images from a Pexels collection, run the script with the following command:
  ```
  python pexels_downloader.py <collection_id> --output <folder_name> --concurrency <number_of_concurrent_downloads>
  ```

### Arguments
- `collection_id`: The unique ID of the Pexels collection (found in the URL of the collection page).
- `--output <folder_name>`: Optional flag to specify the folder to save the images (default is `downloads`).
- `--concurrency <number_of_concurrent_downloads>`: Optional flag to set the number of concurrent downloads (default is 5).

### Example

1. **Download images from the collection `ritss5w`**:

  ```
  python pexels_downloader.py ritss5w --output downloads --concurrency 5
  ```


This command will:
- Download images from the collection with the ID `ritss5w`.
- Save the images to the `downloads` folder.
- Download up to 5 images concurrently.

## Notes
- Ensure your API key is valid and has not exceeded its usage limits.
- If you encounter issues with the script, check the logs for any error messages.