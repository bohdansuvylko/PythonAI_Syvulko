import logging
import datetime

logging.basicConfig(filename='example.log', level=logging.INFO)

current_date = datetime.datetime.now().strftime("%Y-%m-%d")

logging.info(f"Current date is: {current_date}")