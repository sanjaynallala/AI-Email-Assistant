import heapq

class EmailItem:
    def __init__(self, priority_score, email_row):
        self.priority_score = priority_score  # higher => processed earlier
        self.email_row = email_row

    def __lt__(self, other):
        # invert for max-heap behavior
        return self.priority_score > other.priority_score

def build_priority_queue(email_df, scoring_fn):
    heap = []
    for _, row in email_df.iterrows():
        score = scoring_fn(row)  # numeric priority
        heapq.heappush(heap, EmailItem(score, row))
    return heap

def pop_all(heap):
    ordered = []
    while heap:
        item = heapq.heappop(heap)
        ordered.append(item.email_row)
    return ordered
