import argparse

from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.private_l1_private_l2_cache_hierarchy import (
    PrivateL1PrivateL2CacheHierarchy,
)
from gem5.components.memory.single_channel import SingleChannelDDR3_1600
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.isas import ISA
from gem5.resources.resource import obtain_resource
from gem5.simulate.simulator import Simulator

parser = argparse.ArgumentParser(description="Experimento simples de hierarquia de memória com gem5")
parser.add_argument("--l1d", default="16KiB")
parser.add_argument("--l1i", default="16KiB")
parser.add_argument("--l2", default="256KiB")
parser.add_argument("--binary", default="x86-matrix-multiply")
args = parser.parse_args()

cache_hierarchy = PrivateL1PrivateL2CacheHierarchy(
    l1d_size=args.l1d,
    l1i_size=args.l1i,
    l2_size=args.l2,
)

memory = SingleChannelDDR3_1600("1GiB")

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
