import subprocess

from celery import signals
from celery.utils.log import get_task_logger

# API docs - https://openrelik.github.io/openrelik-worker-common/openrelik_worker_common/index.html
from openrelik_worker_common.file_utils import create_output_file
from openrelik_worker_common.logging import Logger
from openrelik_worker_common.task_utils import create_task_result, get_input_files

from .app import celery

# Task name used to register and route the task to the correct queue.
TASK_NAME = "openrelik-worker-TEMPLATEWORKERNAME.tasks.your_task_name"

# Task metadata for registration in the core system.
TASK_METADATA = {
    "display_name": "openrelik-worker-TEMPLATEWORKERNAME",
    "description": "TEMPLATEDESC",
    # Configuration that will be rendered as a web for in the UI, and any data entered
    # by the user will be available to the task function when executing (task_config).
    "task_config": [
        {
            "name": "<REPLACE_WITH_NAME>",
            "label": "<REPLACE_WITH_LABEL>",
            "description": "<REPLACE_WITH_DESCRIPTION>",
            "type": "<REPLACE_WITH_TYPE>",  # Types supported: text, textarea, checkbox
            "required": False,
        },
    ],
}

log_root = Logger()
logger = log_root.get_logger(__name__, get_task_logger(__name__))

@signals.task_prerun.connect
def on_task_prerun(sender, task_id, task, args, kwargs, **_):
    log_root.bind(
        task_id=task_id,
        task_name=task.name,
        worker_name=TASK_METADATA.get("display_name"),
    )

@celery.task(bind=True, name=TASK_NAME, metadata=TASK_METADATA)
def command(
    self,
    pipe_result: str = None,
    input_files: list = None,
    output_path: str = None,
    workflow_id: str = None,
    task_config: dict = None,
) -> str:
    """Run <REPLACE_WITH_COMMAND> on input files.

    Args:
        pipe_result: Base64-encoded result from the previous Celery task, if any.
        input_files: List of input file dictionaries (unused if pipe_result exists).
        output_path: Path to the output directory.
        workflow_id: ID of the workflow.
        task_config: User configuration for the task.

    Returns:
        Base64-encoded dictionary containing task results.
    """
    # Setup logger
    log_root.bind(workflow_id=workflow_id)
    logger.info(f"Starting {TASK_NAME} for workflow {workflow_id}")

    input_files = get_input_files(pipe_result, input_files or [])
    output_files = []
    base_command = ["<REPLACE_WITH_COMMAND>"]
    base_command_string = " ".join(base_command)

    for input_file in input_files:
        output_file = create_output_file(
            output_path,
            display_name=input_file.get("display_name"),
            extension="<REPLACE_WITH_FILE_EXTENSION>",
            data_type="<[OPTIONAL]_REPLACE_WITH_DATA_TYPE>",
        )
        command = base_command + [input_file.get("path")]

        # Run the command
        with open(output_file.path, "w") as fh:
            subprocess.Popen(command, stdout=fh, stderr=subprocess.PIPE)
        if process.stderr:
            logger.error(process.stderr.read())
        
        output_files.append(output_file.to_dict())

    return create_task_result(
        output_files=output_files,
        workflow_id=workflow_id,
        command=base_command_string,
        meta={},
    )
