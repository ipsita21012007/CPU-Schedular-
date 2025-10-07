def sjf_algorithm(processes):
    """Shortest Job First (non-preemptive).

    processes: list of dicts with keys 'id', 'arrival', 'burst'
    """
    procs = [dict(p) for p in processes]
    time = 0
    schedule = []
    waiting_times = {}
    turnaround_times = {}

    # Keep scheduling until all done
    remaining = sorted(procs, key=lambda p: (p.get('arrival', 0), p.get('burst', 0), p.get('id')))
    done = []
    while remaining:
        # get available processes
        available = [p for p in remaining if p.get('arrival', 0) <= time]
        if not available:
            # advance time to next arrival
            time = remaining[0].get('arrival', 0)
            continue
        # pick shortest burst (tie by arrival then id)
        available.sort(key=lambda p: (p.get('burst', 0), p.get('arrival', 0), p.get('id')))
        p = available[0]
        remaining.remove(p)

        pid = p.get('id')
        arrival = int(p.get('arrival', 0))
        burst = int(p.get('burst', 0))
        start = max(time, arrival)
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
        'algorithm': 'SJF',
        'schedule': schedule,
        'waiting_times': waiting_times,
        'turnaround_times': turnaround_times,
        'avg_waiting_time': avg_wait,
        'avg_turnaround_time': avg_turn,
    }
