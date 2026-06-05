# Extraordinary JXF Multi-Environment Toolkit

This repository bridges high-precision Python math models with real-time audio-visual synthesis in Cycling '74 Max/MSP. It utilizes the native binary JXF (Jitter Matrix Format) to pass uncompressed multi-dimensional coordinate data directly between disk and RAM at maximum speeds.

## 📁 Repository Structure
```text
jxf-extraordinary-toolkit/
├── python/
│   ├── generator.py      # Outputs chaos_cloud.jxf (Lorenz Attractor)
│   ├── dna_generator.py  # Outputs dna_helix.jxf (Parametric Helix)
│   └── run_all.py        # Automation execution script
├── max/
│   ├── jxf_synth.maxpat  # The real-time visual grid and audio engine
│   └── data/             # Target directory for generated JXF files
└── README.md             # This instruction manual
```

## 🚀 Quick Start Setup

### Step 1: Generate the Binary Matrix Data
Ensure you have Python 3 and NumPy installed, then execute the orchestration script:
```bash
cd python
python run_all.py
```
This generates `chaos_cloud.jxf` and `dna_helix.jxf` into the `max/data/` workspace.

### Step 2: Fire Up the Max Engine
1. Launch **Max/MSP Jitter**.
2. Open `max/jxf_synth.maxpat`.
3. Unmute your DAC (`ezdac~`) to activate audio processing.
4. Toggle between the `read data/chaos_cloud.jxf` and `read data/dna_helix.jxf` message boxes.

## 🎚️ Interaction Profiles
* **Chaos Mode (`chaos_cloud.jxf`)**: Renders an infinite 3D strange attractor starfield on screen while producing harsh, unaligned chaotic sound frequencies.
* **Bio-Structure Mode (`dna_helix.jxf`)**: Automatically collapses the cloud into a perfectly structured, rotating dual helix while shifting the audio profile into rhythmic, looping harmonic cycles.
