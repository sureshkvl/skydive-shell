from setuptools import setup

setup(
    name="skydive Shell",
    version="0.1",
    entry_points={
        'console_scripts': [
            'skydive-shell = skydive_shell.shell:main',
        ],
    },
    install_requires=[
        'prompt-toolkit',
        'lark-parser',
        'pygments'
    ],
    test_suite="tests",
    author="lewo",
    author_email="lewo@abesis.fr",
)
