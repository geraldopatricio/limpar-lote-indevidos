FROM python:3.8-buster
RUN mkdir /webapps
WORKDIR /webapps

RUN pip install requests \
                azure.keyvault.secrets \
                azure.identity \ 
                pandas \
                openpyxl
ADD . /webapps/
CMD [ "python", "./src/procedimento_bloquear_cartoes.py" ]