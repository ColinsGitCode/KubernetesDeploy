import time
from utils_tools import CmdExecutor


class StartMinikube:
    @staticmethod
    def process() -> None:
        """
        The process of Install Minikube
        1. Minikube start with 3 nodes and k8s v1.23.0
            minikube start --nodes=3 --force --kubernetes-version=v1.23.0 --extra-config=kubelet.authentication-token-webhook=true --extra-config=kubelet.authorization-mode=Webhook
        2. Minikube start check: minikube kubectl -- get pods -A
        3. Minikube Dashboard Start: minikube dashboard &
        4. Kubectl Proxy: kubectl proxy --port=31000 --address='192.168.100.81' --accept-hosts='^.*' &

        :return: None
        """
        cmd_list = [
            "minikube start --nodes=3 --force --kubernetes-version=v1.23.0 --extra-config=kubelet.authentication-token-webhook=true --extra-config=kubelet.authorization-mode=Webhook",
            "minikube kubectl -- get pods -A",
            "minikube dashboard &",
            "kubectl proxy --port=31000 --address='192.168.100.81' --accept-hosts='^.*' &",
        ]

        for cmd in cmd_list:
            CmdExecutor.exec_cmd(cmd)
            CmdExecutor.wait_countdown(30)


if __name__ == "__main__":
    print("Starting Minikube......")
    StartMinikube.process()