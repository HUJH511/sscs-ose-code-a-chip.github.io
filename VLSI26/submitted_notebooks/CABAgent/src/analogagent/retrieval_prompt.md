I have the following SKY130 analog circuit design rules and topology patterns stored in the knowledge base.

| Id | Circuit Type | Topology | Key Feature |
|---|---|---|---|
| 1 | OTA | Five-transistor OTA | PMOS mirror load, NMOS diff pair, 1:1 tail mirror, 6 transistors |
| 2 | OTA | Telescopic cascode OTA | PMOS cascode mirror, NMOS cascode diff pair, VCN/VCP bias, 10 transistors |
| 3 | Current Mirror | Simple 1:1 NMOS mirror | Diode-connected ref, 2 transistors |
| 4 | Current Mirror | Simple 1:1 PMOS mirror | Diode-connected ref, 2 transistors |
| 5 | Bias Circuit | Self-biased reference | Resistor + diode-connected NMOS |

SKY130 device rules:
- All MOSFETs use subcircuit prefix X (not M)
- NMOS model: sky130_fd_pr__nfet_01v8, PMOS model: sky130_fd_pr__pfet_01v8
- Minimum L = 0.15 um, W multiples of 0.42 um, nf >= 1
- NMOS bulk = VSS, PMOS bulk = VDD

Now, you need to design [TASK].

Based on the circuit description, identify which topology pattern(s) from the table above are most relevant as reference. Choose the IDs of the most relevant entries and enumerate them in a Python list like ```[1]``` or ```[1, 3]```.
