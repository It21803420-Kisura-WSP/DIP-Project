import kagglehub

# Download the latest version of the model
path = kagglehub.model_download("kaggle/maxim/tensorFlow2/s-3-denoising-sidd")

print("Path to model files:", path)
