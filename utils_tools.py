import os
from jinja2 import Environment, FileSystemLoader


class UtilsJinja2:
    @staticmethod
    def create_file_from_template(j2_path, data_dict, file_path):
        # Create a Jinja2 environment
        env = Environment(loader=FileSystemLoader("."))

        # Load the template
        template = env.get_template(j2_path)

        # Provide data to render the template
        # data = {"name": "John"}

        # Render the template with data
        output = template.render(data_dict)

        # Save the rendered output to a new file
        with open(file_path, "w") as f:
            f.write(output)


class CmdExecutor:
    @staticmethod
    def exec_cmd(cmd: str) -> None:
        print("-------------------------------------------------")
        print("Executing: " + cmd)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        os.system(cmd)
        print("Finished: " + cmd)
        print("************************************************")
        print()



if __name__ == "__main__":
    j2_template_path = "../templates/prometheus-service.yaml.j2"
    result_file_path = "/root/KubernetesDeploy/Templates/prometheus-service.yaml"
    UtilsJinja2.create_file_from_template(j2_template_path, {}, result_file_path)