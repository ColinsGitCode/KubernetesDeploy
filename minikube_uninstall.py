from Utils import CmdExecutor


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


if __name__ == "__main__":
    print("Uninstalling Minikube......")
    UninstallMinikube.process()