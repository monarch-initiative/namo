# Examples of using namo

This folder contains examples using the datamodel.

The source of the data used in the example is [tests/data](../tests/data/).

The command `just test` creates different representations of the data in [tests/data](../tests/data/) and writes them to the subfolder `output`, one JSON and one YAML file per example.
It also writes a log of the run, with each example's input and output, to `tmp/linkml-run-examples.md`, which is not tracked.
