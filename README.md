# Kedro Tutorial - Titanic Starter

## Overview

This project helps understand the basics of kedro by introducing you, in a step by step fashion, to its different concepts and tools.

By following along with this project, you will understand the concepts of **nodes**, **pipelines**, and **datasets**, and how to leverage them to create collaborative, scalable, production-ready data pipelines.

Follow along with this `README.md` file as it explains kedro's concepts.

#### Credits

A huge thank you to @agconti, whose notebook "Titanic" this tutorial is based directly off of. Please see his notebook here: [Titanic.ipynb](https://nbviewer.jupyter.org/github/agconti/kaggle-titanic/blob/master/Titanic.ipynb)

Another thank you to [Kaggle.com](kaggle.com), who was the provider of this titanic dataset in the competition [Titanic: Machine Learning from Disaster]()

## Tutorial


### Part 0: Installing Kedro

Kedro may be installed simply by using `pip` and the Python Package Index.

```bash
# Console
pip install kedro
```

**Optional** - If you prefer, you may use a virtual environment, or conda environment for the purposes of this tutorial.

```bash
# With Conda
conda create python=3.8 --name kedro-titanic-tutorial-conda 
conda activate !$
```

```bash
# With Virtual Environment (MacOSX)
virtualenv kedro-titanic-tutorial-venv
source !$/bin/activate
```

### Part 1: Hello World

#### Introduction to CLI

In order to interact with kedro, we use the kedro command line interface (CLI). Let's first get acquainted with the most important command, the `kedro run` command.

The `kedro run` command allows us to run our pipelines. But where are our pipelines? Traditionally, they can be found inside of the `src/{project_name}/pipeline.py` file (in our case, our project name is `tts`).

Looking inside of this file, we find a function called `create_pipelines`. By default, it is this function that is used by kedro to create the pipelines for our run. Notice the dictionary being returned, at the bottom. This dictionary is what determines the available pipelines for us to run.

There's one pipeline in particular we're going to try running, and that's the `hello-world` pipeline. Any keys in the dictionary being returned are available to the `kedro run` command.

```python
# src/tts/pipeline.py

def create_pipelines(**kwargs):
...
    return {
        ...
        "hello-world": hello_world.create_pipeline(),
        ...
    }
```

*Note: Notice that the value is actually being created inside of the module called `hello_world`, which exists inside of `src/tts/pipelines/`. Putting the pipeline implementation inside of the `pipelines` folder is a standard convention, to help encourage pipeline reuse.*

#### Run the Pipeline

Let's run the pipeline! Make sure you `cd` into the `titanic-tutorial-starter` project, first.

```bash
# Console
kedro run --pipeline hello-world
```

You should get an output similar to this

```bash
2020-08-31 09:48:07,098 - root - INFO - ** Kedro project kedro-tutorial-titanic-starter
2020-08-31 09:48:07,903 - kedro.pipeline.node - INFO - Running node: hello_world(None) -> [hello-output]
2020-08-31 09:48:07,903 - tts.pipelines.hello_world.nodes - INFO - Hello World!
2020-08-31 09:48:07,904 - kedro.io.data_catalog - INFO - Saving data to `hello-output` (MemoryDataSet)...
2020-08-31 09:48:07,904 - kedro.runner.sequential_runner - INFO - Completed 1 out of 1 tasks
2020-08-31 09:48:07,904 - kedro.runner.sequential_runner - INFO - Pipeline execution completed successfully.
2020-08-31 09:48:07,904 - kedro.io.data_catalog - INFO - Loading data from `hello-output` (MemoryDataSet)...
```

We did it! Congratulations, you've just successfully run a kedro pipeline.

### Part 2: Connecting a DataSet to Nodes in a Pipeline

#### Explanation of Kedro Concepts

Now that we know how to run pipelines, let's get a handle on what a "pipeline" actually is.

In kedro, there are 3 important constructs to understand. In this section, we're going to cover 

1. Pipelines
2. Nodes
3. DataSets

We've already run our first pipeline, but what is a pipeline, exactly? A pipeline is a simple construct that ties all of your data (in the form of DataSets) and transformations (in the form of nodes). You put data in one side, and out the other side comes transformed data.

Represented in the following illustration is a "Circles to Triangles Pipeline." Here, the cylinders represent DataSets, the cube represents a Node, and all of the Yellow represents the Pipeline.  
The "Circles DataSet" is a data source that contains a "rows of circles" and the transformation function will take each "circle row" turning it into a "triangle row," outputting it to a "Triangles DataSet."

The important thing to point out is all of the yellow, which represents the Pipeline.  
It's responsible for tying all of the DataSets and Nodes together by

1. Moving data from the input DataSet into the Node
2. Moving data from the Node into the output DataSet

Below, "Circles" is the input DataSet and "Triangles" is the output DataSet.

![Pipeline](images/pipeline.jpg)

If the previous illustration were to be represented in Pipeline code, it would look like this.

```python
from kedro.pipeline import Pipeline, node
from .lib import circles_to_triangle

def create_pipeline():

    return Pipeline([
        node(
            circles_to_triangle,
            inputs="Circles",
            outputs="Triangles",
        )       
    ])
```

The `node` function requires three arguments in order to create a node. The first is a function, representing the function the node is to run, the second is the inputs to the function and the third is the outputs of that function. Kedro will take the input data as pass it to the function directly to the arguments of the function, as well as take any output of the function and pass it to output datasets.

### Connecting our DataSet to our Node

For this exercise, we're going to be connecting the `titanic_training_data` DataSet to the `survival_breakdown` pipeline.
