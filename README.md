# Weather Data Automation Script

This script fetches weather data from the OpenWeatherMap API, transforms it, and saves it to a CSV file.

## Prerequisites

-   Python 3.6+
-   An OpenWeatherMap API key (replace `YOUR_API_KEY` in `.env` with your actual key)

## Installation

1.  Clone the repository.
2.  Create a virtual environment: `python -m venv venv`
3.  Activate the virtual environment: `source venv/bin/activate` (or `venv\\Scripts\\activate` on Windows)
4.  Install the dependencies: `pip install -r requirements.txt`

## Usage

1.  Set your OpenWeatherMap API key in the `.env` file.
2.  Run the script: `python scripts/run.py --city CityName --interval 60`

    *   `--city`: The city to fetch weather data for (default: London).
    *   `--interval`: The interval in seconds to run the script (default: 60).

## Project Structure

```
projeto_automacao/
├── .devcontainer/
│   └── devcontainer.json
├── README.md
├── requirements.txt
├── src/
│   └── main.py
├── scripts/
│   └── run.py
```

*   `.devcontainer/`: Configuration for the development environment.
*   `README.md`: This file.
*   `requirements.txt`: List of dependencies.
*   `src/main.py`: Main script to fetch, transform, and save weather data.
*   `scripts/run.py`: Script to run the main script with command-line arguments.
