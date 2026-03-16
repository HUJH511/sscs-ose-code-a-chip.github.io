The circuit simulation found a floating node: [NODE]

This node has no DC path to ground or supply, causing the simulation to fail.

Please identify the cause and fix the connection:
- Every internal node must be connected to at least two devices.
- Check that drain, gate, source, and bulk are all explicitly wired.
- A diode-connected transistor must have its gate shorted to its drain (same node name for both).
- The tail current transistor source must connect to VSS, not left floating.

Please rewrite the corrected complete .subckt netlist.
