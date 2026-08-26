import sys
from monitorcontrol import get_monitors

# Exact mapping for the 57" Odyssey Neo G9
INPUTS = {
    "dp1": 15,
    "hdmi1": 5, 
    "hdmi2": 6, 
    "hdmi3": 1, 
}

def switch_input(target_input):
    if target_input not in INPUTS:
        print(f"Invalid input. Choose from: {', '.join(INPUTS.keys())}")
        sys.exit(1)

    value = INPUTS[target_input]
    
    for monitor in get_monitors():
        with monitor:
            try:
                monitor.set_input_source(value)
                print(f"Command sent: {target_input} ({value})")
            except Exception as e:
                print(f"Failed on a monitor: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python switch.py [{ '|'.join(INPUTS.keys()) }]")
        sys.exit(1)
        
    switch_input(sys.argv[1].lower())