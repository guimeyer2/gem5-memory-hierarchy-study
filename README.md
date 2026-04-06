# gem5-memory-hierarchy-study

Projeto da disciplina de Arquitetura de Computadores para estudo da hierarquia de memória usando o simulador gem5.

## Objetivo

Investigar o impacto de parâmetros da hierarquia de memória no desempenho e no comportamento de memória em um workload com padrão de acesso à memória mais representativo.

## Estrutura do repositório

- `configs/`: scripts de configuração do gem5
- `scripts/`: scripts de execução e extração de métricas
- `docs/`: descrição do ambiente e metodologia
- `results/raw/`: saídas brutas do gem5
- `results/tables/`: tabelas consolidadas
- `results/figures/`: gráficos finais
- `paper/`: artigo
- `slides/`: apresentação

## Organização dos resultados

### Rodada preliminar

As pastas `results/raw/l1_*` correspondem a execuções preliminares usadas apenas para validar o pipeline de simulação e extração.

### Cenários finais oficiais

Os cenários usados na análise final do trabalho são:

#### Experimento A, variação da L1

- `matmul_l1_16k`
- `matmul_l1_32k`
- `matmul_l1_64k`

#### Experimento B, variação da L2

- `matmul_l2b_32k`
- `matmul_l2b_64k`
- `matmul_l2b_128k`
- `matmul_l2b_256k`

#### Experimento C, configuração da memória principal

- `matmul_mem_ddr3_1600`
- `matmul_mem_ddr3_2133`
- `matmul_mem_ddr4_2400`

#### Experimento D, associatividade da L1D

- `matmul_assoc_l1d2`
- `matmul_assoc_l1d4`
- `matmul_assoc_l1d8`

A tabela consolidada oficial para gráficos e artigo está em:

`results/tables/final_summary.csv`

## Workload

O workload principal utilizado na análise final foi `x86-matrix-multiply`.

## Métricas disponíveis

A tabela final consolidada inclui:

- hits e misses
- miss rate
- MPKI
- IPC
- CPI
- numCycles
- speedup
- latência média de miss da L1D
- latência média de miss da L2

## Como reproduzir

### Pré-requisito

Ter o gem5 compilado localmente.

### Rodar os experimentos

```bash
./scripts/run_l1.sh
./scripts/run_l2.sh
./scripts/run_mem.sh
./scripts/run_assoc.sh
```

### Caso seja necessário regerar a tabela final

```bash
python3 scripts/extract_final_results.py
```
