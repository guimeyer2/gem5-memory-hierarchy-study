# Metodologia

## Objetivo

Avaliar o impacto de parâmetros da hierarquia de memória no desempenho de um workload com padrão de acesso à memória mais representativo.

## Hipótese

A capacidade e a organização da hierarquia de memória influenciam diretamente o desempenho do workload analisado. Espera-se que aumentos de capacidade de cache, ajustes de associatividade e melhorias na configuração da memória principal reduzam misses e custos de acesso, com ganhos que tendem a saturar após certo ponto.

## Simulador e configuração base

- gem5
- modo SE
- ISA x86
- 1 núcleo
- CPU do tipo TIMING
- frequência de 3 GHz
- memória principal de 1 GiB
- cache line size de 64 bytes
- workload `x86-matrix-multiply`

## Workload

O workload principal utilizado na análise final foi `x86-matrix-multiply`, disponível na biblioteca de recursos do gem5. O benchmark realiza multiplicação de matrizes densas com padrão de acesso regular, sendo adequado para observar comportamento de cache e interação com a memória principal.

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

## Experimento C, configuração da memória principal

Variação da configuração da memória principal, mantendo a hierarquia de cache fixa:

- DDR3-1600
- DDR3-2133
- DDR4-2400

Com L1 fixa em 16 KiB e L2 fixa em 32 KiB.

Cenários:

- `matmul_mem_ddr3_1600`
- `matmul_mem_ddr3_2133`
- `matmul_mem_ddr4_2400`

## Experimento D, associatividade da L1D

Variação da associatividade da cache L1D, mantendo os demais parâmetros constantes dentro do experimento:

- 2-way
- 4-way
- 8-way

Com L1D e L1I fixas em 16 KiB e L2 fixa em 64 KiB.

Cenários:

- `matmul_assoc_l1d2`
- `matmul_assoc_l1d4`
- `matmul_assoc_l1d8`

Observação: neste experimento foi utilizada uma configuração de hierarquia específica para permitir a variação da associatividade da L1D. A comparação deve ser interpretada internamente ao próprio experimento.

## Métricas analisadas

- hits e misses
- miss rate
- MPKI
- IPC
- CPI
- número de ciclos
- speedup em relação à baseline de cada experimento
- latência média de miss da L1D
- latência média de miss da L2

Os contadores de blocked cycles também foram extraídos, mas não se mostraram informativos no conjunto final de execuções.

## Baselines

As baselines utilizadas foram:

- `matmul_l1_16k` para o experimento A
- `matmul_l2b_32k` para o experimento B
- `matmul_mem_ddr3_1600` para o experimento C
- `matmul_assoc_l1d2` para o experimento D

## Tabela oficial

A tabela consolidada usada para a análise final está em:

`results/tables/final_summary.csv`
