from utils_tools import CmdExecutor, UtilsJinja2
from constants import KubePrometheusConst
import time


class InstallMonitoring:
    @staticmethod
    def kube_prometheus_repo_process() -> None:
        git_cmd = "git clone " + KubePrometheusConst.KUBE_PROMETHEUS_REPO_URL + " " + KubePrometheusConst.KUBE_PROMETHEUS_LOCAL_PREFIX + "/kube-prometheus"
        CmdExecutor.exec_cmd(git_cmd)

        prometheus_service_j2_path = "templates/prometheus-service.yaml.j2"
        prometheus_service_yaml_path = KubePrometheusConst.KUBE_PROMETHEUS_REPO_MANIFESTS + "/prometheus-service.yaml"
        UtilsJinja2.create_file_from_template(prometheus_service_j2_path, {}, prometheus_service_yaml_path)
        cmd = "ls -lht " + prometheus_service_yaml_path
        CmdExecutor.exec_cmd(cmd)

        grafana_service_j2_path = "templates/grafana-service.yaml.j2"
        grafana_service_yaml_path = KubePrometheusConst.KUBE_PROMETHEUS_REPO_MANIFESTS + "/grafana-service.yaml"
        UtilsJinja2.create_file_from_template(grafana_service_j2_path, {}, grafana_service_yaml_path)
        cmd = "ls -lht " + grafana_service_yaml_path
        CmdExecutor.exec_cmd(cmd)

        alertmanager_service_j2_path = "templates/alertmanager-service.yaml.j2"
        alertmanager_service_yaml_path = KubePrometheusConst.KUBE_PROMETHEUS_REPO_MANIFESTS + "/alertmanager-service.yaml"
        UtilsJinja2.create_file_from_template(alertmanager_service_j2_path, {}, alertmanager_service_yaml_path)
        cmd = "ls -lht " + alertmanager_service_yaml_path
        CmdExecutor.exec_cmd(cmd)

    @staticmethod
    def kubectl_apply_kube_prometheus() -> None:
        cmd = "kubectl apply --server-side -f " + KubePrometheusConst.KUBE_PROMETHEUS_REPO_MANIFESTS + "/setup"
        CmdExecutor.exec_cmd(cmd)

        cmd = "kubectl wait --for condition=Established --all CustomResourceDefinition --namespace=monitoring"
        CmdExecutor.exec_cmd(cmd)

        cmd = "kubectl apply -f " + KubePrometheusConst.KUBE_PROMETHEUS_REPO_MANIFESTS + "/"
        CmdExecutor.exec_cmd(cmd)

        cmd = "kubectl get all -n monitoring"
        CmdExecutor.exec_cmd(cmd)

        cmd = "minikube service list"
        CmdExecutor.exec_cmd(cmd)

    @staticmethod
    def nginx_process() -> None:
        install_nginx_cmd = "apt-get install -y nginx"
        CmdExecutor.exec_cmd(install_nginx_cmd)

        grafana_nginx_conf_j2_path = "templates/grafana.conf.j2"
        grafana_nginx_conf_path = KubePrometheusConst.GRAFANA_NGINX_PROXY_CONF
        UtilsJinja2.create_file_from_template(grafana_nginx_conf_j2_path, {}, grafana_nginx_conf_path)

        prometheus_nginx_conf_j2_path = "templates/prometheus.conf.j2"
        prometheus_nginx_conf_path = KubePrometheusConst.PROMETHEUS_NGINX_PROXY_CONF
        UtilsJinja2.create_file_from_template(prometheus_nginx_conf_j2_path, {}, prometheus_nginx_conf_path)

        alertmanager_nginx_conf_j2_path = "templates/alertmanager.conf.j2"
        alertmanager_nginx_conf_path = KubePrometheusConst.ALERTMANAGER_NGINX_PROXY_CONF
        UtilsJinja2.create_file_from_template(alertmanager_nginx_conf_j2_path, {}, alertmanager_nginx_conf_path)

        nginx_test_cmd = "nginx -t"
        CmdExecutor.exec_cmd(nginx_test_cmd)

        nginx_reload_cmd = "nginx -s reload"
        CmdExecutor.exec_cmd(nginx_reload_cmd)

    @staticmethod
    def process() -> None:
        """
        The process of installing the monitoring
        1. git clone kube-prometheus:
        2.
        3.
        :return:
        """
        InstallMonitoring.kube_prometheus_repo_process()
        InstallMonitoring.kubectl_apply_kube_prometheus()
        InstallMonitoring.nginx_process()


if __name__ == '__main__':
    print("Installing Kubernetes Cluster Monitoring")
    InstallMonitoring.process()
    # InstallMonitoring.nginx_process()
