FROM jupyter/scipy-notebook

EXPOSE 8888

CMD jupyterlab --allow-root \
    --NotebookApp.token='' \
    --NotebookApp.password=''

