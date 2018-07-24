from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='bella_tdsa',
      version='0.1.0',
      description='Target Dependent Sentiment Analysis (TDSA) framework.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/apmoore1/Bella',
      author='Andrew Moore',
      author_email='andrew.p.moore94@gmail.com',
      license='MIT',
      install_requires=[
          'Babel==2.5.1',
          'bleach==1.5.0',
          'boto==2.48.0',
          'bz2file==0.98',
          'certifi==2017.7.27.1',
          'chardet==3.0.4',
          'cycler==0.10.0',
          'decorator==4.1.2',
          'distro==1.3.0',
          'docutils==0.14',
          'entrypoints==0.2.3',
          'enum34==1.1.6',
          'ftfy==5.2.0',
          'gensim==3.0.1',
          'google-compute-engine==2.8.2',
          'graphviz==0.8.2',
          'h5py==2.7.1',
          'html5lib==0.9999999',
          'idna==2.6',
          'imagesize==0.7.1',
          'ipykernel==4.6.1',
          'ipython==6.2.1',
          'ipython-genutils==0.2.0',
          'ipywidgets==7.0.4',
          'jedi==0.11.0',
          'Jinja2==2.9.6',
          'jsonschema==2.6.0',
          'jupyter==1.0.0',
          'Keras==2.1.3',
          'lxml==4.1.1',
          'Markdown==2.6.9',
          'MarkupSafe==1.0',
          'matplotlib==2.1.1',
          'mistune==0.8.1',
          'nbconvert==5.3.1',
          'nbformat==4.4.0',
          'networkx==2.0',
          'nltk==3.2.5',
          'notebook>=5.6.0',
          'numpy==1.13.3',
          'pandas==0.21.0',
          'pandocfilters==1.4.2',
          'parso==0.1.0',
          'pexpect==4.3.0',
          'pickleshare==0.7.4',
          'prompt-toolkit==1.0.15',
          'protobuf==3.5.0.post1',
          'psutil==5.4.3',
          'ptyprocess==0.5.2',
          'pydot==1.2.4',
          'Pygments==2.2.0',
          'pyparsing==2.2.0',
          'python-dateutil==2.6.1',
          'pytz==2017.2',
          'PyYAML==3.12',
          'pyzmq>=17.1.0',
          'qtconsole==4.3.1',
          'requests==2.18.4',
          'ruamel.yaml==0.15.34',
          'scikit-learn==0.19.1',
          'scipy==1.0.0',
          'seaborn==0.8.1',
          'simplegeneric==0.8.1',
          'smart-open==1.5.3',
          'snowballstemmer==1.2.1',
          'stanfordcorenlp==3.7.0.2',
          'tensorflow==1.3.0',
          'tensorflow-tensorboard==0.1.8',
          'terminado>=0.8.1',
          'testpath==0.3.1',
          'tornado==4.5.2',
          'traitlets==4.3.2',
          'tweebo-parser-python-api==1.0.2',
          'wcwidth==0.1.7',
          'webencodings==0.5.1',
          'Werkzeug==0.12.2',
          'widgetsnbextension==3.0.7',
          'twokenize==1.0.0',
          'tqdm==4.23.4'
      ],
      python_requires='>=3.6',
      packages=find_packages(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 3.6',
          'Topic :: Text Processing',
          'Topic :: Text Processing :: Linguistic',
      ])
