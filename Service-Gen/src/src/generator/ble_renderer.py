from numpy import NaN
from jinja2 import Environment, FileSystemLoader
from pandas import ExcelFile
from src.common.path_utils import convert_path_for_build
from src.generator.service_render_functions import UtilsBLE
from os import path

def render_ble_service_common(file_name, service_info, df, template_file, output_extension, output_path,
                              include_path=""):
    dirname = path.dirname(convert_path_for_build(__file__))
    filename = path.join(dirname, 'templates')
    file_loader = FileSystemLoader(filename)
    env = Environment(loader=file_loader, trim_blocks=True, lstrip_blocks=True)

    template = env.get_template(template_file)
    output = template.render(service_info=service_info,
                             df=df,
                             ble_util=UtilsBLE,
                             include_path=include_path)
    print(f'{output_path}/{file_name}{output_extension}')
    with open(f'{output_path}/{file_name}{output_extension}', "w") as fh:
        fh.write(output)


def render_ble_service_source(service_info, df, output_path_c="outputs/", include_relative_path="./"):
    filename = service_info["SheetName"].replace(" ", "_")
    render_ble_service_common(filename, service_info, df,
                              template_file="bleGenerationTemplate_Source.j2", output_extension=".c",
                              output_path=output_path_c, include_path=include_relative_path)


def render_ble_service_header(service_info, df, output_path_h="outputs/"):
    filename = service_info["SheetName"].replace(" ", "_")
    render_ble_service_common(filename, service_info, df,
                              template_file="bleGenerationTemplate_Header.j2", output_extension=".h",
                              output_path=output_path_h)


def render_ble_service_dart(service_info, df, output_path="outputs/"):
    filename = service_info["SheetName"].replace(" ", "")
    render_ble_service_common(filename, service_info, df,
                              template_file="bleGenerationTemplate_Dart.j2", output_extension=".dart",
                              output_path=output_path)


def execute_ble_renderer(filepath, output_path_h="outputs/", output_path_c="outputs/", include_relative_path="./"):
    xl = ExcelFile(filepath, engine='openpyxl')
    df_services = xl.parse("Services")
    for index, each_service in df_services.iterrows():
        df = xl.parse(each_service["SheetName"])
        if "Group" not in df:
            df["Group"] = NaN
        df["Group"] = df["Group"].fillna("NoGroup")  ## Workaround to change to a string! instead of handling NaN
        render_ble_service_source(service_info=each_service, df=df,
                                  output_path_c=output_path_c, include_relative_path=include_relative_path)
        render_ble_service_header(service_info=each_service, df=df, output_path_h=output_path_h)
