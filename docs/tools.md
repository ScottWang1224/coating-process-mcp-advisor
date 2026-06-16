# Tools

All tools are simulation-only and deterministic.

## convert_volume

Converts between `mL`, `L`, and `m3`. Rejects negative values and unsupported units.

## convert_temperature

Converts between `C`, `K`, and `F`. Rejects temperatures below absolute zero.

## check_process_range

Returns `normal`, `low`, or `high` plus deviation.

## calculate_solvent_addition

Uses:

```text
V_final = V_initial * C_current / C_target
V_solvent_add = V_final - V_initial
```

## estimate_line_speed_for_target_thickness

Uses:

```text
target_speed = current_thickness * current_speed / target_thickness
```

## estimate_viscosity_temperature_risk

Classifies qualitative risk from viscosity status and temperature context. It does not calculate
material-specific corrected viscosity.

