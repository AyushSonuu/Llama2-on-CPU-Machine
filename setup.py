from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements():
    req: List = []
    with open("requirements.txt", "r") as f:
        for line in f:
            if not line.startswith(HYPHEN_E_DOT):
                req.append(line.strip())
    return req


setup(
    name='Llama2-on-CPU-Machine',
    version='0.0.1',
    # packages=['src'],
    url='https://github.com/AyushSonuu/Llama2-on-CPU-Machine',
    license='MIT',
    author='AYUSH',
    author_email='ayush.sonu@impressico.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)
