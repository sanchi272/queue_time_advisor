import streamlit as st

from llm_parser import parse_queue_input
from fuzzy_system import calculate_waiting_time


# Page settings
st.set_page_config(
    page_title="Smart Queue Waiting Time Advisor",
    page_icon="⏳",
    layout="centered"
)


# Title
st.title("⏳ Smart Queue Waiting Time Advisor")

st.write(
    "Describe your queue in simple language and get an estimated waiting time."
)


# User input
user_input = st.text_area(
    "Describe your queue:",
    placeholder=(
        "Example: There are around 20 people waiting, "
        "2 counters are open and each person takes about 4 minutes."
    )
)


# Button
if st.button("Estimate Waiting Time"):

    if user_input.strip() == "":
        st.warning("Please describe the queue first.")

    else:

        with st.spinner("Analyzing queue..."):

            # Step 1: LangChain + Gemini
            queue_data = parse_queue_input(user_input)

            # Step 2: Fuzzy Logic
            waiting_time = calculate_waiting_time(
                queue_data["queue_length"],
                queue_data["service_time"],
                queue_data["counters"]
            )


        # Extracted information
        st.subheader("📊 Queue Information")

        st.write(
            f"**People waiting:** {queue_data['queue_length']}"
        )

        st.write(
            f"**Service time:** {queue_data['service_time']} minutes/person"
        )

        st.write(
            f"**Active counters:** {queue_data['counters']}"
        )


        # Final result
        st.subheader("⏱️ Estimated Waiting Time")

        st.success(
            f"Approximately {waiting_time} minutes"
        )