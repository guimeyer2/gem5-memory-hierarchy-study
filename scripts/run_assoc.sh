#!/bin/bash

GEM5_DIR="/Users/guimeyer/Importantes/dev/gem5"
PROJECT_DIR="/Users/guimeyer/Importantes/Faculdade/5º período/AC3/gem5-memory-hierarchy-study"
CONFIG="$PROJECT_DIR/configs/assoc_exp.py"
OUT_BASE="$PROJECT_DIR/results/raw"

mkdir -p "$OUT_BASE/matmul_assoc_l1d2" "$OUT_BASE/matmul_assoc_l1d4" "$OUT_BASE/matmul_assoc_l1d8"

"$GEM5_DIR/build/ALL/gem5.opt" -d "$OUT_BASE/matmul_assoc_l1d2" "$CONFIG" --l1d_assoc 2
"$GEM5_DIR/build/ALL/gem5.opt" -d "$OUT_BASE/matmul_assoc_l1d4" "$CONFIG" --l1d_assoc 4
"$GEM5_DIR/build/ALL/gem5.opt" -d "$OUT_BASE/matmul_assoc_l1d8" "$CONFIG" --l1d_assoc 8
