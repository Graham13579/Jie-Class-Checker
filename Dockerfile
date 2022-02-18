FROM amazon/aws-lambda-python:3.8 as lambda-base

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

# Install the function's dependencies using file requirements.txt
# from your project folder.

COPY requirements.txt  .
COPY install-browsers.sh .

RUN yum install xz atk cups-libs gtk3 libXcomposite alsa-lib tar \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt xorg-x11-server-Xvfb \
    xorg-x11-xauth dbus-glib dbus-glib-devel unzip bzip2 -y -q

RUN /usr/bin/bash install-browsers.sh

RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

RUN yum remove xz tar unzip bzip2 -y

FROM lambda-base 

COPY app.py /var/task/

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]