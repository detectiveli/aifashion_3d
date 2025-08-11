import torch
import joblib
import numpy as np
import os
import sys
import os

# 添加SMPL-Anthropometry-master目录到Python路径的开头
smpl_anthropometry_path = os.path.abspath('SMPL-Anthropometry-master')
sys.path.insert(0, smpl_anthropometry_path)

# 从SMPL-Anthropometry-master目录导入模块
from measure import MeasureBody
from measurement_definitions import STANDARD_LABELS
# 确保使用SMPL-Anthropometry-master目录中的utils
import utils as smpl_utils
# 将smpl_utils添加到全局命名空间，以便其他模块可以使用
import builtins
builtins.utils = smpl_utils
from pprint import pprint

# 不加载pkl文件，使用默认参数
import torch

try:
    # 设置默认参数
    gender = 'neutral'
    # 创建10个零值的betas参数
    betas = torch.zeros((1, 10))

    print(f"使用默认性别: {gender}")
    print(f"使用默认betas形状: {betas.shape}")

    # 创建SMPLX测量器
    print("创建SMPLX测量器...")
    # 添加调试信息，检查模型文件路径
    import inspect
    # 检查MeasureBody类的实现
    # print("检查MeasureBody类的实现...")
    # print(f"MeasureBody模块路径: {inspect.getfile(MeasureBody)}")
    # 手动检查模型文件路径
    model_root = os.path.abspath('data/body_models')
    model_type = 'smplx'
    gender_upper = gender.upper()
    npz_model_path = os.path.join(model_root, model_type, f'{model_type.upper()}_{gender_upper}.npz')
    pkl_model_path = os.path.join(model_root, model_type, f'{model_type.upper()}_{gender_upper}.pkl')
    # print(f"模型根目录: {model_root}")
    # print(f"检查.npz模型文件: {npz_model_path}")
    # print(f".npz文件存在: {os.path.exists(npz_model_path)}")
    # print(f"检查.pkl模型文件: {pkl_model_path}")
    # print(f".pkl文件存在: {os.path.exists(pkl_model_path)}")
    # 创建测量器
    measurer = MeasureBody('smplx')

    # 使用body model参数初始化
    # print("初始化测量器...")
    measurer.from_body_model(gender=gender, shape=betas)

    # 进行测量
    print("开始测量...")
    measurement_names = measurer.all_possible_measurements
    measurer.measure(measurement_names)

    # 输出测量结果
    print("\n--- 测量结果 ---")
    pprint(measurer.measurements)

    # 输出标记测量结果
    print("\n--- 标记测量结果 ---")
    measurer.label_measurements(STANDARD_LABELS)
    pprint(measurer.labeled_measurements)

except Exception as e:
    print(f"发生错误: {e}")