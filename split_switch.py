import sys
from monitorcontrol import get_monitors

# Vendor-specific VCP code for PBP/PIP pane source
VCP_PANE_SOURCE = 0xE3

# Pane assignments (Channel)
PANES = {
    "left": 0x00,
    "middle": 0x01,
    "right": 0x02
}

# Source assignments for 0xE3 on the 57" G9
SOURCES = {
    "dp1": 0x10,
    "hdmi1": 0x00,
    "hdmi2": 0x01,
    "hdmi3": 0x02
}

def switch_pbp_input(pane, source):
    if pane not in PANES:
        print(f"Invalid pane. Choose from: {', '.join(PANES.keys())}")
        sys.exit(1)
        
    if source not in SOURCES:
        print(f"Invalid source. Choose from: {', '.join(SOURCES.keys())}")
        sys.exit(1)

    payload = (PANES[pane] << 8) | SOURCES[source]
    
    print(f"Targeting {pane} pane with {source}...")
    print(f"Calculated payload: {payload} (Hex: {hex(payload)})")

    monitors = get_monitors()
    if not monitors:
        print("No monitors found.")
        sys.exit(1)

    # Grab the first detected display connection
    target_monitor = monitors[0]
    
    # We MUST use the context manager (with target_monitor:) to open the connection
    with target_monitor:
        try:
            target_monitor.vcp.set_vcp_feature(VCP_PANE_SOURCE, payload)
            print("Command sent successfully (1 time).")
        except Exception as e:
            print(f"Failed to send DDC command: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python split_switch.py [pane] [source]")
        print("Example: python split_switch.py middle dp1")
        sys.exit(1)
        
    switch_pbp_input(sys.argv[1].lower(), sys.argv[2].lower())