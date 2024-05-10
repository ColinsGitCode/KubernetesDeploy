from utils_tools import CmdExecutor


class PrerequisitesUninstall:
    @staticmethod
    def uninstall_yq() -> None:
        # Remove yq
        rm_yq_cmd = "snap remove yq"
        CmdExecutor.exec_cmd(rm_yq_cmd)

    @staticmethod
    def uninstall_kubectl() -> None:
        # Remove kubectl
        rm_kubectl_cmd = "snap remove kubectl"
        CmdExecutor.exec_cmd(rm_kubectl_cmd)

    @staticmethod
    def uninstall_skopeo() -> None:
        # Remove skopeo
        rm_skopeo_cmd = "apt-get remove skopeo -y"
        CmdExecutor.exec_cmd(rm_skopeo_cmd)

    @staticmethod
    def uninstall_helm() -> None:
        # Remove helm
        rm_helm_cmd = "apt-get remove helm -y"
        CmdExecutor.exec_cmd(rm_helm_cmd)

        rm_link_cm = "rm -rf /usr/local/bin/helm"
        CmdExecutor.exec_cmd(rm_link_cm)

    @staticmethod
    def uninstall_kind() -> None:
        # Delete kind
        rm_kind_cmd = "rm -rf /usr/bin/kind"
        CmdExecutor.exec_cmd(rm_kind_cmd)

    @staticmethod
    def uninstall_docker() -> None:
        stop_docker_cmd = "systemctl stop docker"
        CmdExecutor.exec_cmd(stop_docker_cmd)

        uninstall_docker_cmd_list = [
            "rm",
            "apt-get purge -y docker-ce",
            "apt-get purge -y docker-ce-cli",
            "apt-get purge -y containerd.io",
            "apt-get purge -y docker-buildx-plugin",
            "apt-get purge -y docker-compose-plugin",
            "apt-get purge -y docker-ce-rootless-extras",
            "rm -rf /var/lib/docker",
            "rm -rf /var/lib/containerd",
            "rm -rf /usr/bin/docker"
        ]
        for cmd in uninstall_docker_cmd_list:
            CmdExecutor.exec_cmd(cmd)


    @staticmethod
    def process() -> None:
        # PrerequisitesUninstall.uninstall_helm()
        # PrerequisitesUninstall.uninstall_skopeo()
        # PrerequisitesUninstall.uninstall_kubectl()
        # PrerequisitesUninstall.uninstall_yq()
        # PrerequisitesUninstall.uninstall_kind()
        PrerequisitesUninstall.uninstall_docker()


if __name__ == "__main__":
    print("Uninstalling Prerequisites.......")
    PrerequisitesUninstall.process()