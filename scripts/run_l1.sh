#!/bin/bash

GEM5_DIR="$HOME/dev/gem5"
PROJECT_DIR="/Users/guimeyer/Importantes/Faculdade/5º período/AC3/gem5-memory-hierarchy-study"
CONFIG="$PROJECT_DIR/configs/cache_exp.py"
OUT_BASE="$PROJECT_DIR/results/raw"

mkdir -p "$OUT_BASE/mm_l1_16k" "$OUT_BASE/mm_l1_32k" "$OUT_BASE/mm_l1_64k"

"$GEM5_DIR/build/ALL/gem5.opt" -d "$OUT_BASE/mm_l1_16k" "$CONFIG" --l1d 16KiB --l1i 16KiB --l2 256KiB
"$GEM5_DIR/build/ALL/gem5.opt" -d "$OUT_BASE/mm_l1_32k" "$CONFIG" --l1d 32KiB --l1i 32KiB --l2 256KiB
"$GEM5_DIR/build/ALL/gem5.opt" -d "$OUT_BASE/mm_l1_64k" "$CONFIG" --l1d 64KiB --l1i 64KiB --l2 256KiB
