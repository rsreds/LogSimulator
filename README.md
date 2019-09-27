# Log Simulator

<p align="center">
    <img src="static/img/LogoLogSimulator.png" width="300" >
</p>
Log Simulator is a project aimed at the development of a Log File generator with Python 3.6 backend.
The Log file generator should be able to produce a text file simulating a Log file of unstructured text, with a defined number of source template for every log line.
The number of parameters in every line and the size of the resulting file should be tunable from a configuration file.

The purpose of the generator is to output a Log Files with known defining parameter to test the effectiveness of different clustering algorithms to be used in real life situation.

## Usage

To run the simulator launch `sample.py`.
Use `-h` to list the possible arguments.

The parameters for the log files generation are configurable from the `config.json` file

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

The main developments branch is `dev`, please make a merge request before merging to the master branch.

Please make sure to update tests as appropriate.

## License

[MIT](./LICENSE)
