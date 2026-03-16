Your generated netlist produced the following ngspice error:

[ERROR]

Please fix the netlist and regenerate the complete .subckt block. Rules:
- Do NOT change the overall circuit topology.
- Fix only: wrong node names, missing connections, or invalid SPICE syntax.
- Every MOSFET must use the X prefix (subcircuit instance), NOT M.
- Only use SKY130 models: sky130_fd_pr__nfet_01v8 (NMOS) or sky130_fd_pr__pfet_01v8 (PMOS).
- NMOS bulk must connect to VSS. PMOS bulk must connect to VDD.
- Do NOT include parasitic parameters (no ad=, as=, pd=, ps=, nrd=, nrs=, sa=, sb=, sd=, mult=, m=).
- Use parameterized sizing (L=L1 W=W1 nf=NF1), not hard-coded numbers in device lines.
- The .subckt line must include all required pins exactly as specified.
