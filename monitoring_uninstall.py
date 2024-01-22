from utils_tools import CmdExecutor
from constants import KubePrometheusConst


class UninstallMonitoring:
    @staticmethod
    def remove_kube_prometheus_repo() -> None:
        cmd = "rm -rf " + KubePrometheusConst.KUBE_PROMETHEUS_LOCAL_REPO
        CmdExecutor.exec_cmd(cmd)

    @staticmethod
    def kubectl_delete_monitoring() -> None:
        cmd = "kubectl delete --ignore-not-found=true -f " + KubePrometheusConst.KUBE_PROMETHEUS_REPO_MANIFESTS + "/ -f " + KubePrometheusConst.KUBE_PROMETHEUS_REPO_MANIFESTS + "/setup"
        CmdExecutor.exec_cmd(cmd)

    @staticmethod
    def process() -> None:
        UninstallMonitoring.kubectl_delete_monitoring()
        UninstallMonitoring.remove_kube_prometheus_repo()


if __name__ == "__main__":
    print("Uninstalling Kube-prometheus.........")
    UninstallMonitoring.process()