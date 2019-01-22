# Esta imagen está construido a partir de la imagen hadoop construida tambien en este mismo proyecto
FROM hadoop:ubuntu18.04
LABEL maintainer="Javier Gálvez <jgalvez@cabocom.com>"

# Instalamos Scala
RUN wget https://www.scala-lang.org/files/archive/scala-2.12.7.tgz
RUN tar xzf scala-2.12.7.tgz -C /usr/local/
RUN rm scala-2.12.7.tgz

# Instalamos Spark
RUN wget http://apache.uvigo.es/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz
RUN tar xzf spark-2.4.0-bin-hadoop2.7.tgz -C /usr/local/
RUN rm spark-2.4.0-bin-hadoop2.7.tgz

# Configuramos variables de entorno
ENV SCALA_HOME /usr/local/scala-2.12.7
ENV SPARK_HOME /usr/local/spark-2.4.0-bin-hadoop2.7
ENV PATH="${PATH}:${SCALA_HOME}/bin:${SPARK_HOME}/bin"
