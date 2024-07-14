import os
import shutil
import re

def find_cuda_bin_path(cuda_base_path="C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA"):
    """
    Finds the CUDA bin directory by searching for subdirectories starting with "v".
    """
    for entry in os.listdir(cuda_base_path):
        if entry.startswith("v") and os.path.isdir(os.path.join(cuda_base_path, entry)):
            cuda_bin_path = os.path.join(cuda_base_path, entry, "bin")
            if os.path.exists(cuda_bin_path):
                return cuda_bin_path
    print(f"Error: CUDA bin directory not found in '{cuda_base_path}' or its subdirectories.")
    return None

def copy_tensorrt_lib_folder(cuda_base_path="C:\\Program Files\\NVIDIA GPU Computing Toolkit"):  # Change to base toolkit path
    """
    Copies the 'lib' folder from ANY TensorRT- directory to the CUDA bin directory. Resolves symbolic links.
    """
    cuda_bin_path = find_cuda_bin_path(os.path.join(cuda_base_path, "CUDA"))  # Look for CUDA within the toolkit path
    if not cuda_bin_path:
        return

    # Search directly in the base toolkit path for the TensorRT- folder
    tensorrt_folders = [f for f in os.listdir(cuda_base_path) if f.startswith("TensorRT-") and os.path.isdir(os.path.realpath(os.path.join(cuda_base_path, f)))]

    if not tensorrt_folders:
        print(f"No TensorRT folders found in '{cuda_base_path}'.")
        return

    # Copy from the first TensorRT- folder found
    tensorrt_folder = tensorrt_folders[0]
    lib_folder = os.path.join(cuda_base_path, tensorrt_folder, "lib")

    if os.path.exists(lib_folder):
        try:
            print(f"Copying from '{lib_folder}' to '{cuda_bin_path}'...")
            shutil.copytree(lib_folder, cuda_bin_path, dirs_exist_ok=True)
            print(f"Copying completed successfully.")
        except shutil.Error as e:
            print(f"Error copying files: {e}")
    else:
        print(f"Warning: 'lib' folder not found in '{tensorrt_folder}'")

if __name__ == "__main__":
    copy_tensorrt_lib_folder()