```
  _____                     _              ____        _ _                 _       _         ___       _ _   _       _ _          _             
 |  ___|__  _   _ _ __   __| |_ __ _   _  | __ )  ___ (_) | ___ _ __ _ __ | | __ _| |_ ___  |_ _|_ __ (_) |_(_) __ _| (_)______ _| |_ ___  _ __ 
 | |_ / _ \| | | | '_ \ / _` | '__| | | | |  _ \ / _ \| | |/ _ \ '__| '_ \| |/ _` | __/ _ \  | || '_ \| | __| |/ _` | | |_  / _` | __/ _ \| '__|
 |  _| (_) | |_| | | | | (_| | |  | |_| | | |_) | (_) | | |  __/ |  | |_) | | (_| | ||  __/  | || | | | | |_| | (_| | | |/ / (_| | || (_) | |   
 |_|  \___/ \__,_|_| |_|\__,_|_|   \__, | |____/ \___/|_|_|\___|_|  | .__/|_|\__,_|\__\___| |___|_| |_|_|\__|_|\__,_|_|_/___\__,_|\__\___/|_|   
                                   |___/                            |_|                                                                         
```
A Foundry VTT initializator for the Boilerplate system!

## How to use:
- Copy the `startBoilerplate.py` to your repository
- Run `python startBoilerplate.py true|false`
    - The argument passed is the Dry Run configuration.
        - If passed `true`, it will execute the process as a "Dry Run" not changing the files
        - If passed `false`, it will execute the process as a "Wet Run", changing files
        - If the argument is ommited, it wil execute the process as a "Wet Run", changing files
- Choose your system name
    - The script will replace using the following pattern:
        - `boilerplate` => your system name in lower case
        - `BOILERPLATE` => your system name in upper case
        - `Boilerplate` => your system name capitalized
