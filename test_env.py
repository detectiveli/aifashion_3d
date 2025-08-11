import numpy as np
import torch
import open3d as o3d

print("Python环境测试成功!")
print(f"NumPy版本: {np.__version__}")
print(f"PyTorch版本: {torch.__version__}")
print(f"Open3D版本: {o3d.__version__}")

try:
    # 测试基本功能
    arr = np.array([1, 2, 3])
    print(f"NumPy数组: {arr}")

    tensor = torch.tensor([1, 2, 3])
    print(f"PyTorch张量: {tensor}")

    print("环境测试完成，所有库均正常工作。")
except Exception as e:
    print(f"测试出错: {e}")