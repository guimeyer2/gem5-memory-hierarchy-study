#!/bin/bash

PROJECT_DIR="/Users/guimeyer/Importantes/Faculdade/5º período/AC3/gem5-memory-hierarchy-study"
OUT_BASE="$PROJECT_DIR/results/raw"

for dir in "$OUT_BASE"/l1_*; do
  echo "=============================="
  echo "$(basename "$dir")"
  grep -E "simInsts|simTicks|numCycles|ipc|cpi|overallHits|overallMisses|demandHits|demandMisses" "$dir/stats.txt"
done
