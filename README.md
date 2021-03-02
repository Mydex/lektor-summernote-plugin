# Lektor basic Summernote version

This is a basic Lektor site which uses summernote as the editor

https://www.getlektor.com/
https://summernote.org/

## Getting started


Basic instructions to install are [here](https://www.getlektor.com/docs/installation/)

### Useful commands

`lektor server`

Starts a development server on port 5000 which allows editing content via the UI. 

There is a JavaScript addition ```javascripts/admin-utilities.js``` which allows the content to refresh and to save

`lektor build`

This generates static HTML which can be deployed to remote environments.

The Summernote plugin files are all contained within the ```packages``` folder.

Please refer to the official documentation for more info on what you can do in a Lektor:

https://www.getlektor.com/docs/

There is API documentation here: https://www.getlektor.com/docs/api
### CSS, Javascript and other assets

The directory `assets/` is where any assets such as CSS and Javascript should go. 

*IMPORTANT*: Even though the folder is `/assets`, the website will omit the `assets/` path, making it under `/` on the site,
so you may need to factor this in when using any hardcoded paths in the `layout.html` or `page.html`
### Menus

The site uses ```templates/navigation.html``` for the navigation menu.

Please see this documentation for more info: https://www.getlektor.com/docs/templates/navigation/

## Advanced - macros and models

There is basic support for defining different 'types' of content other than just page.

Different types are considered 'models' and can support other 'fields' than just 'title' and 'body'.

See `models/page.ini` for the basic page model that we are using.

See the official documentation for more info: https://www.getlektor.com/docs/models/


