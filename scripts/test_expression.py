import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("▶ sys.executable:", sys.executable)

from models.smplx_model import build_smplx
import torch

# SMPLX 모델 초기화
smplx = build_smplx()

# 예제 expression 입력
expression = torch.randn(1, 10)  # 표정 벡터
output = smplx(expression=expression)

print(output.vertices.shape)  # (1, 10475, 3)
