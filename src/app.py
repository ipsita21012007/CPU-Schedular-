import streamlit as st
from algorithms.fcfs import fcfs_algorithm
from algorithms.sjf import sjf_algorithm
from algorithms.round_robin import round_robin_algorithm
import json


def main():
    """Streamlit app entrypoint for the CPU Scheduler Simulator."""
    st.title("CPU Scheduler Simulator")

    algorithm = st.selectbox(
        "Select Algorithm",
        ("FCFS", "SJF", "Round Robin")
    )

    process_input = st.text_area(
        "Enter Processes as JSON",
        '[{"id":1,"arrival":0,"burst":5},{"id":2,"arrival":2,"burst":3}]'
    )

    processes = []
    try:
        processes = json.loads(process_input)
    except Exception:
        st.error("Invalid process list format. Use proper JSON.")

    quantum = None
    if algorithm == "Round Robin":
        quantum = st.number_input("Enter Quantum", min_value=1, value=2)

    if st.button("Simulate"):
        if processes:
            if algorithm == "FCFS":
                result = fcfs_algorithm(processes)
            elif algorithm == "SJF":
                result = sjf_algorithm(processes)
            elif algorithm == "Round Robin":
                if not quantum:
                    st.warning("Please enter a valid quantum.")
                    return
                else:
                    result = round_robin_algorithm(processes, int(quantum))
            st.write("Simulation Result:")
            st.json(result)
        else:
            st.warning("Please enter valid process data.")


if __name__ == "__main__":
    main()
