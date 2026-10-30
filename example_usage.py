# -*- coding: utf-8 -*-
from client import GenParkChromeInterceptor

cdp = GenParkChromeInterceptor()

# 1. CDP Priority Queue
reqs = [
    {"request_id": "analytics_ping", "priority": "low", "wait_cycles": 8},
    {"request_id": "checkout_api", "priority": "very_high", "wait_cycles": 1},
    {"request_id": "product_image", "priority": "medium", "wait_cycles": 3}
]
sched = cdp.schedule_network_priority_queue(reqs)
print(f"CDP Request Queue: Top Dispatch='{sched['top_dispatch_request_id']}'")
for r in sched['dispatched_queue']:
    print(f"  {r['request_id']}: EffectivePriority={r['effective_priority']} (Base={r['base_priority']}, Aging={r['aging_bonus']})")

# 2. DOM Tree Edit Distance
dom1 = ["html", "body", "div", "header", "nav", "main", "article", "footer"]
dom2 = ["html", "body", "div", "header", "main", "article", "aside", "footer"]
diff = cdp.calculate_dom_tree_edit_distance(dom1, dom2)
print()
print(f"DOM Edit Distance: Dist={diff['levenshtein_edit_distance']} (Similarity={diff['structural_similarity_ratio']}, {diff['status']})")

# 3. Fingerprint Jitter Synthesis
jitter = cdp.synthesize_fingerprint_jitter(base_delay_ms=300.0, jitter_sigma_ms=50.0, seed=123)
print()
print(f"Anti-Bot Jitter: Delay={jitter['synthesized_delay_ms']}ms (Delta={jitter['jitter_delta_ms']}ms)")
