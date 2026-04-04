# Metodologia

## Objetivo

Avaliar o impacto de parâmetros da hierarquia de memória no desempenho de um workload com padrão de acesso à memória mais representativo.

## Hipótese

O aumento da capacidade da cache L1 e da cache L2 tende a reduzir misses e melhorar o desempenho até certo ponto, dependendo do padrão de acesso do workload.

## Simulador e configuração base

- gem5
- modo SE
- ISA x86
- 1 núcleo
- CPU do tipo TIMING
- memória DDR3
- hierarquia clássica com L1 privada e L2 privada
- cache line size de 64 bytes

## Workload

O workload principal utilizado na análise final foi `x86-matrix-multiply`.

## Rodada preliminar

Uma rodada preliminar com workload simples foi utilizada apenas para validar o ambiente, os scripts e a extração de métricas. Esses resultados aparecem nas pastas `results/raw/l1_*` e não fazem parte da análise final do trabalho.

## Experimento A, variação da L1

Variação do tamanho da L1, mantendo os demais parâmetros constantes:

- 16 KiB
- 32 KiB
- 64 KiB

Com L2 fixa em 256 KiB.

Cenários:

- `matmul_l1_16k`
- `matmul_l1_32k`
- `matmul_l1_64k`

## Experimento B, variação da L2

Variação do tamanho da L2, mantendo os demais parâmetros constantes:

- 32 KiB
- 64 KiB
- 128 KiB
- 256 KiB

Com L1 fixa em 16 KiB.

Cenários:

- `matmul_l2b_32k`
- `matmul_l2b_64k`
- `matmul_l2b_128k`
- `matmul_l2b_256k`

## Métricas analisadas

- hits e misses
- miss rate
- MPKI
- IPC
- CPI
- número de ciclos

## Tabela oficial

A tabela consolidada usada para a análise final está em:

`results/tables/final_summary.csv`
