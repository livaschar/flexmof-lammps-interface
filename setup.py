from setuptools import setup, find_packages
import versioneer

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="flexmof-lammps-interface",
    author="Charalampos G. Livas",
    python_requires=">=3.6",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license="MIT",
    url="https://github.com/livaschar/flexmof-lammps-interface",  # Update the URL to your repo
    description="Automatic generation of LAMMPS input files for molecular dynamics simulations of MOFs.",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    install_requires=requirements,
    extras_require={
        'docs': ['sphinx', 'sphinx-rtd-theme'],
        'tests': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'flexmof-lammps-interface = flexmof_lammps_interface.cli:main',  # Update the entry point
        ]
    },
    include_package_data=True,
    packages=find_packages(),
)
