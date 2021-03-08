# Lektor basic Summernote plugin

This is a [Lektor](https://www.getlektor.com/) plugin which utilises [Summernote](https://summernote.org/) as the editor/WYSIWYG.

This plugin also includes a script which allows the content to refresh and to save.

## Getting started

Basic instructions to install lektor can be found [here](https://www.getlektor.com/docs/installation/)

## Adding the plugin 

The plugin can be added as a Package by following the instructions [here](https://www.getlektor.com/docs/plugins/)

Alternatively it can ge added as a ```git submodule``` by creating a packages folder within your project and then using:

```$ git submodule add https://github.com/Mydex/lektor-summernote-plugin packages/lektor-summernote```

### Useful commands

`lektor server`

Starts a development server on port 5000 which allows editing content via the UI. 

`lektor build`

This generates static HTML which can be deployed to remote environments.

The Summernote plugin files are all contained within the ```packages``` folder.

Please refer to the official documentation for more info on what you can do in a Lektor:

https://www.getlektor.com/docs/

There is API documentation here: https://www.getlektor.com/docs/api

### Additional feature

There is the addition of a script to reload the page when navigating between pages or when using the browser navigation.
This is to resolve an issue where the page content is not refreshed as it should be.

### Known issues

When browsing between pages in the admin interface, a very brief popup error message appears via React as the browser
navigates away. 

It is harmless but we haven't found a way to hide it without modifying core parts of Lektor to squelch the message.
