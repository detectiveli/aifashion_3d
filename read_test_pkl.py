import torch
import joblib
import numpy as np
import os

# 定义文件路径
file_path = 'c:\\Users\\lihui\\Desktop\\AiFashion\\code\\body-model-visualizer\\test.pkl'

# 检查文件是否存在
if not os.path.exists(file_path):
    print(f"文件不存在: {file_path}")
    exit(1)

# 加载pkl文件
try:
    data = joblib.load(file_path)
    print(f"成功加载文件: {file_path}")
    print(f"字典键: {list(data.keys())}")
    print("\n--- 数据内容 ---\n")

    # 打印每个键的值信息
    for key, value in data.items():
        print(f"键: {key}")
        print(f"类型: {type(value)}")

        # 根据不同类型进行打印
        if isinstance(value, torch.Tensor):
            print(f"形状: {value.shape}")
            print(f"数据类型: {value.dtype}")
            print(f"设备: {value.device}")
            # 打印前几个元素
            print(f"前5个元素: {value.flatten()[:5]}")
        elif isinstance(value, np.ndarray):
            print(f"形状: {value.shape}")
            print(f"数据类型: {value.dtype}")
            # 打印前几个元素
            print(f"前5个元素: {value.flatten()[:5]}")
        elif isinstance(value, str):
            print(f"值: {value}")
        else:
            print(f"值: {value}")
        print("-")

except Exception as e:
    print(f"加载文件时出错: {e}")