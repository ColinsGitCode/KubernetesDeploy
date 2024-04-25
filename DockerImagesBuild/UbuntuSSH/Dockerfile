# 最新バージョンの Ubuntu システムをプルします
# Pull the latest verison of Ubuntu OS
FROM ubuntu:latest

# 必要なソフトウェアをインストールする
# Install the necessary softwares
RUN apt-get update \
    && apt-get install -y openssh-server \
    && apt-get install -y net-tools \
    && apt-get install -y iproute2 \
    && apt-get install -y vim \
    && apt-get install -y systemctl \
    && apt-get install -y curl

# SSH サービスを有効にし、外部 SSH アクセスを許可します
# Enable SSH service and allow external SSH access
## 1. Create sshd dictionary
## 1. sshd ディクショナリを作成する
RUN mkdir /var/run/sshd

## ２．SSH アクセス用の root パスワードを設定します (希望のパスワードに変更します)。
## ２．Set root password for SSH access (change to your desired password)
RUN echo 'root:msd00000' | chpasswd

## 3. sshd_config と /etc/pam.d/sshを設置する['
## 3. Setting sshd_config and /etc/pam.d/ssh
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication yes/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# 22 ポートを外部アクセス用に公開する
# Expose 22 port for external access
EXPOSE 22

# sshd　サービスを稼働する
# Start sshd service
CMD ["/usr/sbin/sshd", "-D"]