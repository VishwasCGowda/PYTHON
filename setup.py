from io import open
from setuptools import setup
from auto_py_to_exe import __version__ as version

setup(
    name='personal_assistance',
    version=version,
    url='https://github.com/VISHWAS-c-dot/PYTHON',
    license='MIT',
    author='Vishwas c',
    author_email='vishwas@varzsecurity.com',
    description='Converts .py to .exe using a simple graphical interface.',
    long_description=''.join(open('README.md', encoding='utf-8').readlines()),
    long_description_content_type='text/markdown',
    keywords=['gui', 'executable'],
    packages=['personal_assistance'],
    include_package_data=True,
    install_requires=['pyttsx3'],
    install_requires=['SpeechRecognition'],
    install_requires=['pyjokes'],
    install_requires=['wikipedia'],
    python_requires='>=3.5',
    classifiers=[
        'License :: OSI Approved :varz security',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
    ],
    entry_points={
        'console_scripts': [
            'autopytoexepersonal_assistance.__main__:run',
            'personal_assistance=personal_assistance.__main__:run'
        ],
    },
)
