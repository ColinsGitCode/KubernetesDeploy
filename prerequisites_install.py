from utils_tools import CmdExecutor


class PrerequisitesInstall:
    @staticmethod
    def install_yq() -> None:
        # Install yq
        install_yq_cmd = 'snap install yq'
        CmdExecutor.exec_cmd(install_yq_cmd)

    @staticmethod
    def install_kubectl() -> None:
        # Install kubectl
        install_kubectl_cmd = 'snap install kubectl --classic'
        CmdExecutor.exec_cmd(install_kubectl_cmd)

    @staticmethod
    def install_skopeo() -> None:
        # Install skopeo
        install_skopeo_cmd = "apt-get install skopeo -y"
        CmdExecutor.exec_cmd(install_skopeo_cmd)

    @staticmethod
    def install_helm() -> None:
        # Install helm
        curl_cmd = "curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | tee /usr/share/keyrings/helm.gpg > /dev/null"
        CmdExecutor.exec_cmd(curl_cmd)

        apt_get_install_cmd = "apt-get install apt-transport-https --yes"
        CmdExecutor.exec_cmd(apt_get_install_cmd)

        echo_cmd = 'echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | tee /etc/apt/sources.list.d/helm-stable-debian.list'
        CmdExecutor.exec_cmd(echo_cmd)

        apt_get_update_cmd = "apt-get update"
        CmdExecutor.exec_cmd(apt_get_update_cmd)

        apt_get_install_cmd = "apt-get install helm -y"
        CmdExecutor.exec_cmd(apt_get_install_cmd)

        link_cmd = "ln -s /usr/bin/helm /usr/local/bin/"
        CmdExecutor.exec_cmd(link_cmd)

    @staticmethod
    def install_kind() -> None:
        curl_cmd = "curl -Lo /root/kind https://qiniu-download-public.daocloud.io/kind/v0.17.0/kind-linux-amd64"
        CmdExecutor.exec_cmd(curl_cmd)

        chmod_cmd = "chmod +x /root/kind"
        CmdExecutor.exec_cmd(chmod_cmd)

        mv_cmd = "mv /root/kind /usr/bin/kind"
        CmdExecutor.exec_cmd(mv_cmd)

        kind_version_cmd = "kind version"
        CmdExecutor.exec_cmd(kind_version_cmd)

    @staticmethod
    def install_docker() -> None:
        install_docker_cmd = "apt-get install docker-ce -y"
        CmdExecutor.exec_cmd(install_docker_cmd)

        start_docker_cmd = "service docker start"
        CmdExecutor.exec_cmd(start_docker_cmd)

        systemctl_cmd = "systemctl enable docker"
        CmdExecutor.exec_cmd(systemctl_cmd)

        docker_version_cmd = "docker version"
        CmdExecutor.exec_cmd(docker_version_cmd)

    @staticmethod
    def process() -> None:
        PrerequisitesInstall.install_docker()
        PrerequisitesInstall.install_kind()
        PrerequisitesInstall.install_yq()
        PrerequisitesInstall.install_kubectl()
        PrerequisitesInstall.install_skopeo()
        PrerequisitesInstall.install_helm()


if __name__ == "__main__":
    print("Running prerequisites install...")
    PrerequisitesInstall.process()
    print("Finishing prerequisites install...")

