from setuptools import setup, find_packages

setup(
    name="mask-detector",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'numpy>=2.0.0',
        'pandas>=1.3.0',
        'torch>=1.9.0',
        'torchvision>=0.10.0',
        'tensorflow>=2.12.0',
        'keras>=2.6.0',
        'matplotlib>=3.4.0',
        'seaborn>=0.11.0',
        'notebook>=6.4.0',
        'opencv-python>=4.5.0',
        'scikit-learn>=0.24.0',
        'scipy>=1.7.0',
        'imutils'
    ],
    python_requires='<3.13',
)