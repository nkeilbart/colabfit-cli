import click
import tqdm

OKGREEN = '\033[92m'
END = '\x1b[0m'
@click.group('colabfit')
@click.pass_context
def colabfit(ctx):
    """
    ColabFit Exchange: Data for Advanced Materials and Chemistry
    """
    ctx.ensure_object(dict)



#specify options for query 
#print summary message
#dump info out to stdout and have hyperlinked
#put default values
@colabfit.command('query')
@click.option('--text','-t',
        help="""Perform text search over dataset names, descriptions, and authors. 

        \b 
        See \033]8;;https://www.mongodb.com/docs/manual/reference/operator/query/text/#definition\033\\here\033]8;;\033\\ for examples.
        \b

        """,
        type=click.STRING,
        )
@click.option('--elements', '-e',
        help="""Returns datasets that contain specified elements. Datasets may contain more elements in addition to those queried. Use --elements-exact to return datasets that contain ONLY queried elements. Pass arguements as space delimited string.

        \b
        """,
        type=click.STRING)
@click.option('--elements-exact', '-ee',
        help="""Returns datasets that contain ONLY specified elements. Pass arguments as space-delimited string.

        \b

        """,
        type=click.STRING)
@click.option('--download', '-d',
        help="""Downloads all found datasets in specified format. Format can either be "xyz" or "lmdb".

        \b

        """,
        type=click.STRING)
@click.option('--property-types','-p',
        help="""Returns datasets that contain queried properties. 

        \b
        See property-name \033]8;;https://github.com/colabfit/colabfit-tools/blob/master/colabfit/tools/property_definitions.py\033\\here\033]8;;\033\\ for relevant properties. Pass arguements as space delimited string.

        \b

        """,
        type=click.STRING)
@click.pass_context
#more
def query(ctx,text,elements,elements_exact,download,property_types):
    """
    Queries the ColabFit Exchange and prints results. Optionally downloads resulting datasets.
    """
    from .utils import _query, format_print
    q = _query(text,elements,elements_exact,property_types)
    q = list(q)
    print (OKGREEN+"Found %s Dataset(s) on the ColabFit Exchange!" %len(q)+END)
    print ("--------------------------------------------")
    for i in q:
         format_print(i)
    if download in ["xyz", "XYZ", "lmdb", "LMDB"]:
        print ("--------------------------------------------")
        print ('Downloading Datasets')
        print ("--------------------")
    for i in tqdm.tqdm(q):
        _download(i,download)
        
