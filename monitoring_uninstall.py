from utils_tools import CmdExecutor, AptGetUtils
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
    def nginx_uninstall() -> None:
        nginx_stop_cmd = "nginx -s quit"
        CmdExecutor.exec_cmd(nginx_stop_cmd)

        rm_cmd = "rm -rf /etc/nginx"
        CmdExecutor.exec_cmd(rm_cmd)

        AptGetUtils.uninstall(["nginx", "nginx-common"])

    @staticmethod
    def process() -> None:
        UninstallMonitoring.nginx_uninstall()
        UninstallMonitoring.kubectl_delete_monitoring()
        UninstallMonitoring.remove_kube_prometheus_repo()


if __name__ == "__main__":
    print("Uninstalling Kube-prometheus.........")
    UninstallMonitoring.process()
    # UninstallMonitoring.nginx_uninstall()
