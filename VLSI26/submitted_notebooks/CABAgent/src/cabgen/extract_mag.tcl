set pdk_mcfg    $env(PDK_MCFG)
set gds_path    $env(GDS_PATH)
set top_module  $env(TOP_MODULE)

# Load PDK
source $pdk_mcfg

# Read layout
gds read $gds_path
load $top_module
select top cell

# Automatically label all external pins as ports
port makeall

# Extract layout and ports
extract all
extract do local
extract unique

# Generate initial .sim file (needed for resistance extraction)
ext2sim labels on
ext2sim

# Extract detailed resistance network
extresist tolerance 0.01
extresist 

# LVS netlist (structure only)
ext2spice lvs
ext2spice -m -o ${top_module}_lvs.spice

# PEX netlist with parasitics (flattened + full RC)
ext2spice merge none
ext2spice format ngspice
ext2spice extresist on
ext2spice cthresh 0
ext2spice rthresh 0
ext2spice -o tmp_pex.spice

# Filter out bad lines with w=0 l=0
shell "grep -v ' w=0 l=0' tmp_pex.spice > ${top_module}_pex.spice"
shell "rm -f tmp_pex.spice"

exit