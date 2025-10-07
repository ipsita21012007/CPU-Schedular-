from collections import deque


def round_robin_algorithm(processes, quantum):
    """Round Robin scheduling.

    processes: list of dicts with keys 'id', 'arrival', 'burst'
    quantum: time quantum (int)
    """
    procs = sorted([dict(p) for p in processes], key=lambda p: (p.get('arrival', 0), p.get('id')))
    time = 0
    queue = deque()
    schedule = []
    waiting_times = {}
    turnaround_times = {}

    # map id -> remaining
    rem = {p['id']: int(p.get('burst', 0)) for p in procs}
    arrivals = list(procs)

    # push first arrivals at time 0
    while arrivals or queue:
        # enqueue arrivals at current time
        while arrivals and arrivals[0].get('arrival', 0) <= time:
            queue.append(arrivals.pop(0))

        if not queue:
            # jump to next arrival
            if arrivals:
                time = arrivals[0].get('arrival', 0)
                continue
            else:
                break

        p = queue.popleft()
        pid = p.get('id')
        arrival = int(p.get('arrival', 0))
        r = rem.get(pid, 0)
        start = time
        run = min(int(quantum), r)
        finish = start + run

        # record schedule slice
        schedule.append({'id': pid, 'start': start, 'finish': finish, 'burst': run, 'arrival': arrival})

        time = finish
        rem[pid] = r - run

        # enqueue any newly arrived processes during this quantum
        while arrivals and arrivals[0].get('arrival', 0) <= time:
            queue.append(arrivals.pop(0))

        # if current process still has remaining, requeue it
        if rem[pid] > 0:
            # preserve arrival for fairness
            queue.append({'id': pid, 'arrival': arrival, 'burst': rem[pid]})
        else:
            # finished; compute waiting and turnaround
            finish_time = time
            turnaround = finish_time - arrival
            waiting = turnaround - int(p.get('burst', 0))
            turnaround_times[pid] = turnaround
            waiting_times[pid] = waiting

    avg_wait = sum(waiting_times.values()) / len(waiting_times) if waiting_times else 0
    avg_turn = sum(turnaround_times.values()) / len(turnaround_times) if turnaround_times else 0

    return {
        'algorithm': 'Round Robin',
        'quantum': quantum,
        'schedule': schedule,
        'waiting_times': waiting_times,
        'turnaround_times': turnaround_times,
        'avg_waiting_time': avg_wait,
        'avg_turnaround_time': avg_turn,
    }
