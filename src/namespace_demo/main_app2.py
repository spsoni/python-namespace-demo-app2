from namespace_demo.main import cli

from namespace_demo.base.base_module import random_name
from namespace_demo.base.shared import hello_world
from namespace_demo.app2.add_space import add_space

@cli.command
def app2():
    name = random_name()
    spaced_name = add_space(name)
    hello_world(spaced_name)


if __name__ == '__main__':
    cli()
