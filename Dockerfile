FROM jupyter/datascience-notebook

USER $NB_UID
WORKDIR /home/jovyan/work
RUN pip install requests && \
	pip install pdfminer.six
COPY . .

