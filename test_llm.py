from dotenv import load_dotenv

from llm_parser import parse_queue_input
from fuzzy_system import calculate_waiting_time


# Load environment variables
load_dotenv()


# Natural-language queue input
text = (
    "There are around 20 people waiting, "
    "2 counters are open and each person takes about 4 minutes."
)


# Step 1: LLM extracts queue information
queue_data = parse_queue_input(text)

print("Extracted Queue Information:")
print(queue_data)


# Step 2: Send LLM output to Fuzzy Logic System
waiting_time = calculate_waiting_time(
    queue_data["queue_length"],
    queue_data["service_time"],
    queue_data["counters"]
)


# Final fuzzy result
print("\nFuzzy Estimated Waiting Time:")
print(f"{waiting_time} minutes")