import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def calculate_waiting_time(queue_length, service_time, counters):

    # Input variables
    queue = ctrl.Antecedent(np.arange(0, 51, 1), "queue")
    service = ctrl.Antecedent(np.arange(1, 11, 1), "service")
    counter = ctrl.Antecedent(np.arange(1, 6, 1), "counter")

    # Output variable
    waiting = ctrl.Consequent(np.arange(0, 121, 1), "waiting")

    # -----------------------------
    # Membership Functions
    # -----------------------------

    # Queue Length
    queue["short"] = fuzz.trimf(queue.universe, [0, 0, 15])
    queue["medium"] = fuzz.trimf(queue.universe, [5, 20, 35])
    queue["long"] = fuzz.trimf(queue.universe, [25, 50, 50])

    # Service Time
    service["fast"] = fuzz.trimf(service.universe, [1, 1, 4])
    service["moderate"] = fuzz.trimf(service.universe, [2, 5, 8])
    service["slow"] = fuzz.trimf(service.universe, [6, 10, 10])

    # Number of Counters
    counter["few"] = fuzz.trimf(counter.universe, [1, 1, 2])
    counter["moderate"] = fuzz.trimf(counter.universe, [1, 3, 4])
    counter["many"] = fuzz.trimf(counter.universe, [3, 5, 5])

    # Waiting Time
    waiting["short"] = fuzz.trimf(waiting.universe, [0, 0, 30])
    waiting["moderate"] = fuzz.trimf(waiting.universe, [15, 45, 75])
    waiting["long"] = fuzz.trimf(waiting.universe, [60, 120, 120])

    # -----------------------------
    # Fuzzy Rules
    # -----------------------------

    rule1 = ctrl.Rule(
        queue["short"] & service["fast"],
        waiting["short"]
    )

    rule2 = ctrl.Rule(
        queue["medium"] & service["moderate"],
        waiting["moderate"]
    )

    rule3 = ctrl.Rule(
        queue["long"] & service["slow"] & counter["few"],
        waiting["long"]
    )

    rule4 = ctrl.Rule(
        queue["long"] & counter["few"],
        waiting["long"]
    )

    rule5 = ctrl.Rule(
        queue["short"] & counter["many"],
        waiting["short"]
    )

    rule6 = ctrl.Rule(
        queue["medium"] & counter["moderate"],
        waiting["moderate"]
    )

    rule7 = ctrl.Rule(
        queue["long"] & counter["many"],
        waiting["moderate"]
    )

    # -----------------------------
    # Fuzzy Control System
    # -----------------------------

    waiting_control = ctrl.ControlSystem([
        rule1,
        rule2,
        rule3,
        rule4,
        rule5,
        rule6,
        rule7
    ])

    waiting_simulation = ctrl.ControlSystemSimulation(
        waiting_control
    )

    # Give input values
    waiting_simulation.input["queue"] = queue_length
    waiting_simulation.input["service"] = service_time
    waiting_simulation.input["counter"] = counters

    # Fuzzification + Rule Evaluation + Defuzzification
    waiting_simulation.compute()

    result = waiting_simulation.output["waiting"]

    return round(result, 2)