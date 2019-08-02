import json


def generate_dataflow_configuration(*args):
    if args[2] == 'stream':
        streaming = True
    else:
        streaming = False

    config = {
        "project": args[0],
        "temp_location": args[1],
        "streaming": streaming,
        "runner": args[3],
        "read_gsc_location": args[4],
        "bq_dataset": args[5],
        "bq_table": args[6],
        "setup_file": args[0]+'/setup.py'
    }
    return config


def run():
    flag = False
    project_folder_name = input('Enter your project folder name: ')
    if project_folder_name:
        df_type = input(
            "Choose dataflow job type : batch/stream (default's to batch)")

        if df_type == 'stream':
            # set df streaming parameter
            pass
        df_type = 'batch'

        gcp_project_id = input('Enter your gcp project id: ')
        if gcp_project_id:
            gsc_temp_location = input('Enter gcs temp path location: ')
            if gsc_temp_location:
                df_runner = input(
                    'Enter dataflow runner type: DataflowRunner/DirectRunner: ')

                type_of_df = input("Default to 1. GCS to BiqQuery: ")
                type_of_df = '1'
                if type_of_df == '1':
                    read_gsc_location = input(
                        'Enter gcs location path: ')
                    bq_dataset = input(
                        'Enter big query dataset name: ')
                    bq_table = input(
                        'Enter big query table name: ')
                    flag = True

    if flag == True:
        config = generate_dataflow_configuration(
            gcp_project_id, gsc_temp_location, df_type, df_runner, read_gsc_location, bq_dataset, bq_table)

        with open('/Users/cloudcover-vaibhav/python-dataflow-generator/app_code/config/mapping.json', 'w') as p:
            json.dump(config, p)


if __name__ == "__main__":
    run()
