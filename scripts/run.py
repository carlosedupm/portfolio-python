
import time
import schedule
from src.main import job  # Import the job function from src/main.py
import argparse
import os
from dotenv import load_dotenv


def main():
    parser = argparse.ArgumentParser(
        description="Fetch and save weather data.")
    parser.add_argument("--city", type=str, default="London",
                        help="City to fetch weather data for.")
    parser.add_argument("--interval", type=int, default=60,
                        help="Interval in seconds to run the script.")

    args = parser.parse_args()

    load_dotenv()

    # Schedule the job with the city argument
    schedule.every(args.interval).seconds.do(job, city=args.city)

    print(
        f"Fetching weather data for {args.city} every {args.interval} seconds.")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
