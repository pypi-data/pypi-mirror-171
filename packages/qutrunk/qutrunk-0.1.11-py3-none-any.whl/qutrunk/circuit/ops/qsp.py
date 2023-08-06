"""Quantum state preparation Operator."""

from typing import Union

from qutrunk.exceptions import QuTrunkError
from .operator import Operator, OperatorContext
from qutrunk.circuit import Qureg
from qutrunk.circuit.gates import X, All, H


class QSP(Operator):
    """Quantum state preparation Operator.

    Init the quantum state to specific state, currently support: Plus state, Classical state.

    Args:
        state: The target state of circuit initialized to.

    Example:
        .. code-block:: python

            from qutrunk.circuit.ops import QSP
            from qutrunk.circuit import QCircuit
            from qutrunk.circuit.gates import H, All, Measure

            circuit = QCircuit()
            qureg = circuit.allocate(2)
            QSP("+") * qureg
            print(circuit.get_all_state())
    """

    def __init__(self, state: Union[str, int]):
        super().__init__()
        self.state = state

    def _check_state(self, qureg: Qureg):
        if self.state == "+":
            return True

        if isinstance(self.state, str):
            val = int(self.state, base=2)
            if 0 <= val < 2 ** len(qureg):
                return True

        if isinstance(self.state, int):
            if 0 <= self.state < 2 ** len(qureg):
                return True

        return False

    def __mul__(self, qureg: Qureg):
        """Apply the QSP operator."""
        if not isinstance(qureg, Qureg):
            raise TypeError("the operand must be Qureg.")

        if not self._check_state(qureg):
            raise ValueError("Invalid Classical state.")

        if qureg.circuit.gates_len > 0:
            raise QuTrunkError("QSP should be applied at the beginning of circuit.")

        with OperatorContext(qureg.circuit) as oc:
            if self.state == "+":
                self._process_plus_state(qureg)
            else:
                self._process_classical_state(qureg)

        qureg.circuit.append_statement(f"QSP('{self.state}') * q")

    def _process_plus_state(self, qureg: Qureg):
        """Process plus state."""
        All(H) * qureg

    def _process_classical_state(self, qureg: Qureg):
        """Process classical state."""
        bit_strs = ""
        if isinstance(self.state, str):
            if self.state.startswith("0b"):
                bit_strs = self.state[2:]
            else:
                bit_strs = self.state
        elif isinstance(self.state, int):
            bit_strs = str(bin(self.state))
            bit_strs = bit_strs[2:]

        bit_strs = bit_strs.zfill(len(qureg))
        bit_strs = bit_strs[::-1]

        for i, _ in enumerate(qureg):
            if bit_strs[i] == "1":
                X * qureg[i]
