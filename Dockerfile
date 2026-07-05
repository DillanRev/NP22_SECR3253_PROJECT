FROM debian:bullseye
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y openssh-server python3 sudo sysstat iproute2

RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN useradd -rm -d /home/ansible_user -s /bin/bash -g root -G sudo -u 1000 ansible_user
RUN echo 'ansible_user:utmpassword123' | chpasswd
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]