import setuptools


setuptools.setup(
    name="colabfit-cli",
    version="0.0.1",
    author="Eric Fuemmeler",
    author_email="efuemmel@umn.edu",
    description=
    "Data query and retrieval from the ColabFit Exchange",
    url="https://github.com/colabfit/colabfit-cli",
    packages=setuptools.find_packages(),
    install_requires=[
         'click>=7.0', 'pymongo', 'requests',
    ],
    python_requires='>=3.7',
    entry_points="""
    [console_scripts]
    colabfit=cli.colabfit:colabfit
    """)
