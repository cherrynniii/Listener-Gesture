import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.smplx_model import build_smplx
import torch
import trimesh

# SMPLX 모델 초기화
smplx = build_smplx()

# 예제 expression 입력
expression = torch.randn(1, 10)  # 표정 벡터
expression[0, 1] = 3.0
output = smplx(expression=expression)

# 3D 메쉬 시각화 (trimesh 사용)
verts = output.vertices[0].detach().cpu().numpy()   # output.vertices: (1, 10475, 3) -> 3D 메쉬의 vertex 좌표
faces = smplx.faces  # (어떤 vertex 3개로 표면을 구성하는지)

mesh = trimesh.Trimesh(vertices=verts, faces=faces)
mesh.visual.vertex_colors = [255, 140, 0, 255]  # 주황색으로 설정 (안 쓰면 검정색이라서 무섭다)
mesh.show()

print(output.vertices.shape)  # (1, 10475, 3)