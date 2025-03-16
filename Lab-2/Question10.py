# Implement an exponential backoff strategy that doubles the wait time between retries,
# starting from 1  second, but stops after 5 retries.
import time
import random

MAX_RETRIES = 5
INITIAL_WAIT_TIME = 1  # Start with 1 second

for attempt in range(1, MAX_RETRIES + 1):
    try:
        # Simulate an operation (replace with actual logic)
        print(f"Attempt {attempt}: Trying...")
        if random.random() < 0.7:  # Simulate a 70% failure rate
            raise Exception("Operation failed")
        
        print("Operation succeeded!")
        break  # Exit loop if successful
    
    except Exception as e:
        print(e)
        if attempt < MAX_RETRIES:
            wait_time = INITIAL_WAIT_TIME * (2 ** (attempt - 1))  # Exponential backoff
            print(f"Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        else:
            print("Max retries reached. Giving up.")
