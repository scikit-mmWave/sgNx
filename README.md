# OpenSignalX (open source signal exchange) Format (.sgNx)

**.sgNx** is a human-readable, open-source data format designed for efficient and flexible exchange of frequency-domain RF and microwave signal data, such as S-parameters. It is intended to be easy to parse in both MATLAB and Python without requiring any external libraries or complex parsing logic.

## 🔧 Key Features

* 📡 **Multi-port support**: Use `.sg1x`, `.sg2x`, `.sg3x`, etc., to represent 1-port, 2-port, and multi-port networks.
* 🧾 **Minimal, clean format**: Frequency data is stored using a compact vector definition (e.g., `linspace()`).
* 💬 **Embedded metadata**: User-defined fields such as author, date, comments, and port mappings.
* 📈 **Complex signal representation**: Complex S-parameters are stored using Euler’s form: `re^{jθ}`.
* 🔁 **Interoperable**: Designed for use in MATLAB, Python, and other analysis environments with minimal setup.

## 📂 File Naming Convention

* `.sgNx`: General format definition file.
* `.sg1x`: 1-port network data (e.g., S11).
* `.sg2x`: 2-port network data (e.g., S11, S21, S12, S22).
* `.sgNx`: Generic multi-port data format for N ports.

## 🧱 File Structure (Draft Format)

```plaintext
# Signal Exchange Format v0.1
# Format under revision
meta:
  title: "My S-Parameter Measurement"
  author: "scikit-mmWave"
  date: "2025-05-17"
  ports: 2
  comments: "Measured at lab with 10 MHz spacing"
  
frequency:
  linspace(1e9, 5e9, 401)

sparameters:
  S11: [ 0.9e^{j0.1}, 0.85e^{j0.15}, ..., 0.3e^{j1.2} ]
  S21: [ 0.1e^{j0.8}, 0.12e^{j0.82}, ..., 0.6e^{j1.5} ]
  S12: [ ... ]
  S22: [ ... ]
```
