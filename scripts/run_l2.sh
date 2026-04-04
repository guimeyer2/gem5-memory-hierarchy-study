#!/bin/bash

GEM5_DIR="/Users/guimeyer/Importantes/dev/gem5"
PROJECT_DIR="/Users/guimeyer/Importantes/Faculdade/5º período/AC3/gem5-memory-hierarchy-study"
CONFIG="$PROJECT_DIR/configs/cache_exp.py"
OUT_BASE="$PROJECT_DIR/results/raw"

mkdir -p "$OUT_BASE/matmul_l2b_32k" "$OUT_BASE/matmul_l2b_64k" "$OUT_BASE/matmul_l2b_128k" "$OUT_BASE/matmul_l2b_256k"

"$GEM5_DIR/build/ALL/gem5.opt" -d "$OUT_BASE/matmul_l2b_32k"  "$CONFIG" --l1d 16KiB --l1i 16KiB --l2 32KiB
"$GEM5_DIR/build/ALL/gem5.opt" -d "$OUT_BASE/matmul_l2b_64k"  "$CONFIG" --l1d 16KiB --l1i 16KiB --l2 64KiB
"$GEM5_DIR/build/ALL/gem5.opt" -d "$OUT_BASE/matmul_l2b_128k" "$CONFIG" --l1d 16KiB --l1i 16KiB --l2 128KiB
"$GEM5_DIR/build/ALL/gem5.opt" -d "$OUT_BASE/matmul_l2b_256k" "$CONFIG" --l1d 16KiB --l1i 16KiB --l2 256KiB
