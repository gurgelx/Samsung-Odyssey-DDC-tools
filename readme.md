# Samsung Odyssey DDC tools

## Requirements

- Firmware 1008.2 or later
- At least one source needs to be connected through HDMI
- monitorcontrol package `pip install monitorcontrol`

## PIP input select

`python split_switch.py left hdmi1`
`python split_switch.py middle dp1`
`python split_switch.py right hdmi2`

## PIP toggle

### Turn PBP mode on (50/50 split)

`python toggle_pbp.py pbp`

### Turn it back to a normal single screen

`python toggle_pbp.py off`

### Switch to the 3-way split

`python toggle_pbp.py 3pbp`
