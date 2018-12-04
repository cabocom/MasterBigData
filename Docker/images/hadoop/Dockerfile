FROM ubuntu:18.04
LABEL maintainer="Javier Gálvez <jgalvez@cabocom.com>"

# Installation
RUN apt-get clean && apt-get update -y && apt-get upgrade -y && \
	DEBIAN_FRONTEND=noninteractive apt-get install -y nano curl wget openssl git ntp cron openssh-server \
    openjdk-8-jdk \
	supervisor 

# Timezone and NTP
COPY config/ntp.conf /etc/ntp.conf

# Instalamos Hadoop
WORKDIR /tmp
RUN wget http://apache.uvigo.es/hadoop/common/hadoop-2.8.5/hadoop-2.8.5.tar.gz
RUN tar xzf hadoop-2.8.5.tar.gz -C /usr/local/
RUN rm hadoop-2.8.5.tar.gz

ENV HADOOP_HOME /usr/local/hadoop-2.8.5
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV PATH="${PATH}:${HADOOP_HOME}/bin"

# Claves ssh (ojo, posible vulnerabilidad)
COPY config/ssh/id_rsa /root/.ssh/id_rsa
COPY config/ssh/id_rsa.pub /root/.ssh/id_rsa.pub
COPY config/ssh/authorized_keys /root/.ssh/authorized_keys
RUN chmod 600 /root/.ssh/*

RUN mkdir /var/run/sshd

# Supervisor
COPY config/supervisor/supervisord.conf /etc/supervisor/supervisord.conf
COPY config/supervisor/programs.conf /etc/supervisor/conf.d/
ADD config/start.sh /root/start.sh
RUN chmod 755 /root/start.sh

# Parámetros de Docker
ENTRYPOINT ["/usr/bin/supervisord"]
