#!/bin/bash

GEM5_DIR="/Users/guimeyer/Importantes/dev/gem5"
PROJECT_DIR="/Users/guimeyer/Importantes/Faculdade/5º período/AC3/gem5-memory-hierarchy-study"
CONFIG="$PROJECT_DIR/configs/memory_exp.py"
OUT_BASE="$PROJECT_DIR/results/raw"

mkdir -p "$OUT_BASE/matmul_mem_ddr3_1600" "$OUT_BASE/matmul_mem_ddr3_2133" "$OUT_BASE/matmul_mem_ddr4_2400"

"$GEM5_DIR/build/ALL/gem5.opt" -d "$OUT_BASE/matmul_mem_ddr3_1600" "$CONFIG" --mem ddr3_1600
"$GEM5_DIR/build/ALL/gem5.opt" -d "$OUT_BASE/matmul_mem_ddr3_2133" "$CONFIG" --mem ddr3_2133
"$GEM5_DIR/build/ALL/gem5.opt" -d "$OUT_BASE/matmul_mem_ddr4_2400" "$CONFIG" --mem ddr4_2400
