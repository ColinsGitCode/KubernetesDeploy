from utils_tools import CmdExecutor
import time


class InstallMinikube:
    @staticmethod
    def process() -> None:
        """
        The process of Install Minikube
        1. Download Minikube deb package: curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
        2. Install Minikube deb package by using dkpg: dpkg -i minikube_latest_amd64.deb
        3. Minikube start with 3 nodes and k8s v1.23.0
            minikube start --nodes=3 --force --kubernetes-version=v1.23.0 --extra-config=kubelet.authentication-token-webhook=true --extra-config=kubelet.authorization-mode=Webhook
        4. Minikube start check: minikube kubectl -- get pods -A
        5. Minikube Dashboard Start: minikube dashboard &
        6. Kubectl Proxy: kubectl proxy --port=31000 --address='192.168.100.81' --accept-hosts='^.*' &

        :return: None
        """
        cmd_list = [
            "curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb",
            "dpkg -i minikube_latest_amd64.deb",
            "minikube start --nodes=3 --force --kubernetes-version=v1.23.0 --extra-config=kubelet.authentication-token-webhook=true --extra-config=kubelet.authorization-mode=Webhook",
            "minikube kubectl -- get pods -A",
            "minikube dashboard &",
            "kubectl proxy --port=31000 --address='192.168.100.81' --accept-hosts='^.*' &",
        ]

        for cmd in cmd_list:
            CmdExecutor.exec_cmd(cmd)
            time.sleep(30)


if __name__ == "__main__":
    print("Installing Minikube......")
    InstallMinikube.process()