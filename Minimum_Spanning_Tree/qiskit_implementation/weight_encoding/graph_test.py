
import qiskit
import qiskit_aqua
import qiskit as q

from edge_finder import EdgeFinder
from edge_finder import encode_graph
from edge_finder import select_value
from edge_finder import get_logger

logger = get_logger(__name__)


class GraphTest(EdgeFinder):

    def setup_oracle(self):
        self.oracle  = q.QuantumCircuit(*self.qregisters,*self.cregisters)

        self.oracle.barrier()

        self.oracle = encode_graph(self.oracle, self.graph, self.start, self.end, self.weight, self.flags[0], self.ancillas)

        self.oracle.barrier()

        self.oracle.z(self.flags[0])


if __name__ == "__main__":
    t = GraphTest()
    edge = t.run()
    logger.info("Result: {}".format(edge))