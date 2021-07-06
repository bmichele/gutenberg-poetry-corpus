from setuptools import setup
    
with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='gutenbergpoetrycorpus',
    version='0.0.1',
    author='Allison Parrish',
    author_email='allison@decontextualize.com',
    url='https://github.com/aparrish/gutenberg-poetry-corpus',
    description='A corpus of poetry from Project Gutenberg',
    long_description=readme,
    packages=setuptools.find_packages(),
    install_requires=[
        'wordfilter==0.2.6.2'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        'Programming Language :: Python :: 3',
    ],
    platforms='any',
)
