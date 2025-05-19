from smplx import SMPLX

# 외부 인체 모델인 SMPLX를 초기화하기 위한 설정
def build_smplx(gender='neutral'):
    model_path = 'data/smplx'
    smplx_model = SMPLX(
        model_path=model_path,
        model_type='smplx',
        gender=gender,
        ext='pkl',
        num_betas=10,
        use_face_contour=True
    )
    return smplx_model
