#!/usr/bin/python3
"""yaml.dumps() expects a single argument
   performs the YAML transformation,
   and returns that as a YAML string | Alta3 Research"""

# YAML is NOT part of the standard library
# python3 -m pip install pyyaml
import yaml

def main():
    """runtime code"""
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]

    ## display our Python data (a list containing two dictionaries)
    print(hitchhikers)

    ## Create the YAML string
    yamlstring = yaml.dump(hitchhikers)

    ## Display a single string of YAML
    print(yamlstring)

if __name__ == "__main__":
    main()

