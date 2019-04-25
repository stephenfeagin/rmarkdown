"""
Nikola Page Compiler for R Markdown files
"""

from nikola import shortcodes as sc
from nikola.plugin_categories import PageCompiler
from nikola.utils import makedirs, req_missing, write_metadata


class CompileRMarkdown(PageCompiler):
    """PageCompiler for R Markdown files"""
    
    name = "rmarkdown"
    pass
