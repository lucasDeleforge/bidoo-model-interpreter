# Start from the jupter images
FROM jupyter/scipy-notebook

# Copy thepackage files & install it
# Using pip to make it easier..
COPY . /bidoo-model-interpreter/
RUN pip install --no-index /bidoo-model-interpreter/

EXPOSE 8888

CMD jupyter lab --allow-root \
    --NotebookApp.token='' \
    --NotebookApp.password=''

