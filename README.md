# linear-models

Notes on linear statistical models, univariate models, multivariate models, empirical model building, and response surfaces.

On the Web: [http://charlesreid1.github.io/linear-models-notes](http://charlesreid1.github.io/linear-models-notes)

On Github: [http://github.com/charlesreid1/linear-models-notes](http://github.com/charlesreid1/linear-models-notes) 

<br />
<br />

## HTML Pages and Notebooks

The main output of the repository consists of HTML pages 
and Jupyter notebooks containing lecture notes and
example problems on various linear modeling topics. 

To generate these, use Pelican (see next section).

<br />
<br />

## Pelican Source Code

The source code for creating the HTMl and Jupyter notebooks
is organized as follows:

* Pelican is the Python module used to turn raw content into web content
    * `pelicanconf.py` is the main Pelican "Makefile"
    * `content/` directory will contain any pelican content

* Raw content in `content/` is turned into static web content in `docs`
    * Use `pelican content` command

* Jupyter notebooks are converted to HTML and added to `docs`
    * Jupyter nbconvert commands should be called by `pelicanconf.py`

* Static content in `docs` is hosted on Github Pages 
    * See link at top


### Configuration file:

The Pelican configuration file is `pelicanconf.py`.

### Raw Content: 

Pelican turns raw content (markdown, HTML-like Jinja templates)
into static HTML content.

The default location for Pelican content is `content/`. 
This is where it looks for markdown files to turn into static content.
You can add more locations by adding to the list `EXTRA_TEMPLATE_PATHS`
in `pelicanconf.py`.

Markdown files in `content/` will be rendered as blog posts. 
This is problematic if there is no support for blog stuff, 
as with the theme we are using,

Markdown files in `content/pages/` will be rendered as static 
HTML pages. Easy peasy. 

### Theme:

The basic template files are contained in the theme folder.
To add your own templates to customize the theme, add more paths
containing templates to the `EXTRA_TEMPLATES_PATHS` list 
in `pelicanconf.py`.

Also explicitly add HTML template pages like this:

```
TEMPLATE_PAGES['mypage.html'] = 'mypage.html'
TEMPLATE_PAGES['custompath.html'] = 'custom/path/custompath.html'
```

We use this to turn a custom HTML template into an index/splash page:

```
TEMPLATE_PAGES['splash.html'] = 'index.html'
```

### Splash/Landing Page:

The splash/landing page is a Jinja template at `content/splash.html`.
It is converted into the destination file `index.html` as per `pelicanconf.py`.
To modify the template, just edit `splash.html`. 
To use a different template as the splash page, just modify `pelicanconf.py`.

