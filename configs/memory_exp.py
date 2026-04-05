import argparse

from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.private_l1_private_l2_cache_hierarchy import (
    PrivateL1PrivateL2CacheHierarchy,
)
from gem5.components.memory.single_channel import (
    SingleChannelDDR3_1600,
    SingleChannelDDR3_2133,
    SingleChannelDDR4_2400,
)
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.isas import ISA
from gem5.resources.resource import obtain_resource
from gem5.simulate.simulator import Simulator

parser = argparse.ArgumentParser(description="Experimento de configuracao da memoria principal")
parser.add_argument("--mem", choices=["ddr3_1600", "ddr3_2133", "ddr4_2400"], default="ddr3_1600")
parser.add_argument("--binary", default="x86-matrix-multiply")
args = parser.parse_args()

cache_hierarchy = PrivateL1PrivateL2CacheHierarchy(
    l1d_size="16KiB",
    l1i_size="16KiB",
    l2_size="64KiB",
)

if args.mem == "ddr3_1600":
    memory = SingleChannelDDR3_1600("1GiB")
elif args.mem == "ddr3_2133":
    memory = SingleChannelDDR3_2133("1GiB")
else:
    memory = SingleChannelDDR4_2400("1GiB")

processor = SimpleProcessor(
    cpu_type=CPUTypes.TIMING,
    num_cores=1,
    isa=ISA.X86,
)

board = SimpleBoard(
    clk_freq="3GHz",
    processor=processor,
    memory=memory,
    cache_hierarchy=cache_hierarchy,
)

binary = obtain_resource(args.binary)
board.set_se_binary_workload(binary)

simulator = Simulator(board=board)
simulator.run()
