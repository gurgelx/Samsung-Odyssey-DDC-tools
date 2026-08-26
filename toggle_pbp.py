import sys
from monitorcontrol import get_monitors

# Vendor-specific VCP code for Mode/Layout
VCP_LAYOUT = 0xE2

# Samsung 57" Neo G9 Layout Codes
LAYOUTS = {
    "off": 0x00,
    "pip": 0x10,
    "pbp": 0x03,     # Standard 50/50 split
    "3pbp": 0x08,    # 3-way split (25/50/25)
}

def set_layout(layout_name):
    if layout_name not in LAYOUTS:
        print(f"Invalid layout. Choose from: {', '.join(LAYOUTS.keys())}")
        sys.exit(1)

    payload = LAYOUTS[layout_name]
    print(f"Switching layout to {layout_name} (Hex: {hex(payload)})...")

    monitors = get_monitors()
    if not monitors:
        print("No monitors found.")
        sys.exit(1)

    # Grab the first detected display connection
    target_monitor = monitors[0]
    
    with target_monitor:
        try:
            target_monitor.vcp.set_vcp_feature(VCP_LAYOUT, payload)
            print("Layout changed successfully.")
        except Exception as e:
            print(f"Failed to change layout: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python toggle_pbp.py [{ '|'.join(LAYOUTS.keys()) }]")
        print("Example: python toggle_pbp.py off")
        sys.exit(1)
        
    set_layout(sys.argv[1].lower())