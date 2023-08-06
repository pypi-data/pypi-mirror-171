# IrisML

Proof of Concept for a simple framework to create a ML pipeline.


# Features
- Run a ML training/inference with a simple JSON configuration.
- Modularized interfaces for task components.
- Cache task outputs for faster experiments.

# Getting started
## Installation
Prerequisite: python 3.8+

```
# Install the core framework and standard tasks.
pip install irisml irisml-tasks irisml-tasks-training
```

## Run an example job
```
# Install additional packages that are required for the example
pip install irisml-tasks-torchvision

# Run on local machine
irisml_run docs/examples/mobilenetv2_mnist_training.json
```

## Available commands
```
# Run the specified pipeline. You can provide environment variables by "-e" option, which will be acceible through $env variable in the json config.
irisml_run <pipeline_json_path> [-e <ENV_NAME>=<env_value>] [--no_cache] [-v]

# Show information about the specified task. If <task_name> is not provided, shows a list of available tasks in the current environment.
irisml_show [<task_name>]
```

## Pipeline definition
```
PipelineDefinition = {"tasks": List[TaskDefinition], "on_error": Optional[List[TaskDescription]]}

TaskDefinition = {
    "task": <task module name>,
    "name": <optional unique name of the task>,
    "inputs": <list of input objects>,
    "config": <config for the task. Use irisml_show command to find the available configurations.>
}
```
In the TaskDefinition.inputs and TaskDefinition.config, you cna use the following two variable.
- $env.<variable_name>
  This variable will be replaced by the environment variable that was provided as arguments for irisml_run command.
- $outputs.<task_name>.<field_name>
  This variable will be replaced by the outputs of the specified previous task.

It raises an exception on runtime if the specified variable was not found.

If a task raised an exception, the tasks specified in on_error field will be executed. The exception object will be assigned to "$env.IRISML_EXCEPTION" variable.

## Pipeline cache
Using cache, you can modify and re-run a pipeline config with minimum cost. If the cache is enabled, IrisML will calculate hash values for all task inputs/configs and upload the task outputs to a specified storage. When it found a task with same hash values, it can download the cache and skip the task execution.

To enable cache, you must specify the cache storage location by setting IRISML_CACHE_URL environment variable. Currently Azure Blob Storage and local filesystem is supported.

To use Azure Blob Storage, a container URL must be provided. It the URL contains a SAS token, it will be used for authentication. Otherwise, interactive authentication and Managed Identity authentication will be used.

# List of available tasks

To show the detailed help for each task, run the following command after installing the package.
```
irisml_show <task_name>
```

## [irisml-tasks](https://github.com/microsoft/irisml-tasks)
- assert
- download_azure_blob
- get_dataset_stats
- get_dataset_subset
- get_fake_image_classification_dataset
- get_fake_object_detection_dataset
- get_item
- load_state_dict
- run_parallel
- run_sequential
- save_file
- save_state_dict
- search_grid_sequential
- upload_azure_blob

## [irisml-tasks-training](https://github.com/microsoft/irisml-tasks-training)
This package contains tasks related to pytorch training
- append_classifier
- build_classification_prompt_dataset
- build_zero_shot_classifier
- create_classification_prompt_generator
- evaluate_accuracy
- evaluate_detection_average_precision
- export_onnx
- get_targets_from_dataset
- load_state_dict
- make_feature_extractor_model
- make_image_text_contrastive_model
- make_image_text_transform
- predict
- save_state_dict
- split_image_text_model
- train

## [irisml-tasks-torchvision](https://github.com/microsoft/irisml-tasks-torchvision)
- load_torchvision_dataset
- create_torchvision_model
- create_torchvision_transform

## [irisml-tasks-timm](https://github.com/microsoft/irisml-tasks-timm)
Adapter for models in timm library
- create_timm_model


## [irisml-tasks-azureml](https://github.com/microsoft/irisml-tasks-azureml)
- run_azureml_child

## [irisml-tasks-fiftyone](https://github.com/microsoft/irisml-tasks-fiftyone)
- launch_fiftyone

# Development
## Create a new task
To create a Task, you must define a module that contains a "Task" class. Here is a simple example:
```python
# irisml/tasks/my_custom_task.py
import dataclasses
import irisml.core

class Task(irisml.core.TaskBase):  # The class name must be "Task".
  VERSION = '1.0.0'
  CACHE_ENABLED = True  # (default: True) This is optional.

  @dataclasses.dataclass
  class Inputs:  # You can remove this class if the task doesn't require inputs.
    int_value: int
    float_value: float

  @dataclasses.dataclass
  class Config:  # If there is no configuration, you can remove this class. All fields must be JSON-serializable.
    another_float: float
    child_dataclass: dataclass  # If you'd like to define a nested config, you can define another dataclass.

  @dataclasses.dataclass
  class Outputs:  # Can be removed if the task doesn't have outputs.
    float_value: float = 0  # If dry_run() is not implemented, Outputs fields must have default value or default factory.

  def execute(self, inputs: Inputs) -> Outputs:
    return self.Outputs(inputs.int_value * inputs.float_value * self.config.another_float)

  def dry_run(self, inputs: Inputs) -> Outputs:  # This method is optional.
    return self.Outputs(0)  # Must return immediately without actual processing.
```

Each Task must define "execute" method. The base class has empty implementation for Inputs, Config, Outputs and dry_run(). For the detail, please see the document for TaskBase class.

# Related repositories
- [irisml-tasks](https://github.com/microsoft/irisml-tasks)
- [irisml-tasks-training](https://github.com/microsoft/irisml-tasks-training)
- [irisml-tasks-torchvision](https://github.com/microsoft/irisml-tasks-torchvision)
- [irisml-tasks-transformers](https://github.com/microsoft/irisml-tasks-transformers)
- [irisml-tasks-timm](https://github.com/microsoft/irisml-tasks-timm)
- [irisml-tasks-azureml](https://github.com/microsoft/irisml-tasks-azureml)
- [irisml-tasks-fiftyone](https://github.com/microsoft/irisml-tasks-fiftyone)
