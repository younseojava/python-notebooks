# Set-up for PyThreeJS

Turned out pythreejs involves nodejs dependency, which is usually handled well by conda.
I.e.  simple `pip install pythreejs` gives 'model not found' error.
<br>
so, wanted to try out conda for installation, but doesn't seem to be working.
It was due to the subtle way of using Conda with Jupyter Notebook -- there is a way to select conda environment within Jupyter notebook.

### How to set up conda environment for `pythreejs`
```
$ conda create py3js-test
$ conda activate py3js-test
$ (py3js-test) conda install -c conda-forge pythreejs
$ (py3js-test) conda install ipykernel
$ (py3js-test) ipython kernel install --user --name=py3js-test
$ (py3js-test) jupyter lab --ip=0.0.0.0 --port=12088
```
Then in the notebook kernel menu, Change Kernel ..., find kernel named 'py3js-test'
<br>
Now, your Jupyter notebook is ready for `pythreejs`:

```
!jupyter labextension list

JupyterLab v3.5.2
/mnt/beegfs/home/yroh/.local/share/jupyter/labextensions
        jupyter-threejs v2.4.0 enabled OK (python, pythreejs)
        jupyter-leaflet v0.17.2 enabled OK
        jupyterlab-datawidgets v7.1.2 enabled OK
        jupyterlab-plotly v5.10.0 enabled OK
        jupyterlab_pygments v0.2.2 enabled OK (python, jupyterlab_pygments)
        @jupyter-widgets/jupyterlab-manager v3.1.1 enabled OK (python, jupyterlab_widgets)

Other labextensions (built into JupyterLab)
   app dir: /mnt/beegfs/home/yroh/.local/share/jupyter/lab
```
