cd webapp && docker build -f Dockerfile -t test-yolo-v5:dummy . && cd ..
cd companion && docker build -f Dockerfile -t test-yolo-v5-streamlit:dummy . && cd ..
