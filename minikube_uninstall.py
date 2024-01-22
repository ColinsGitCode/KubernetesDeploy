import time

from utils_tools import CmdExecutor


class UninstallMinikube:
    @staticmethod
    def process() -> None:
        cmd_list = [
            "minikube stop",
            "minikube delete",
            "dpkg --remove minikube",
            "rm -rf /var/lib/minikube"
        ]

        for cmd in cmd_list:
            CmdExecutor.exec_cmd(cmd)
            time.sleep(10)


if __name__ == "__main__":
    print("Uninstalling Minikube......")
    UninstallMinikube.process()