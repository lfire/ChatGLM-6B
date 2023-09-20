import torch

print(f"Pytorch version: {torch.__version__}")
if torch.cuda.is_available():
    device_count = torch.cuda.device_count()
    for i in range(device_count):
        print(f"CUDA device {i}: {torch.cuda.get_device_name(i)}")
else:
    print("No CUDA devices available.")
