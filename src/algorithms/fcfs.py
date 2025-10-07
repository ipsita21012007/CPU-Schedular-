def fcfs_algorithm(processes):
    """First-Come-First-Serve scheduling.

    processes: list of dicts with keys 'id', 'arrival', 'burst'
    Returns a dict with schedule order, start/finish times and metrics.
    """
    # Sort by arrival then id
    procs = sorted(processes, key=lambda p: (p.get('arrival', 0), p.get('id')))
    time = 0
    schedule = []
    waiting_times = {}
    turnaround_times = {}

    for p in procs:
        pid = p.get('id')
        arrival = int(p.get('arrival', 0))
        burst = int(p.get('burst', 0))
        if time < arrival:
            time = arrival
        start = time
        finish = start + burst
        waiting = start - arrival
        turnaround = finish - arrival

        schedule.append({'id': pid, 'start': start, 'finish': finish, 'burst': burst, 'arrival': arrival})
        waiting_times[pid] = waiting
        turnaround_times[pid] = turnaround

        time = finish

    avg_wait = sum(waiting_times.values()) / len(waiting_times) if waiting_times else 0
    avg_turn = sum(turnaround_times.values()) / len(turnaround_times) if turnaround_times else 0

    return {
        'algorithm': 'FCFS',
        'schedule': schedule,
        'waiting_times': waiting_times,
        'turnaround_times': turnaround_times,
        'avg_waiting_time': avg_wait,
        'avg_turnaround_time': avg_turn,
    }
