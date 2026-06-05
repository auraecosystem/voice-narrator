import numpy as np
import struct
import os

def write_jxf(filename, matrix_data):
    """Writes a NumPy array directly into a valid Cycling '74 JXF file."""
    shape = matrix_data.shape
    planecount = shape[2] if len(shape) == 3 else 1
    dimcount = 2
    dim_w, dim_h = shape[0], shape[1]

    magic = b'jmp!'
    # type_code 3 = float32
    header_data = struct.pack('>IIIIIIII', 0, 3, planecount, dimcount, dim_w, dim_h, 0, 0)
    header_size = len(header_data) + 8
    
    with open(filename, 'wb') as f:
        f.write(magic)
        f.write(struct.pack('>I', header_size))
        f.write(header_data)
        # Force big-endian encoding for Max/MSP Jitter compliance
        if struct.pack('H', 1) == b'\x01\x00':
            f.write(matrix_data.astype(np.float32).byteswap(inplace=False).tobytes())
        else:
            f.write(matrix_data.astype(np.float32).tobytes())
    print(f"Generated structural DNA JXF: {filename}")

def generate_dna_helix(num_points=10000):
    """Generates a 3D parametric DNA Double Helix scaled between -1.0 and 1.0."""
    t = np.linspace(0, 4 * np.pi, num_points)
    
    # Strand 1 coordinates
    x1 = np.cos(t)
    y1 = np.sin(t)
    z1 = t / (4 * np.pi) * 2 - 1  # Scale Z axis between -1 and 1
    
    # Strand 2 coordinates (180 degrees out of phase)
    x2 = np.cos(t + np.pi)
    y2 = np.sin(t + np.pi)
    z2 = z1
    
    # Interleave the strands together to create a continuous data matrix
    coords = np.zeros((num_points, 3))
    coords[0::2] = np.vstack((x1[0::2], y1[0::2], z1[0::2])).T
    coords[1::2] = np.vstack((x2[1::2], y2[1::2], z2[1::2])).T
    
    # Reshape to a clean 100x100 matrix with 3 planes (X, Y, Z)
    return coords.reshape((100, 100, 3)).astype(np.float32)

if __name__ == "__main__":
    os.makedirs("../max/data", exist_ok=True)
    dna_matrix = generate_dna_helix()
    write_jxf("../max/data/dna_helix.jxf", dna_matrix)
