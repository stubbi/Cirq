# Copyright 2018 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""A combination of several optimizations targeting XmonDevice."""
from typing import Callable, cast, Optional, TYPE_CHECKING

import cirq
from cirq_google.optimizers import optimized_for_sycamore

if TYPE_CHECKING:
    import cirq_google


def optimized_for_xmon(
    circuit: cirq.Circuit,
    new_device: Optional['cirq_google.XmonDevice'] = None,
    qubit_map: Callable[[cirq.Qid], cirq.GridQubit] = lambda e: cast(cirq.GridQubit, e),
    allow_partial_czs: bool = False,
) -> cirq.Circuit:
    if allow_partial_czs:
        return optimized_for_sycamore(
            circuit, new_device=new_device, qubit_map=qubit_map, optimizer_type='xmon_partial_cz'
        )
    else:
        return optimized_for_sycamore(
            circuit, new_device=new_device, qubit_map=qubit_map, optimizer_type='xmon'
        )
