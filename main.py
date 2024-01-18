from utils_tools import UtilsJinja2

if __name__ == '__main__':
    j2_template_path = "templates/prometheus-service.yaml.j2"
    result_file_path = "/root/KubernetesDeploy/templates/prometheus-service.yaml"
    UtilsJinja2.create_file_from_template(j2_template_path, {}, result_file_path)
