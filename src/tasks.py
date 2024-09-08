import subprocess

from openrelik_worker_common.utils import (
    create_output_file,
    get_input_files,
    task_result,
)

from .app import celery

# Task name used to register and route the task to the correct queue.
TASK_NAME = "your-worker-package-name.tasks.your_task_name"

# Task metadata for registration in the core system.
TASK_METADATA = {
    "display_name": "<SHORT NAME FOR YOUR WORKER>",
    "description": "<DESCRIPTION FOR YOUR WORKER>",
}


@celery.task(bind=True, name=TASK_NAME, metadata=TASK_METADATA)
def command(
    self,
    pipe_result: str = None,
    input_files: list = None,
    output_path: str = None,
    workflow_id: str = None,
    user_config: dict = None,
) -> str:
    """Run <COMMAND> on input files.

    Args:
        pipe_result: Base64-encoded result from the previous Celery task, if any.
        input_files: List of input file dictionaries (unused if pipe_result exists).
        output_path: Path to the output directory.
        workflow_id: ID of the workflow.
        user_config: User configuration for the task (currently unused).

    Returns:
        Base64-encoded dictionary containing task results.
    """
    input_files = get_input_files(pipe_result, input_files or [])
    output_files = []
    base_command = ["<COMMAND>"]
    base_command_string = " ".join(base_command)

    for input_file in input_files:
        output_file = create_output_file(
            output_path,
            filename=input_file.get("filename"),
            file_extension="<FILE EXTENSION>",
        )
        command = base_command + [input_file.get("path")]

        # Run the command
        with open(output_file.path, "w") as fh:
            subprocess.Popen(command, stdout=fh)

        output_files.append(output_file.to_dict())

    if not output_files:
        raise RuntimeError("<ERROR STRING>")

    return task_result(
        output_files=output_files,
        workflow_id=workflow_id,
        command=base_command_string,
        meta={},
    )
