from fuzzy_system import calculate_waiting_time

result = calculate_waiting_time(
    queue_length=20,
    service_time=4,
    counters=2
)

print("Estimated Waiting Time:", result, "minutes")