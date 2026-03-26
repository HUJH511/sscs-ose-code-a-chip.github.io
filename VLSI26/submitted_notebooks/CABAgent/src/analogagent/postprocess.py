"""
Post-processing for AnalogAgent output:
  1. Rename devices to sequential XM1, XM2, ...
  2. Split .subckt netlist and .param into separate files
"""

import re
from pathlib import Path


def rename_devices(subckt_code: str) -> str:
    """Rename all X-prefix devices to XM1, XM2, ... in order of appearance."""
    lines = subckt_code.splitlines()
    counter = 1
    result = []
    for line in lines:
        stripped = line.strip()
        if stripped.upper().startswith("X") and (
            "nfet" in stripped.lower() or "pfet" in stripped.lower()
        ):
            tokens = stripped.split()
            old_name = tokens[0]
            new_name = f"XM{counter}"
            tokens[0] = new_name
            result.append(" ".join(tokens))
            counter += 1
        else:
            result.append(line)
    return "\n".join(result)


def split_netlist_param(raw_code: str):
    """
    Split raw AnalogAgent output into:
      - netlist_lines: device lines only (no .param, no .subckt/.ends wrapper)
      - param_line: single .param string for ckt_param.spice
      - subckt_header: the .subckt declaration line
    """
    lines = raw_code.splitlines()

    device_lines = []
    param_tokens = []
    subckt_header = ""

    for line in lines:
        stripped = line.strip()
        low = stripped.lower()

        if low.startswith(".subckt"):
            subckt_header = stripped
        elif low.startswith(".ends"):
            continue
        elif low.startswith(".param"):
            # Extract key=value pairs
            pairs = re.findall(r'(\w+)\s*=\s*([\w.eE+\-]+)', stripped)
            param_tokens.extend(pairs)
        elif stripped.startswith("+") and param_tokens:
            # Continuation of .param line
            pairs = re.findall(r'(\w+)\s*=\s*([\w.eE+\-]+)', stripped)
            param_tokens.extend(pairs)
        elif stripped and not stripped.startswith("*"):
            # Device or other SPICE line (keep comments too? no, strip them)
            device_lines.append(stripped)
        elif stripped.startswith("*"):
            # Keep comments
            device_lines.append(stripped)

    param_line = ".param " + " ".join(f"{k}={v}" for k, v in param_tokens)
    return device_lines, param_line, subckt_header


def write_ckt_files(raw_code: str, netlist_path: str, param_path: str):
    """
    Post-process AnalogAgent output and write:
      - ckt_netlist.spice: device lines only (no .subckt/.ends/.param)
      - ckt_param.spice: single .param line
    """
    # Step 1: Rename devices
    renamed = rename_devices(raw_code)

    # Step 2: Split
    device_lines, param_line, _ = split_netlist_param(renamed)

    # Write netlist (device lines only, as Jinhai's format)
    Path(netlist_path).parent.mkdir(parents=True, exist_ok=True)
    with open(netlist_path, "w", encoding="utf-8") as f:
        f.write("\n".join(device_lines) + "\n")

    # Write param
    with open(param_path, "w", encoding="utf-8") as f:
        f.write(param_line + "\n")

    print(f"[PostProcess] Written: {netlist_path}")
    print(f"[PostProcess] Written: {param_path}")
    return netlist_path, param_path
