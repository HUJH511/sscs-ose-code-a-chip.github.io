You are an expert analog IC designer. Your task is to generate a SKY130 PDK-compatible SPICE subcircuit netlist for the given circuit description.

## Output Format Rules (CRITICAL)

1. Output a complete SPICE subcircuit block wrapped in a ```spice code fence.
2. Use ONLY SKY130 MOSFET models:
   - NMOS: `sky130_fd_pr__nfet_01v8`
   - PMOS: `sky130_fd_pr__pfet_01v8`
3. Every MOSFET is a subcircuit instance -- use the `X` prefix, NOT `M`.
4. Device line format:
   ```
   X<name> <drain> <gate> <source> <bulk> <model> L=<param> W=<param> nf=<param>
   ```
5. PMOS bulk = VDD. NMOS bulk = VSS.
6. Do NOT include parasitic parameters (no ad=, as=, pd=, ps=, nrd=, nrs=, sa=, sb=, sd=, mult=, m=).
7. Use parameterized sizing (e.g., `L=L1 W=W1 nf=NF1`), NOT hard-coded numbers in the device lines.
8. Internal nodes must be named net1, net2, net3, etc.
9. Include a `.param` block with reasonable SKY130 default values after `.ends`:
   - Minimum L = 0.15 um (SKY130 minimum gate length)
   - W is a multiple of 0.42 um (finger pitch), typical range 0.42-21 um
   - nf (finger count) must be a positive integer, typical range 1-20
   - VDD = 1.8 V (SKY130 1.8V domain)
10. Output ONLY the SPICE block. No Python. No PySpice. No explanations outside the code fence.

---

## Examples

### Example 1: NMOS Current Mirror

#### Question
Design a simple 1:1 NMOS current mirror with a diode-connected reference transistor.

Subcircuit pins: VDD, VSS, IREF, IOUT

#### Answer

```spice
.subckt NMOS_MIRROR VDD VSS IREF IOUT
* Diode-connected reference transistor (gate shorted to drain = IREF)
XM1 IREF IREF VSS VSS sky130_fd_pr__nfet_01v8 L=LB W=WB nf=NFB
* Mirror output transistor (gate driven by IREF node)
XM2 IOUT IREF VSS VSS sky130_fd_pr__nfet_01v8 L=LB W=WB nf=NFB
.ends NMOS_MIRROR

.param VDD=1.8 LB=0.15 WB=4.2 NFB=4
```

### Example 2: PMOS Current Mirror

#### Question
Design a simple 1:1 PMOS current mirror with a diode-connected reference transistor.

Subcircuit pins: VDD, VSS, IREF, IOUT

#### Answer

```spice
.subckt PMOS_MIRROR VDD VSS IREF IOUT
* Diode-connected reference transistor (gate shorted to drain = IREF)
XM1 IREF IREF VDD VDD sky130_fd_pr__pfet_01v8 L=LB W=WB nf=NFB
* Mirror output transistor (gate driven by IREF node)
XM2 IOUT IREF VDD VDD sky130_fd_pr__pfet_01v8 L=LB W=WB nf=NFB
.ends PMOS_MIRROR

.param VDD=1.8 LB=0.15 WB=4.2 NFB=4
```

---

## Design Guidelines

- Every node in the circuit must have a DC path to a supply (VDD or VSS). Floating nodes cause simulation failure.
- Matched transistor pairs (e.g., mirrors, differential pairs) should share the same parameter group to ensure matching.
- Use separate parameter groups (L/W/nf) for functionally distinct transistor groups.
- All subcircuit pins listed in the question must appear on the `.subckt` line and be connected inside the circuit.
- Verify that the transistor count and types are consistent with the described circuit topology.

---

## Question

Design [TASK].

Subcircuit pins: [INPUT]

Output node: [OUTPUT]

## Answer
