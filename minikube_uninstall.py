import time
from utils_tools import CmdExecutor


class UninstallMinikube:
    @staticmethod
    def process() -> None:
        """
        The Process of Uninstalling Minikube
        1. Stop Minikube: minikube stop
        2. Delete Minikube Nodes: minikube delete
        3. Remove Minikube Packages: dpkg --remove minikube
        4. Remove Minikube Files: rm -rf /var/lib/minikube

        :return: None
        """
        cmd_list = [
            "minikube stop",
            "minikube delete",
            "dpkg --remove minikube",
            "rm -rf /var/lib/minikube"
        ]

        for cmd in cmd_list:
            CmdExecutor.exec_cmd(cmd)
            CmdExecutor.wait_countdown(10)


if __name__ == "__main__":
    print("Uninstalling Minikube......")
    UninstallMinikube.process()