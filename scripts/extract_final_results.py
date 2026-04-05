from pathlib import Path
import csv

PROJECT_DIR = Path("/Users/guimeyer/Importantes/Faculdade/5º período/AC3/gem5-memory-hierarchy-study")
RAW_DIR = PROJECT_DIR / "results" / "raw"
OUT_CSV = PROJECT_DIR / "results" / "tables" / "final_summary.csv"

SCENARIOS = [
    ("l1_size", "matmul_l1_16k"),
    ("l1_size", "matmul_l1_32k"),
    ("l1_size", "matmul_l1_64k"),
    ("l2_size", "matmul_l2b_32k"),
    ("l2_size", "matmul_l2b_64k"),
    ("l2_size", "matmul_l2b_128k"),
    ("l2_size", "matmul_l2b_256k"),
    ("memory_cfg", "matmul_mem_ddr3_1600"),
    ("memory_cfg", "matmul_mem_ddr3_2133"),
    ("memory_cfg", "matmul_mem_ddr4_2400"),
    ("l1d_assoc", "matmul_assoc_l1d2"),
    ("l1d_assoc", "matmul_assoc_l1d4"),
    ("l1d_assoc", "matmul_assoc_l1d8"),
]

BASELINES = {
    "matmul_l1_16k": "matmul_l1_16k",
    "matmul_l1_32k": "matmul_l1_16k",
    "matmul_l1_64k": "matmul_l1_16k",
    "matmul_l2b_32k": "matmul_l2b_32k",
    "matmul_l2b_64k": "matmul_l2b_32k",
    "matmul_l2b_128k": "matmul_l2b_32k",
    "matmul_l2b_256k": "matmul_l2b_32k",
    "matmul_mem_ddr3_1600": "matmul_mem_ddr3_1600",
    "matmul_mem_ddr3_2133": "matmul_mem_ddr3_1600",
    "matmul_mem_ddr4_2400": "matmul_mem_ddr3_1600",
    "matmul_assoc_l1d2": "matmul_assoc_l1d2",
    "matmul_assoc_l1d4": "matmul_assoc_l1d2",
    "matmul_assoc_l1d8": "matmul_assoc_l1d2",
}

def read_stats(path: Path):
    stats = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        left = line.split("#", 1)[0].strip()
        parts = left.split()
        if len(parts) >= 2:
            name = parts[0]
            value = parts[1]
            try:
                stats[name] = float(value)
            except ValueError:
                pass
    return stats

def ratio(hits, misses):
    total = hits + misses
    return (misses / total) if total else 0.0

def mpki(misses, sim_insts):
    return (misses / (sim_insts / 1000.0)) if sim_insts else 0.0

all_stats = {}

for _, scenario in SCENARIOS:
    stats_file = RAW_DIR / scenario / "stats.txt"
    if not stats_file.exists():
        print(f"Aviso: {scenario} não encontrado, pulando.")
        continue
    all_stats[scenario] = read_stats(stats_file)

rows = []

for experiment, scenario in SCENARIOS:
    if scenario not in all_stats:
        continue

    s = all_stats[scenario]
    sim_insts = s.get("simInsts", 0.0)
    num_cycles = s.get("board.processor.cores.core.numCycles", 0.0)
    ipc = s.get("board.processor.cores.core.ipc", 0.0)
    cpi = s.get("board.processor.cores.core.cpi", 0.0)

    l1d_hits = s.get("board.cache_hierarchy.l1d-cache-0.overallHits::total", 0.0)
    l1d_misses = s.get("board.cache_hierarchy.l1d-cache-0.overallMisses::total", 0.0)

    l1i_hits = s.get("board.cache_hierarchy.l1i-cache-0.overallHits::total", 0.0)
    l1i_misses = s.get("board.cache_hierarchy.l1i-cache-0.overallMisses::total", 0.0)

    l2_hits = s.get("board.cache_hierarchy.l2-cache-0.overallHits::total", 0.0)
    l2_misses = s.get("board.cache_hierarchy.l2-cache-0.overallMisses::total", 0.0)

    baseline_name = BASELINES[scenario]
    baseline_cycles = all_stats[baseline_name].get("board.processor.cores.core.numCycles", 0.0)
    speedup = (baseline_cycles / num_cycles) if num_cycles else 0.0

    rows.append({
        "experiment": experiment,
        "scenario": scenario,
        "baseline": baseline_name,
        "simInsts": int(sim_insts),
        "numCycles": int(num_cycles),
        "ipc": round(ipc, 6),
        "cpi": round(cpi, 6),
        "speedup": round(speedup, 6),
        "l1d_hits": int(l1d_hits),
        "l1d_misses": int(l1d_misses),
        "l1d_miss_rate": round(ratio(l1d_hits, l1d_misses), 6),
        "l1d_mpki": round(mpki(l1d_misses, sim_insts), 6),
        "l1i_hits": int(l1i_hits),
        "l1i_misses": int(l1i_misses),
        "l1i_miss_rate": round(ratio(l1i_hits, l1i_misses), 6),
        "l1i_mpki": round(mpki(l1i_misses, sim_insts), 6),
        "l2_hits": int(l2_hits),
        "l2_misses": int(l2_misses),
        "l2_miss_rate": round(ratio(l2_hits, l2_misses), 6),
        "l2_mpki": round(mpki(l2_misses, sim_insts), 6),
    })

OUT_CSV.parent.mkdir(parents=True, exist_ok=True)

fieldnames = [
    "experiment",
    "scenario",
    "baseline",
    "simInsts",
    "numCycles",
    "ipc",
    "cpi",
    "speedup",
    "l1d_hits",
    "l1d_misses",
    "l1d_miss_rate",
    "l1d_mpki",
    "l1i_hits",
    "l1i_misses",
    "l1i_miss_rate",
    "l1i_mpki",
    "l2_hits",
    "l2_misses",
    "l2_miss_rate",
    "l2_mpki",
]

with OUT_CSV.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"CSV final gerado em: {OUT_CSV}")
print(f"Total de cenários finais: {len(rows)}")
for row in rows:
    print(row)
