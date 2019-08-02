

def run():
    project_folder_name = input('Enter your project folder name: ')
    if project_folder_name:
        df_type = input(
            "Choose dataflow job type : batch/stream (default's to batch)")

        if df_type == 'stream':
            # set df streaming parameter
            pass

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


if __name__ == "__main__":
    run()
