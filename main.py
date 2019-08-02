
def run():
    project_folder_ name = input('Enter your project folder name: ')
    if project_folder_:
        df_type = input(
            "Choose dataflow job type : batch/stream (default's to batch)")

        if df_type == 'stream':
            # set df streaming parameter
            gcp_project_id = input('Enter your gcp project if: ')
            if gcp_project_id:
                gsc_temp_location = input('Enter temp path: ')
                if gsc_temp_location:
                    df_runner = input(
                        'Enter dataflow runner type: DataflowRunner/DirectRunner')
                    if df_runner = 'DataflowRunner':
                        # create venv
                        # create requirments.txt
                        # create setup.py


if __name__ == "__main__":
    run()
