# Listener-Gesture

project-name/
├── configs/ # YAML/JSON 구성파일 (하이퍼파라미터, 모델 설정)
├── data/ # (보통 비워두고) 데이터 저장 위치로 사용됨
├── datasets/ # PyTorch Dataset 정의
├── models/ # 모델 클래스 정의
├── trainers/ # 학습/검증 루프 로직
├── losses/ # 손실 함수 정의
├── metrics/ # 평가 지표 (예: FID, BLEU 등)
├── utils/ # 헬퍼 함수, 로깅, 시각화 등
├── scripts/ # 학습/추론/전처리 실행 스크립트
├── requirements.txt
├── README.md
├── .gitignore
