import numpy as np
import struct
import os
def write_jxf(filename, matrix_data):
    """
    Writes a NumPy array directly into a valid Cycling '74 JXF file.
    Supports 2D and 3D arrays.
    """
    # Determine dimensions and planes
    shape = matrix_data.shape
    if len(shape) == 2:    # Single plane matrix [rows, cols]
        planecount = 1
        dimcount = 2
        dim = [shape[1], shape[0], 0, 0]
    elif len(shape) == 3:  # Multi-plane matrix [rows, cols, planes]
        planecount = shape[2]
        dimcount = 2
        dim = [shape[1], shape[0], 0, 0]
    else:
        raise ValueError("Only 2D matrices (with optional plane depth) are supported in this script.")

    # Determine type mapping
    dtype = matrix_data.dtype
    if dtype == np.uint8:
        type_str = b'char'
        type_code = 0
    elif dtype == np.float32:
        type_str = b'fl32'
        type_code = 3
    else:
        raise TypeError("Unsupported numpy dtype. Use np.uint8 or np.float32.")

    # 1. Magic Number (4 bytes)
    magic = b'jmp!'
    
    # 2 & 3. Header construction (Fixed size for standard Jitter matrix headers)
    # Header format: padding/version, type_code, planecount, dimcount, dim[0], dim[1], dim[2], dim[3]
    header_data = struct.pack('>IIIIIIII', 0, type_code, planecount, dimcount, dim[0], dim[1], dim[2], dim[3])
    header_size = len(header_data) + 8 # includes magic and size bytes
    
    # Write to binary file
    with open(filename, 'wb') as f:
        f.write(magic)
        f.write(struct.pack('>I', header_size))
        f.write(header_data)
        # 4. Matrix Data Block (Flattened big-endian raw binary data)
        # Max reads matrix files in big-endian format
        f.write(matrix_data.astype(dtype).byteswap(inplace=False).tobytes() if ndarray_is_little_endian() else matrix_data.tobytes())
    print(f"Successfully generated extraordinary JXF: {filename}")

def ndarray_is_little_endian():
    return struct.pack('H', 1) == b'\x01\x00'

def generate_lorenz_attractor(num_points=10000):
    """Generates a 3D chaotic attractor mapped to a 100x100 3-plane float32 matrix."""
    dt = 0.01
    xs, ys, zs = np.zeros(num_points), np.zeros(num_points), np.zeros(num_points)
    xs[0], ys[0], zs[0] = 0.1, 0.0, 0.0
    
    # Lorentz system equations
    for i in range(1, num_points):
        xs[i] = xs[i-1] + (10.0 * (ys[i-1] - xs[i-1])) * dt
        ys[i] = ys[i-1] + (xs[i-1] * (28.0 - zs[i-1]) - ys[i-1]) * dt
        zs[i] = zs[i-1] + (xs[i-1] * ys[i-1] - (8.0 / 3.0) * zs[i-1]) * dt
        
    # Normalize data between -1.0 and 1.0 for easy GPU rendering
    coords = np.vstack((xs, ys, zs)).T
    coords /= np.max(np.abs(coords))

    # Reshape to a 100x100 2D grid with 3 planes (X, Y, Z)
    matrix_3d = coords.reshape((100, 100, 3)).astype(np.float32)
    return matrix_3d

if __name__ == "__main__":
    os.makedirs("../max/data", exist_ok=True)
    
    # Generate Concept 1: Extraordinary 3D Chaos Data Cloud
    lorenz_matrix = generate_lorenz_attractor()
    write_jxf("../max/data/chaos_cloud.jxf", lorenz_matrix)
