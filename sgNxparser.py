import re
import numpy as np

class SGNX:
    def __init__(self, filepath=None):
        self.meta = {}
        self.freq = None
        self.sparams = {}
        if filepath:
            self.load(filepath)

    def parse_complex_list(self, line):
        # Matches a list of complex numbers in polar form: 0.9e^{j0.1}
        matches = re.findall(r'([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)[eE]\^\{j([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)\}', line)
        return np.array([float(r) * np.exp(1j * float(p)) for r, p in matches], dtype=complex)

    def load(self, filepath):
        with open(filepath, 'r') as f:
            lines = f.readlines()

        current_param = None
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if line.startswith('meta:'):
                current_param = 'meta'
                continue
            elif line.startswith('frequency:'):
                current_param = 'frequency'
                continue
            elif line.startswith('sparameters:'):
                current_param = 'sparams'
                continue

            if current_param == 'meta':
                key, value = line.split(':', 1)
                self.meta[key.strip()] = value.strip().strip('"')
            elif current_param == 'frequency':
                match = re.match(r'linspace\(([^,]+),([^,]+),([^\)]+)\)', line)
                if match:
                    start, end, num = map(float, match.groups())
                    self.freq = np.linspace(start, end, int(num))
            elif current_param == 'sparams':
                key, value = line.split(':', 1)
                self.sparams[key.strip()] = self.parse_complex_list(value)

    def save(self, filepath):
        with open(filepath, 'w') as f:
            f.write("# Signal Exchange Format v0.1\n")
            f.write("meta:\n")
            for k, v in self.meta.items():
                f.write(f"  {k}: \"{v}\"\n")
            f.write("\nfrequency:\n")
            f.write(f"  linspace({self.freq[0]}, {self.freq[-1]}, {len(self.freq)})\n")
            f.write("\nsparameters:\n")
            for k, arr in self.sparams.items():
                complex_str = ', '.join([f"{np.abs(c):.6g}e^{{j{np.angle(c):.6g}}}" for c in arr])
                f.write(f"  {k}: [ {complex_str} ]\n")

    def __repr__(self):
        return f"<SGNX meta={self.meta} sparams={list(self.sparams.keys())}>"
