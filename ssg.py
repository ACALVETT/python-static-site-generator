import typer
from ssg.site import Site
from ssg.site import Parsers

def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest}
    Site(**config).build()


typer.run(main)

