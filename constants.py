class KubePrometheusConst:
    KUBE_PROMETHEUS_LOCAL_PREFIX = "/root/KubernetesDeploy/MonitoringSystem"
    KUBE_PROMETHEUS_LOCAL_REPO = "/root/KubernetesDeploy/MonitoringSystem/kube-prometheus"
    KUBE_PROMETHEUS_REPO_URL = "https://github.com/prometheus-operator/kube-prometheus.git"
    KUBE_PROMETHEUS_REPO_MANIFESTS = KUBE_PROMETHEUS_LOCAL_REPO + "/manifests"

    GRAFANA_NGINX_PROXY_CONF = "/etc/nginx/conf.d/grafana.conf"
    PROMETHEUS_NGINX_PROXY_CONF = "/etc/nginx/conf.d/prometheus.conf"
    ALERTMANAGER_NGINX_PROXY_CONF = "/etc/nginx/conf.d/alertmanager.conf"


if __name__ == "__main__":
    pass