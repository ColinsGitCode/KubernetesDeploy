class KubePrometheusConst:
    KUBE_PROMETHEUS_LOCAL_PREFIX = "/root/KubernetesDeploy/MonitoringSystem"
    KUBE_PROMETHEUS_LOCAL_REPO = "/root/KubernetesDeploy/MonitoringSystem/kube-prometheus"
    KUBE_PROMETHEUS_REPO_URL = "https://github.com/prometheus-operator/kube-prometheus.git"
    KUBE_PROMETHEUS_REPO_MANIFESTS = KUBE_PROMETHEUS_LOCAL_REPO + "/manifests"

    GRAFANA_NGINX_PROXY_CONF = "/etc/nginx/conf.d/grafana.conf"
    GRAFANA_NGINX_PROXY_LISTEN_PORT = "30333"
    GRAFANA_NGINX_PROXY_PASS_IP = "192.168.49.2"
    GRAFANA_NGINX_PROXY_PASS_PORT = "30300"
    GRAFANA_SERVICE_YAML_TEMPLATE = "templates/grafana-service.yaml.j2"
    GRAFANA_SERVICE_YAML_NAME = "grafana-service.yaml"
    GRAFANA_SERVICE_YAML_SPEC_TYPE = "NodePort"
    GRAFANA_SERVICE_YAML_NODEPORT = "30300"

    PROMETHEUS_NGINX_PROXY_CONF = "/etc/nginx/conf.d/prometheus.conf"
    PROMETHEUS_NGINX_PROXY_LISTEN_PORT = "30334"
    PROMETHEUS_NGINX_PROXY_PASS_IP = "192.168.49.2"
    PROMETHEUS_NGINX_PROXY_PASS_PORT = "30090"
    PROMETHEUS_SERVICE_YAML_TEMPLATE = "templates/prometheus-service.yaml.j2"
    PROMETHEUS_SERVICE_YAML_NAME = "prometheus-service.yaml"
    PROMETHEUS_SERVICE_YAML_SPEC_TYPE = "NodePort"
    PROMETHEUS_SERVICE_YAML_NODEPORT = "30090"

    ALERTMANAGER_NGINX_PROXY_CONF = "/etc/nginx/conf.d/alertmanager.conf"
    ALERTMANAGER_NGINX_PROXY_LISTEN_PORT = "30335"
    ALERTMANAGER_NGINX_PROXY_PASS_IP = "192.168.49.2"
    ALERTMANAGER_NGINX_PROXY_PASS_PORT = "30093"
    ALERTMANAGER_SERVICE_YAML_TEMPLATE = "templates/alertmanager-service.yaml.j2"
    ALERTMANAGER_SERVICE_YAML_NAME = "alertmanager-service.yaml"
    ALERTMANAGER_SERVICE_YAML_SPEC_TYPE = "NodePort"
    ALERTMANAGER_SERVICE_YAML_NODEPORT = "30093"


class AnsibleConst:
    ANSIBLE_PROJECT = "/root/AnsibleProject"

    ANSIBLE_CFG_TEMPLATE = "templates/ansible.cfg.j2"
    ANSIBLE_CFG_FILE = "/root/AnsibleProject/ansible.cfg"

    ANSIBLE_INVENTORY_TEMPLATE = "templates/ansible_inventory.j2"
    ANSIBLE_INVENTORY_FILE = "/root/AnsibleProject/ansible_inventory"

    ANSIBLE_PLAYBOOK_DEMO_YAML_TEMPLATE = "templates/ansible_playbook_demo.yaml.j2"
    ANSIBLE_PLAYBOOK_DEMO_YAML = "/root/AnsibleProject/ansible_playbook_demo.yaml"

    TMUX_PLAYBOOK_PATH = "/root/KubernetesDeploy/AnsiblePlaybooks/playbooks/tmux"


if __name__ == "__main__":
    pass